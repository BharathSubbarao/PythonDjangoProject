# howdy/urls.py
from django.conf.urls import url
from howdy import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='homepage'),
    url(r'^about/$', views.AboutPageView.as_view(), name='aboutpage'), 
    url(r'^profile/$', views.MyProfileView, name='profilepage'), 
]

#https://scotch.io/tutorials/build-your-first-python-and-django-application
#https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html
