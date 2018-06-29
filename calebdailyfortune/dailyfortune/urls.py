# dailyfortune/urls.py
from django.conf.urls import url 
from dailyfortune import views

urlpatterns = [
        url(r'^$', views.HomePageView.as_view()),
        ]
