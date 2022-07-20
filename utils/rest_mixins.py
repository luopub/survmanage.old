from django.http.response import Http404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import models
from django.db.models import Sum, Count
from django.db.models import Min, Max, Avg, StdDev, Variance

from utils.logutils import get_logger

logger = get_logger('rest_mixins')


class GroupbyMixin:

    def custom_transform(self, queryset):
        # We can do some custom transformation before grouping
        return queryset

    def calc_change_rage(self, page_response, fields):
        """
        Calculate change rate on fields. Fields are separated by comma
        """
        results = page_response.data['results']
        fields = fields.split(',')
        for f in fields:
            nf = f'{f}_ch'
            for i, r in enumerate(results):
                if i == len(results) - 1:
                    r[nf] = 0.0
                else:
                    try:
                        r[nf] = (r[f] - results[i+1][f]) / results[i+1][f]
                    except Exception as e:
                        r[nf] = None

        return page_response

    @action(detail=False, methods=['get'])
    def groupby(self, request):
        """
        This is a general groupby api, query params are:
            by: <group fields seperate by comma>, if it's not given, then annotate are act upon whole table
            count: <count fields seperate by comma>
            max: <max fields seperate by comma>
            min: <min fields seperate by comma>
            sum: <sum fields seperate by comma>
        """
        queryset = self.filter_and_groupby(request)
        response = self.paginate_for_grouped(queryset)
        # check if any field need to calculate change rate
        change_rate = request.query_params.get('change_rate')
        if change_rate:
            response = self.calc_change_rage(response, change_rate)

        return response

    def filter_and_groupby(self, request):

        queryset = self.get_queryset()

        queryset = self.custom_transform(queryset)

        queryset = self.filter_queryset(queryset)

        by = request.query_params.get('by', default=None)
        if by:
            bys = by.split(',')
            queryset = queryset.values(*bys)

        def annotate_fields(request, queryset, key, func):
            """
            Annotate the queryset with parameters from request
            :param request:
            :param queryset:
            :param key: query param key
            :param func: functor for the key
            :return: the queryset
            """
            fstr = request.query_params.get(key, default=None)
            if fstr:
                fields = fstr.split(',')
                defaults = {}
                for f in fields:
                    defaults[key + '_' + f] = func(f)
                queryset = queryset.annotate(**defaults)

            return queryset

        queryset = annotate_fields(request, queryset, 'count', Count)

        queryset = annotate_fields(request, queryset, 'max', Max)

        queryset = annotate_fields(request, queryset, 'min', Min)

        queryset = annotate_fields(request, queryset, 'sum', Sum)

        queryset = annotate_fields(request, queryset, 'avg', Avg)

        queryset = annotate_fields(request, queryset, 'stddev', StdDev)

        queryset = annotate_fields(request, queryset, 'variance', Variance)

        ordering = request.query_params.get('ordering', default=None)
        if ordering:
            orderings = ordering.split(',')
            queryset = queryset.order_by(*orderings)
        else:
            # default order is the group by field
            if by:
                queryset = queryset.order_by(*bys)

        return queryset

    def paginate_for_grouped(self, queryset, hook_before_serialize=None):
        if queryset and isinstance(queryset.first(), models.Model):
            # If not grouped-by, result is queryset of Model
            page = self.paginate_queryset(queryset)
            if page is not None:
                if hook_before_serialize:
                    page = hook_before_serialize(page)
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)
            else:
                if hook_before_serialize:
                    queryset = hook_before_serialize(queryset)
                serializer = self.get_serializer(queryset, many=True)
                return Response(serializer.data)
        else:
            # If grouped-by, result is queryset of dict
            page = self.paginate_queryset(queryset)
            if page is not None:
                if hook_before_serialize:
                    page = hook_before_serialize(page)
                return self.get_paginated_response(page)
            else:
                if hook_before_serialize:
                    queryset = hook_before_serialize(queryset)
                return Response(queryset)


class SingleFieldMixin:

    @action(detail=False, methods=['get'])
    def single_field(self, request):
        """
        Get value of a single field from the model. The returned value can be bare values list (bare_value=1) or dict list
        :param request:
        :return:
        """

        queryset = self.get_queryset()

        queryset = self.filter_queryset(queryset)

        field = request.query_params.get('field', default=None)

        if not field:
            raise Http404('"field" param is required')

        queryset = queryset.values(field)

        page = self.paginate_queryset(queryset)

        bare_values = request.query_params.get('bare_values', default=None)
        if bare_values:
            bare_values = int(bare_values)

        if page is not None:
            if bare_values:
                page = [item[field] for item in page]

            return self.get_paginated_response(page)
        else:
            if bare_values:
                queryset = [item[field] for item in queryset]

            return Response(queryset)
