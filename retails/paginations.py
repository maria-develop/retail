from rest_framework.pagination import PageNumberPagination


class RetailPageNumberPagination(PageNumberPagination):
    """Список задач выводится по 10 единиц"""
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class ProductPageNumberPagination(PageNumberPagination):
    """Список задач выводится по 30 единиц"""
    page_size = 30
    page_size_query_param = "page_size"
    max_page_size = 150
