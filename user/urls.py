"""urly_bird URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from user import views as user_views
from django.contrib.auth import views

urlpatterns = [
    # url(r'^register/$', user_views.AddUserView.as_view(), name="user_register"),
    # url(r'^user/(?P<user_id>\d+)$', user_views.ShowUserDetailView.as_view(), name="show_user"),
    # url(r'^login/$', views.login, {'template_name': 'home.html'}, name="login"),
    # url(r'^logout/$', views.logout,{'template_name': 'home.html'}, name='logout'),
    # url(r'^user/edit_profile/', user_views.edit_profile, name="edit_profile"),
]

