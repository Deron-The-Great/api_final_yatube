from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet


router_vol1 = routers.DefaultRouter()
router_vol1.register('posts', PostViewSet, basename='posts')
router_vol1.register('groups', GroupViewSet, basename='groups')
router_vol1.register(
    r'^posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_vol1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_vol1.urls)),
]
