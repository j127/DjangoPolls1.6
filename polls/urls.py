from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<poll_id>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<poll_id>\d+)/results/$', views.ResultsView.as_view(), name='results'),
        url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
