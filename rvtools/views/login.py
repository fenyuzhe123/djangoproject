from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django import forms
from .. import models
import datetime


# 用户登录函数
class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"}),
        required=True
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"}),
        required=True
    )


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 去数据库校验用户名和密码，错误的话返回为NULL
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # 增加TAM到期时间判断，如果离设定的到期时间小于30天，则提示告警不予登录
        current_date = datetime.date.today()
        fixed_date = datetime.date(2024, 6, 1)  # 将此处替换为TAM到期日期
        date_diff = (fixed_date - current_date).days
        if date_diff <= 30:
            form.add_error("password", "您的TAM合同即将到期，请续约后联系TAM激活登录！")
            return render(request, 'login.html', {'form': form})

    # 用户名和密码正确，网站生产随机字符串，写入用户浏览器cookies中，再写入session中
        request.session["info"] = admin_object.username
        return redirect('/vm/')

    return render(request, 'login.html', {'form': form})


def logout(request):
    """注销"""
    request.session.clear()
    return redirect('/login')