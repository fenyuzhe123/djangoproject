from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination
import csv
from django.http import HttpResponse
from django.db import connections


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


def export_csv(request):
    # 定义要导出的表格名称
    table_name = "rvtools_vtools"
    # 查询要导出的表格数据
    with connections['default'].cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()

    # 定义响应的文件名
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="VMwareTools-list.csv"'

    # 设置CSV编码为UTF-8
    response.write(u'\ufeff'.encode('utf8'))

    # 将数据写入响应
    writer = csv.writer(response)

    # 添加表头
    writer.writerow([i[0] for i in cursor.description])
    for row in data:
        writer.writerow(row)

    return response