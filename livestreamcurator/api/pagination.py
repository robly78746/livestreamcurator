from rest_framework import pagination


class PaginationById(pagination.CursorPagination):
    ordering = 'id'