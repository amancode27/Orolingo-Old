from django.contrib import admin
from .import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'users'

urlpatterns = [
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', views.logout_user, name='logout_user'),
    url(r'^register/$', views.register, name='register'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    # url(r'^register/email_authen/$', views.email_authen, name='email_authen'),
    # url(r'^register/create-profile/$', views.create_profile, name='create_profile'),
    # url(r'^register/dob_authen/$', views.dob_authen, name='dob_authen'),
    #url(r'^create-profile/$', views.create_profile, name='create_profile'),
    #url(r'^forgot/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.pass_reset, name='forgot'),


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
