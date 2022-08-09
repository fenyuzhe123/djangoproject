from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vHBA
        fields = '__all__'


def hba(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHBA.objects.filter(
            Q(wwn__contains=search_data) | Q(driver__contains=search_data) | Q(host__contains=search_data) | Q(
                model__contains=search_data))
    else:
        queryset = models.vHBA.objects.all()

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }

    # print(queryset.count())
    return render(request, 'hba.html', context)
