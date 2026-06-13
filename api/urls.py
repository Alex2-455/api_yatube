from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='posts')
router.register(r'groups', views.GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', token_views.obtain_auth_token),
    path('v1/', include(router.urls)),
    # Маршруты для комментариев через re_path
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/$',
        views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post-comments-list'
    ),
    re_path(
        r'^v1/posts/(?P<post_id>\d+)/comments/(?P<pk>\d+)/$',
        views.CommentViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'patch': 'partial_update',
                'delete': 'destroy'
            }
        ),
        name='post-comments-detail'
    ),
]
