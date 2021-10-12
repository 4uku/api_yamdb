from django.urls import include, path

from rest_framework import routers

from . import views
from .views import MeViewSet, UserViewSet, create_and_get_code, get_token

router = routers.DefaultRouter()
#router.register(r'^users\/me$', MeViewSet, basename='me')
#router.register(r'users/me$', MeViewSet, basename='me')
router.register('users', UserViewSet, basename='userviewset')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews',
    views.ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>[^/.]+)/reviews/(?P<review_id>[^/.]+)/comments',
    views.CommentViewSet,
    basename='comments')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'genres', views.GenreViewSet, basename='genres')
router.register(r'titles', views.TitleViewSet, basename='titles')



class CustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(
            url=r'',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            initkwargs={},
            detail=False
        )
    ]

custom_router = CustomRouter()
custom_router.register('', MeViewSet)


urlpatterns = [
    path('v1/auth/signup/', create_and_get_code, name='create_and_get_code'),
    path('v1/auth/token/', get_token, name='get_token'),
    #path('v1/users/me/', APIMe.as_view(), name='apime'),
    path('v1/users/me', include(custom_router.urls)),
    path('v1/', include(router.urls)),
]