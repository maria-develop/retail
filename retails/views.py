from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from .models import Retail, Product
from .serializers import RetailSerializer, ProductSerializer
from .paginations import RetailPageNumberPagination, ProductPageNumberPagination


class RetailListAPIView(ListAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer
    pagination_class = RetailPageNumberPagination
    filter_backends = [DjangoFilterBackend]  # Подключаем фильтрацию
    filterset_fields = ['country']  # Указываем поле для фильтрации


class RetailRetrieveAPIView(RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer


class RetailCreateAPIView(CreateAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class RetailDestroyAPIView(DestroyAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class RetailUpdateAPIView(UpdateAPIView):
    serializer_class = RetailSerializer
    queryset = Retail.objects.all()


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPageNumberPagination


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
