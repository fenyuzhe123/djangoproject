from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.dvSwitch
        fields = '__all__'


def dvswitch(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.dvSwitch.objects.filter(
            Q(Switch__contains=search_data) | Q(Version__contains=search_data) | Q(HostMembers__contains=search_data) |
            Q(MaxMTU__contains=search_data) | Q(vcenter__contains=search_data))
    else:
        queryset = models.dvSwitch.objects.all()

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

    # print(queryset.count())
    return render(request, 'dvswitch.html', context)
