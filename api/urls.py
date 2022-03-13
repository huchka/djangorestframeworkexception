from django.urls import path

from api.views import HelloWorld

urlpatterns = [
    # api001 - post
    path(
        "helloworld/",
        HelloWorld.as_view(),
        name="hello_world",
    )
]
