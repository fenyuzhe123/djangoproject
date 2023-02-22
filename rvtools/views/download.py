import os
import datetime
from django.http import HttpResponse
from django.conf import settings

def download_excel(request):
    # 获取要下载的 Excel 文件的路径
    file_path = os.path.join(settings.MEDIA_ROOT, 'excel_files', 'finaldata.xlsx')
    print(file_path)
  #  file_path = r"E:\code\djangoProject\rvtools\media\excel_files\finaldata.xlsx"
    # 读取文件内容
    with open(file_path, 'rb') as excel_file:
        file_data = excel_file.read()
    # 构建 HTTP 响应对象
    response = HttpResponse(file_data, content_type='application/vnd.ms-excel')

    # 获取当前系统时间
    now = datetime.datetime.now()

    # 设置响应头，指定文件名和下载方式
    response['Content-Disposition'] = 'attachment; filename="inventory_{}.xlsx"'.format(now.strftime('%Y%m%d_%H%M'))
    return response