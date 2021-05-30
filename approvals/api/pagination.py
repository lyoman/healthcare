from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class ApprovalLimitOffSetPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10

class ApprovalPageNumberPagination(PageNumberPagination):
    page_size = 10