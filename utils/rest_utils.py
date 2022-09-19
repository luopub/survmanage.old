from rest_framework import renderers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import serializers
from django_filters.filters import Filter
from django_filters import rest_framework as filters

from .utils import get_all_fields, get_filter_for_all_fields, get_ordering_fields

from utils.logutils import get_logger
logger = get_logger('rest_utils')


class MyJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        if 200 <= status_code < 300 and data and 'code_message' in data:
            code = data['code_message']['code']
            message = data['code_message']['message']
            data = {k: data[k] for k in data if k != 'code_message'}
        else:
            code = 0 if 200 <= status_code < 300 else status_code
            message = 'Success' if 200 <= status_code < 300 else 'Failed'

        # Benzhi require msg field
        data = {'code': code, 'msg': message, 'message': message, 'data': data}
        return super().render(data, accepted_media_type, renderer_context)


# class MyReadOnlyModelViewSet(MyRetrieveModelMixin, MyListModelMixin, viewsets.GenericViewSet):
class MyReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    renderer_classes = (MyJSONRenderer, renderers.BrowsableAPIRenderer)
    pass


# class MyReadOnlyModelViewSet(MyRetrieveModelMixin, MyListModelMixin, viewsets.GenericViewSet):
class MyModelViewSet(viewsets.ModelViewSet):
    renderer_classes = (MyJSONRenderer, renderers.BrowsableAPIRenderer)
    pass


class MyResponse(Response):
    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 exception=False, content_type=None, code=0, message='Success'):
        data = {'code': code, 'message': message, 'data': data}
        super().__init__(data=data, status=status,
                         template_name=template_name, headers=headers,
                         exception=exception, content_type=content_type)


EMPTY_VALUES = ([], (), {}, '', None)


class ArrayFilter(Filter):
    """
    Filtering the array fields
    """
    @staticmethod
    def value_to_array(value):
        return [v for v in value.split(',')]

    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs

        # Convert string to array, otherwise it can't be evaluated
        value = self.value_to_array(value)

        if self.distinct:
            qs = qs.distinct()
        lookup = '%s__%s' % (self.field_name, self.lookup_expr)
        qs = self.get_method(qs)(**{lookup: value})
        return qs


class IntArrayFilter(ArrayFilter):
    """
    Filtering the int array fields
    """
    @staticmethod
    def value_to_array(value):
        return [int(v) for v in value.split(',')]


class CharArrayFilter(ArrayFilter):
    """
    Filtering the char array fields
    """
    pass


class SimpleViewSetBase(type):
    """
    This is a shortcut to create viewset class. Only one "model" field is required. The simple view set is like below:

        class WishTaosjProductFlySerializer(serializers.ModelSerializer):
            class Meta:
                model = WishTaosjProductFly
                fields = get_all_fields(WishTaosjProductFly, remove_sets=True)


        class WishTaosjProductFlyFilter(filters.FilterSet):
            class Meta:
                model = WishTaosjProductFly
                fields = get_filter_for_all_fields(WishTaosjProductFly)


        class WishTaosjProductFlyViewSet(GroupbyMixin, MyModelViewSet):
            queryset = WishTaosjProductFly.objects.all()
            serializer_class = WishTaosjProductFlySerializer
            filterset_class = WishTaosjProductFlyFilter
            search_fields = []
            ordering_fields = get_ordering_fields(WishTaosjProductFly)
            ordering = []

    The above is replaced by:

        class WishTaosjProductFlyViewSet(GroupbyMixin, MyModelViewSet, metaclass=SimpleViewSetBase):
            model = WishTaosjProductFly
    """
    def __new__(cls, name, bases, attrs, **kwargs):
        model = attrs['model']
        serial_depth = attrs.get('serial_depth', 0)

        serializer_class = attrs.get('serializer_class')
        if not serializer_class:
            serial_fields = get_all_fields(model, remove_sets=True) if not serial_depth else '__all__'
            _serializer_meta = type(model.__name__ + 'SerializerMeta', (), {'model': model, 'fields': serial_fields, 'depth': serial_depth})
            serializer_class = type(model.__name__ + 'Serializer', (serializers.ModelSerializer, ), {'Meta': _serializer_meta})

        filterset_class = attrs.get('filterset_class')
        if not filterset_class:
            _filter_meta = type(model.__name__ + 'FilterMeta', (), {'model': model, 'fields': get_filter_for_all_fields(model)})
            filterset_class = type(model.__name__ + 'Filter', (filters.FilterSet, ), {'Meta': _filter_meta})

        attrs = {**attrs}

        # All fields below are optional
        attrs.update({
            # model.__name__ + 'Serializer': _serializer,
            # model.__name__ + 'Filter': _filter,
            'queryset': attrs.get('queryset') or model.objects.all(),
            'serializer_class': serializer_class,
            'filterset_class': filterset_class,
            'search_fields': attrs.get('search_fields') or [],
            'ordering_fields': attrs.get('ordering_fields') or get_ordering_fields(model),
            'ordering': attrs.get('ordering') or []
        })
        view_set = super().__new__(cls, name, bases, attrs, **kwargs)
        return view_set
