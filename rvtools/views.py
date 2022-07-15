from django.shortcuts import render, HttpResponse
from django import forms
from . import models
from django.db.models import Q
from django.utils.safestring import mark_safe
import copy

# Create your views here.
class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vHBA
        fields = '__all__'


def dash(request):
    queryset = models.vHBA.objects.all()
    return render(request, "test.html", {"queryset": queryset})


def index(request):
    # data_dict = {}


    # 1.根据用户想要访问的页码，计算出起止位置
    page = int(request.GET.get('page', 1))
    page_size = 20  # 每页显示30条数据
    start = (page - 1) * page_size
    end = page * page_size

    # 数据总条数
    # total_count = models.vHBA.objects.filter(
    #     Q(wwn__contains=search_data) | Q(driver__contains=search_data) | Q(host__contains=search_data) | Q(model__contains=search_data)).order_by("host").count()

    total_count = models.vHBA.objects.all().count()
    # 总页码
    total_page_count, div = divmod(total_count, page_size)
    if div:
        total_page_count += 1

    # 计算出显示当前的前5页，后5页
    plus = 5
    if total_page_count <= 2 * plus + 1:
        # 数据库中的数据比较少，没有达到11页
        start_page = 1
        end_page = total_page_count
    else:
        # 数据库中的数据大于11页

        # 当前页小于5(小极值)
        if page <= plus:
            start_page = 1
            end_page = 2 * plus + 1
        else:
            # 当前页>5
            # 当前页+5 > 总页数
            if (page + plus) > total_page_count:
                start_page = total_page_count - 2 * plus
                end_page = total_page_count
            else:
                start_page = page - plus
                end_page = page + plus

    # 页码
    page_str_list = []
    # 首页
    page_str_list.append('<li><a href="?page={}">首页</a></li>'.format(1))
    # 上一页
    if page > 1:
        prev_page = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    else:
        prev_page = '<li><a href="?page={}">上一页</a></li>'.format(1)
    page_str_list.append(prev_page)
    # 页面
    for i in range(start_page, end_page + 1):
        if i == page:
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)

    # 下一页
    if page < total_page_count:
        next_page = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    else:
        next_page = '<li><a href="?page={}">下一页</a></li>'.format(total_page_count)
    page_str_list.append(next_page)

    # 尾页
    page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))
    page_string = mark_safe("".join(page_str_list))


    search_data = request.GET.get('q', "")
    if search_data:
        result = models.vHBA.objects.filter(
             Q(wwn__contains=search_data) | Q(driver__contains=search_data) | Q(host__contains=search_data) | Q(model__contains=search_data))[start_page: end_page]
    else:
        result = models.vHBA.objects.all()[start: end]
    print(search_data)
    return render(request, 'servers_list.html', {"result": result, "search_data": search_data, "page_string": page_string})
