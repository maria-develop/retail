from django.urls import path

from retails.apps import RetailsConfig
from retails.views import (
    RetailListAPIView, RetailRetrieveAPIView, RetailCreateAPIView, RetailDestroyAPIView, RetailUpdateAPIView,
    ProductListAPIView, ProductRetrieveAPIView, ProductCreateAPIView, ProductDestroyAPIView, ProductUpdateAPIView,
)

app_name = RetailsConfig.name

urlpatterns = [
    path("", RetailListAPIView.as_view(), name="retail_list"),
    path("<int:pk>/", RetailRetrieveAPIView.as_view(), name="retail_retrieve"),
    path("create/", RetailCreateAPIView.as_view(), name="retail_create"),
    path("<int:pk>/update/", RetailUpdateAPIView.as_view(), name="retail_update"),
    path("<int:pk>/delete/", RetailDestroyAPIView.as_view(), name="retail_delete"),

    path("p/", ProductListAPIView.as_view(), name="product_list"),
    path("p/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"),
    path("p/create/", ProductCreateAPIView.as_view(), name="product_create"),
    path("p/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product_update"),
    path("p/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product_delete"),
]
