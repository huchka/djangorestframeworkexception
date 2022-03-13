from django.urls import path

from api.views import HelloWorld, NoteList

urlpatterns = [
    path(
        "helloworld/",
        HelloWorld.as_view(),
        name="hello_world",
    ),
    path(
        "note/",
        NoteList.as_view(),
        name="note_controller"
    )
]
