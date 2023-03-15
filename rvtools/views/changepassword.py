from django.shortcuts import render
from django.contrib import messages
import re

from rvtools.models import Admin


def changepassword(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        admin = Admin.objects.get(username='admin')

        if current_password == admin.password:
            if new_password == confirm_password:
                if is_valid_password(new_password):
                    admin.password = new_password
                    admin.save()

                    messages.success(request, '修改成功')

                else:
                    messages.error(request, '新密码必须包含数字和字母且不少于8位')
            else:
                messages.error(request, '两次输入的新密码不一致')
        else:
            messages.error(request, '当前密码错误')

    return render(request, 'changepassword.html')





def is_valid_password(password):
    # 验证密码是否至少8位字符，并且包含数字和字母
    if len(password) < 8 or not re.search(r'\d', password) or not re.search(r'[a-zA-Z]', password):
        return False
    # 验证密码是否包含特殊字符（可选）
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return True
    # 如果没有特殊字符，则返回False
    return False
