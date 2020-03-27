from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),

    path('results/', views.results, name='results'),

    path('<gwevent>/', views.fields, name='fields'),

    path('<gwevent>/<field_name>/', views.candidates, name='candidates'),

    path('<gwevent>/<field_name>/<candidate_id>/likely/', views.likelyvote),

    path('<gwevent>/<field_name>/<candidate_id>/possible/', views.possiblevote),

    path('<gwevent>/<field_name>/<candidate_id>/unlikely/', views.unlikelyvote)
]
