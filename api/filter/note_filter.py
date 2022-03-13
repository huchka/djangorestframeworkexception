import logging

from django_filters import rest_framework
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from api.models import Note

DATE_INPUT_FORMATS = ["iso_8601", "%Y/%m/%d", "%Y/%m/%d %H:%M", "%Y/%m/%d %H:%M:%S"]

# logging
logger = logging.getLogger(__file__)


class NoteFilters(rest_framework.FilterSet):

    title = rest_framework.CharFilter(
        field_name="title",
        lookup_expr="contains"
    )

    rank = rest_framework.NumberFilter(
        field_name="rank",
        lookup_expr="gte"
    )

    date_from = rest_framework.IsoDateTimeFilter(
        field_name="created_datetime",
        input_formats=DATE_INPUT_FORMATS,
        lookup_expr="gte",
    )

    class Meta:
        model = Note
        fields = ["title", "modified_datetime"]
