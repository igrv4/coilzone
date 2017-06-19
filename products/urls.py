from django.conf.urls import url, include
from products import views


urlpatterns = [
    url(r'^products/', views.products, name='products'),
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product'),
]