from django.urls import path

from api.views import HelloWorld

urlpatterns = [
    path(
        "helloworld/",
        HelloWorld.as_view(),
        name="hello_world",
    )
]
