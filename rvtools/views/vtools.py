from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vTools
        fields = '__all__'


def vtools(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vTools.objects.filter(
            Q(VM__contains=search_data) | Q(Powerstate__contains=search_data) | Q(Template__contains=search_data) |
            Q(VMVersion__contains=search_data) | Q(Tools__contains=search_data) | Q(ToolsVersion__contains=search_data) |
            Q(Upgradeable__contains=search_data) | Q(vcenter__contains=search_data))
    else:
        queryset = models.vTools.objects.all()

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        "search_data": search_data,
        "total": total,  # 返回总条目数nic.pynic.py
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

#   print(queryset)
    return render(request, 'vtools.html', context)
