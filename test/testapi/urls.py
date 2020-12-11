from django.urls import path
from .views import shop_list, shop_detail


urlpatterns = [
    path('shop/', shop_list),
    path('shop/<int:pk>/', shop_detail, name='shop_pk')
]
