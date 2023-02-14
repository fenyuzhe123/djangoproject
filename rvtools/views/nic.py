from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vNIC
        fields = '__all__'


def nic(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vNIC.objects.filter(
            Q(Host__contains=search_data) | Q(Cluster__contains=search_data) | Q(NetworkDevice__contains=search_data) |
            Q(Driver__contains=search_data) | Q(MAC__contains=search_data))
    else:
        queryset = models.vNIC.objects.all()

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

    # print(queryset.count())
    return render(request, 'nic.html', context)
