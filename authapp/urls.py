from django.conf.urls import url
import authapp.views as asuthapp


urlpatterns = [
    url(r'^$', asuthapp.index, name='index'),
    url(r'/login', asuthapp.login, name='lohin'),
]