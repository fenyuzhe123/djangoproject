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
        model = models.vHealth
        fields = '__all__'


def zombie(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='Zombie') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="Zombie")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'zombie.html', context)


def vmstorage(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='Storage') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="Storage")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'vmstorage.html', context)


def foldername(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='Foldername') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="Foldername")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'foldername.html', context)


def toolsissue(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='VM Tools') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="VM Tools")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'toolsissue.html', context)


def snapshot(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='Snapshot') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="Snapshot")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'snapshot.html', context)


def performance(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='Performance tip') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="Performance tip")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'performance.html', context)


def cdrom(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='CDROM') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="CDROM")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'cdrom.html', context)


def usb(request):
    search_data = request.GET.get('q', "")

    if search_data:
        queryset = models.vHealth.objects.filter(Q(MessageType='USB') &
                                                 (Q(Name__contains=search_data) | Q(Message__contains=search_data) | Q(
                                                     vcenter__contains=search_data)))
    else:
        queryset = models.vHealth.objects.filter(MessageType="USB")

    page_object = Pagination(request, queryset)
    total = queryset.count()
    context = {
        # "search_data": search_data,
        "total": total,  # 返回总条目数
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成的页码
    }
    return render(request, 'usb.html', context)


def export_csv(request):
    # 定义要导出的表格名称
    table_name = "rvtools_vhealth"
    # 查询要导出的表格数据
    with connections['default'].cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()

    # 定义响应的文件名
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="health-list.csv"'

    # 设置CSV编码为UTF-8
    response.write(u'\ufeff'.encode('utf8'))

    # 将数据写入响应
    writer = csv.writer(response)

    # 添加表头
    writer.writerow([i[0] for i in cursor.description])
    for row in data:
        writer.writerow(row)

    return response