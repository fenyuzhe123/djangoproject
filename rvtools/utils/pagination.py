

class Pagination(object):

    def __int__(self, request, page_size=20, page_param="page"):
        page = request.GET.get(page_param, "1")
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        start = (page - 1) * page_size
        end = page * page_size



