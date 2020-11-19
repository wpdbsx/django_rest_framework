from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post' ,views.PostViewSet) # 2개의URL을 만들어줍니다.
# router.urls
urlpatterns = [
    path('',include(router.urls)),
    path('public/',views.public_post_list),
    
]
