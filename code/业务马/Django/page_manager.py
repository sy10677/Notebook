from django.core.paginator import Paginator

class PageManager(object):
    """docstring for PageManager."""

    def __init__(self, arr, pages, request, pagparm='page'):
        self.pagparm = pagparm
        self.request = request
        self.pgnator = Paginator(arr, pages)

    def current_page(self):
        return int(self.request.GET.get(self.pagparm, 1))

    def current_page_list(self):
        return self.pgnator.get_page(self.current_page).object_list

    def total_pages(self):
        return p.num_pages
