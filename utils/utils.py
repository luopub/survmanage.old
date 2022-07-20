import heapq
import zipfile
import hashlib
import html
import re
import json
import datetime
from collections import defaultdict
from django.conf import settings as st
from PIL import Image
import numpy as np
import random
import html2text
import pandas as pd
import time
from django.utils import timezone
import inspect
import requests
import tempfile
import os
import stat
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from urllib3.exceptions import ConnectTimeoutError
from django_filters.filters import RangeFilter, TimeRangeFilter
from django.db import models
from django.conf import settings
from django.db.models.query_utils import DeferredAttribute
from django.db.models.fields.related_descriptors import (
    ForeignKeyDeferredAttribute, ForwardManyToOneDescriptor,
    ForwardOneToOneDescriptor, ManyToManyDescriptor,
    ReverseManyToOneDescriptor, ReverseOneToOneDescriptor,
)
from django.http.response import Http404, HttpResponse
from urllib.parse import urlparse
from utils.logutils import get_logger


logger = get_logger('utils_utils')


def decodeHtml(input):
    s = html.unescape(input)
    return s


def md5_encrypt_chunks(chunks):
    md5 = hashlib.md5()
    for chunk in chunks:
        if chunk:
            md5.update(chunk)
    result = md5.hexdigest()

    return result


def md5_encrypt(content):
    return md5_encrypt_chunks([content])


class JsonDateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


def get_all_fields(model, remove_sets=False, only_reverse=False, no_reverse=False, no_many=False, exclude_fields=None):
    """
    Get a model's all fields including xxx_set
    :param remove_sets, remove xxx_set from result
    :param only_reverse, keeps only xxx_set in result
    :param no_reverse
    :param no_many
    :param exclude_fields
    """
    members = inspect.getmembers(model)
    memnames = [m[0] for m in members]

    if not exclude_fields:
        exclude_fields = []

    if only_reverse:
        accepted_types = [ReverseManyToOneDescriptor, ReverseOneToOneDescriptor]

    else:
        accepted_types = [DeferredAttribute, ForeignKeyDeferredAttribute, ForwardOneToOneDescriptor]
        if remove_sets:
            no_reverse = True
            no_many = True

        if not no_reverse and not no_many:
            accepted_types.extend([ForwardManyToOneDescriptor, ManyToManyDescriptor, ReverseManyToOneDescriptor, ReverseOneToOneDescriptor])
        elif not no_reverse and no_many:
            accepted_types.extend([ReverseOneToOneDescriptor])
        elif no_reverse and not no_many:
            accepted_types.extend([ForwardManyToOneDescriptor, ManyToManyDescriptor])

    f = filter(lambda x: isinstance(getattr(model, x), tuple(accepted_types)), memnames)

    # if the field is a related field and has _id ending, then remove it
    fields = map(lambda x: x[:-3] if str(getattr(model, x)).find('.related_descriptors.') >= 0 and x.endswith('_id') else x, f)

    fields = filter(lambda x: x not in exclude_fields, fields)

    return list(fields)


def get_filter_for_all_fields(model, all_exact=True, all_number=True, all_datetime=True, all_null=True, char_icontains=True, more_filters=None, excepted_fields=None):
    """
    Get filter fields of 'exact' for all fields of a model
    :param model:
    :param all_exact: Add 'exact' filter method for all field except JSONField and ArrayField
    :param all_number: Add 'lte' and 'gte' filter methods for all number fields
    :param all_datetime: Add 'lte' and 'gte' filter methods for all date and time fields
    :param all_null: Add 'isnull' filter method for all nullable fields
    :param more_filters: The filters in addtion to the basic exact query methods
    :return:
    """
    if not more_filters:
        more_filters = {}

    if not excepted_fields:
        excepted_fields = {}

    fields = get_all_fields(model, remove_sets=True)

    filters = dict()
    for field in fields:
        methods = set(more_filters.get(field, []))

        if field not in excepted_fields:
            # if field not in excepted_fields:
            # if all_exact and not isinstance(getattr(model, field).field, JSONField) \
            #         and not isinstance(getattr(model, field).field, ArrayField):
            if all_exact:
                methods = methods.union({'exact'})

            # if field not in excepted_fields:
            if char_icontains and isinstance(getattr(model, field).field, models.CharField):
                methods = methods.union({'icontains'})

            # BigIntegerField and SmallIntegerField are subclasses of IntegerField
            if all_number and (isinstance(getattr(model, field).field, models.IntegerField)
                               or isinstance(getattr(model, field).field, models.FloatField)
                               or isinstance(getattr(model, field).field, models.DecimalField)):
                methods = methods.union({'lte', 'gte', 'lt', 'gt'})

            # DateTimeField is a subclass of DateField
            if all_datetime and (isinstance(getattr(model, field).field, models.DateField)
                                 or isinstance(getattr(model, field).field, models.TimeField)):
                methods = methods.union({'lte', 'gte', 'lt', 'gt'})

            if all_null and getattr(model, field).field.null:
                methods = methods.union({'isnull'})

        # Query methods should not be empty
        if len(methods):
            filters[field] = list(methods)

    return filters


def get_ordering_fields(model, all_char=True, all_number=True, all_datetime=True, all_boolean=True):
    """
    Get filter fields of 'exact' for all fields of a model
    :param model:
    :param all_char: Add all CharField to ordering
    :param all_number: Add all NumberField to ordering
    :param all_datetime: Add all DateTimeField to ordering
    :param all_null: Add all BooleanField to ordering
    :param more_filters: The filters in addtion to the basic exact query methods
    :return:
    """
    fields = get_all_fields(model, remove_sets=True)

    orderings = []
    for field in fields:
        if all_char and isinstance(getattr(model, field).field, (models.CharField, )):
            orderings.append(field)

        if all_number and isinstance(getattr(model, field).field,
                                     (models.IntegerField, models.FloatField, models.DecimalField,
                                      models.AutoField, models.BigAutoField, models.SmallAutoField)):
            orderings.append(field)

        if all_datetime and isinstance(getattr(model, field).field, (models.DateField, models.TimeField)):
            orderings.append(field)

        if all_boolean and isinstance(getattr(model, field).field, (models.BooleanField, )):
            orderings.append(field)

    return orderings


def get_range_filters(model, all_number=True, all_datetime=False, excepted_fields=None):
    """
    Get range filters for number and datetime.
    Range filter can't be simply listed in Meta.fields, it must be created explicitly
    :param model:
    :param all_number: Add 'lte' and 'gte' filter methods for all number fields
    :param all_datetime: Add 'lte' and 'gte' filter methods for all date and time fields
    :param excepted_fields: The filters in addtion to the basic exact query methods
    :return:
    """
    if not excepted_fields:
        excepted_fields = {}

    fields = get_all_fields(model, remove_sets=True)

    filters = dict()
    for field in fields:
        if field not in excepted_fields:
            # BigIntegerField and SmallIntegerField are subclasses of IntegerField
            if all_number \
                and (isinstance(getattr(model, field).field, models.IntegerField)
                     or isinstance(getattr(model, field).field, models.FloatField)
                     or isinstance(getattr(model, field).field, models.DecimalField)):
                filters[field] = RangeFilter(field_name=field)

            # DateTimeField is a subclass of DateField
            # if all_datetime \
            #     and (isinstance(getattr(model, field).field, models.DateField)
            #          or isinstance(getattr(model, field).field, models.TimeField)):
            #     filters[field] = TimeRangeFilter(field_name=field)

    return filters


def today():
    return timezone.now().date()


def current_hour():
    return timezone.now().hour


def values_list_to_list(values_list):
    """
    Django query_set.values_list() will return in the form [(v0, ), (v1, ), ...],
    that's not friendly, convert to [v0, v1, ...]
    :param values_list:
    :return:
    """
    return [v[0] for v in values_list]


def get_kwargs_if_avail(request_data, names, kwargs=None):
    """
    Get list of kwargs from request's data field. If exist, set it in kwargs.
    :param request_data:
    :param names:
    :param kwargs:
    :return:
    """
    if kwargs is None:
        kwargs = dict()

    for name in names:
        value = request_data.get(name)
        if value is not None:
            kwargs[name] = value

    return kwargs


def get_obj_spec_attrs(obj, base_obj=object):
    """
    Get all attribute's name of an object that are different from base object
    :param obj:
    :param base_obj:
    :return: sorted attribute names
    """
    return sorted(list(set(dir(obj)) - set(dir(base_obj))))


def get_cursor_dict_results(cursor):
    """
    Get result from cursor and made the resuls in dict list
    """
    fields = [f[0] for f in cursor.description]
    res = cursor.fetchall()
    return [dict(zip(fields, r)) for r in res]
