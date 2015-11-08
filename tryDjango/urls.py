"""tryDjango URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from tryDjango import settings

from closets import views as closet_views
from user import views as user_views
from django.contrib.auth import views as views
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home$', closet_views.ClosetView.as_view(), name='home'),
    url(r'^about/$', 'profiles.views.about', name='about'),
	url(r'^contact/$','contact.views.contact', name='contact'),
	url(r'^login/$', views.login, name="login"),
	url(r'^register', user_views.AddUserView.as_view(), name='user_register'),
	url(r'^logout', views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^user/', include('user.urls')),
    url(r'^mycloset/(?P<user_id>\d+)/$', closet_views.UserClosetView.as_view(), name="my_closet"),
    url(r'^upload/', closet_views.ItemImageView.as_view(), name='item_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', closet_views.ItemDetailView.as_view(), name='item_image'),
    url(r'^new/$', closet_views.ItemCreate.as_view(), name='add_item'),
    url(r'^show_item/(?P<item_id>\d+)/$', closet_views.ItemDetailView.as_view(), name='show_item'),
    url(r'^(?P<user_id>\d+)$', user_views.show_user, name='show_user'),
    url(r'^(?P<user_id>\d+)/follow/$', user_views.follow_user,
        name="follow_user"),
    




]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
