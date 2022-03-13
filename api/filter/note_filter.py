from django_filters import rest_framework

from api.models import Note

DATE_INPUT_FORMATS = ["iso_8601", "%Y/%m/%d", "%Y/%m/%d %H:%M", "%Y/%m/%d %H:%M:%S"]


class NoteFilters(rest_framework.FilterSet):

    title = rest_framework.CharFilter(field_name="title")

    date_from = rest_framework.IsoDateTimeFilter(
        field_name="created_datetime",
        input_formats=DATE_INPUT_FORMATS,
        lookup_expr="gte",
    )

    class Meta:
        model = Note
        fields = ["title", "modified_datetime"]
