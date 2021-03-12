from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class PatientLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class PatientPageNumberPagination(PageNumberPagination):
    page_size = 10