from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
from django.db.models import Q
from rvtools.utils.pagination import Pagination


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