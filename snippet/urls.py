from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.SnippetList.as_view()),
    url(r'(?P<pk>[a-z0-9]+)', views.SnippetDetail.as_view()),
]
