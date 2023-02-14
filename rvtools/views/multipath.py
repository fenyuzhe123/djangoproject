from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vMultiPath
        fields = '__all__'


def multipath(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vMultiPath.objects.filter(
            Q(DisplayName__contains=search_data) | Q(Host__contains=search_data) | Q(Policy__contains=search_data) |
            Q(Datastore__contains=search_data) | Q(Datacenter__contains=search_data) | Q(DisplayName__contains=search_data)
        )
    else:
        queryset = models.vMultiPath.objects.all()

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

#   print(queryset.count())
    return render(request, 'multipath.html', context)
