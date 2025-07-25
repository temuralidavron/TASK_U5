from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):

    page_size = 2  # Har bir sahifada 10 ta element

    page_size_query_param = 'page_size'

    max_page_size = 100  # Maksimal sahifa o'lchami