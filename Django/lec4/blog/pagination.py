from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
import math

class BlogPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allows clients to set page size
    max_page_size = 25  # Prevents excessively large pages

    def get_paginated_response(self, data):
        # account for the query parameter
        page_size_mod = self.request.query_params.get('page_size')
        
        if page_size_mod and page_size_mod.isdigit():
            self.page_size = int(page_size_mod)

        # Calculate total pages - total items divided by page size
        # If there are any remaining items, add an extra page
        total_pages = math.ceil(self.page.paginator.count / self.page_size)
        return Response({
            "total_results": self.page.paginator.count,  # Total items
            "total_pages": total_pages,  # Total pages
            "current_page": self.page.number,  # Current page number
            "results_per_page": self.page_size,  # Page size
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data  # Actual results
        })