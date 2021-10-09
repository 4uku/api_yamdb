from django.urls import include, path

from rest_framework import routers

from .views import APIMe, UserViewSet, create_and_get_code, get_token
from . import views

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='userviewset')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews',
    views.ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/auth/signup/', create_and_get_code, name='create_and_get_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/users/me/', APIMe.as_view(), name='apime'),
    path('v1/', include(router.urls)),
]
