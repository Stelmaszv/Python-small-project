from django.urls import path, include
from . import views
from rest_framework.authtoken import views as reset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list',views.ListView)

urlpatterns = [
    path('',include(router.urls)),
    path(r'^api-token-auth/', reset.obtain_auth_token)
]

