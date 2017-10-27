# coding=utf-8
from django.conf.urls import url, include
from django_angular.views import IndexView
from rest_framework_mongoengine import routers
from mongo_auth import urls as mongo_auth_urls
from authentication.views import UsersView
from posts.views import PostsView
from analytic.views import CustomersViewSet,OrdersViewSet

router = routers.SimpleRouter()
router.register(r'users', UsersView, base_name='post')
router.register(r'posts', PostsView, base_name='post')
router.register(r'customers', CustomersViewSet, r"customers")
router.register(r'orders', OrdersViewSet, r"orders")

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include(mongo_auth_urls)),
    url(r'^scrumboard/', include('scrumboard.urls')),
    url('^.*$', IndexView.as_view(), name='index'),
]
