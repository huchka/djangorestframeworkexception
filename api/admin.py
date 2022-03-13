from django.contrib import admin

from api.models import Note

# admin.site.register(Note)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "created_datetime",
        "modified_datetime",
    )
    list_filter = (
        "title",
        "created_datetime"
    )
