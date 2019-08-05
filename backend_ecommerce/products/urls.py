from django.conf.urls import url

from .views import (
    ProductListView, 
    ProductDetailSlugView,
    recom
    )

urlpatterns = [
    url(r'^$', ProductListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
    url(r'^recom$', recom, name='recom'),
]