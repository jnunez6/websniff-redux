from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [

    url(r'^$', views.index, name='index'),

    url(r'^firstpush/$', views.firstpush, name='First Push'),

    url(r'^secondpush/$', views.secondpush, name='Second Push'),

    url(r'^likelycandidates/$', views.likelycandidates, name='Likely Candidates'),

    url(r'^results/$', views.results, name='results'),

    url(r'^<gwevent>/$', views.fields, name='fields'),

    url(r'^<gwevent>/<field_name>/$', views.candidates, name='candidates'),

    url(r'^<gwevent>/<field_name>/<candidate_id>/likely/$', views.likelyvote),

    url(r'^<gwevent>/<field_name>/<candidate_id>/possible/$', views.possiblevote),

    url(r'^<gwevent>/<field_name>/<candidate_id>/unlikely/$', views.unlikelyvote)
]
