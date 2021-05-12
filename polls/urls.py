from django.urls import path

from polls import views


urlpatterns = [
    path('', views.home, name='home'),
    path('polls/', views.create_polls, name='create_polls'),
    path('polls/<uuid:poll_id>/vote/', views.vote, name='vote'),
    path('polls/<uuid:slug>/results/', views.ResultsView.as_view(), name='results'),  
]