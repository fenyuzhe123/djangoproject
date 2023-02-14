"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rvtools.views import hba, login, vm, cluster, host, nic, datastore, multipath, vswitch, vport,\
    dvswitch, dvport, vsc_vmk, vhealth, vtools


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hba/', hba.hba, name='hba'),
    path('login/', login.login),
    path('logout/', login.logout, name='logout'),
    path('vm/', vm.vm, name='vm'),
    path('cluster/', cluster.cluster, name='cluster'),
    path('host/', host.host, name='host'),
    path('nic/', nic.nic, name='nic'),
    path('datastore/', datastore.datastore, name='datastore'),
    path('multipath/', multipath.multipath, name='multipath'),
    path('vswitch/', vswitch.vswitch, name='vswitch'),
    path('vport/', vport.vport, name='vport'),
    path('dvswitch/', dvswitch.dvswitch, name='dvswitch'),
    path('dvport/', dvport.dvport, name='dvport'),
    path('vsc_vmk/', vsc_vmk.vsc_vmk, name='vsc_vmk'),
    path('zombie/', vhealth.zombie, name='zombie'),
    path('vmstorage/', vhealth.vmstorage, name='vmstorage'),
    path('foldername/', vhealth.foldername, name='foldername'),
    path('toolsissue/', vhealth.toolsissue, name='toolsissue'),
    path('snapshot/', vhealth.snapshot, name='snapshot'),
    path('performance/', vhealth.performance, name='performance'),
    path('cdrom/', vhealth.cdrom, name='cdrom'),
    path('usb/', vhealth.usb, name='usb'),
    path('vtools/', vtools.vtools, name='vtools')
]
