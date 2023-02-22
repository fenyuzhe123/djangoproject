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
    dvswitch, dvport, vsc_vmk, vhealth, vtools, vsnapshot, vcpu, vmemory, vpartition, vnetwork, vcd, vdisk,download,\
    fnic, enic


urlpatterns = [
    path('download-excel/', download.download_excel, name='download_excel'),
    path('admin/', admin.site.urls),
    path('', login.login),
    path('hba/', hba.hba, name='hba'),
    path('hba-export-csv/', hba.export_csv, name='hba-export-csv'),
    path('login/', login.login),
    path('logout/', login.logout, name='logout'),
    path('vm/', vm.vm, name='vm'),
    path('vm-export-csv/', vm.export_csv, name='vm-export-csv'),
    path('cluster/', cluster.cluster, name='cluster'),
    path('cluster-export-csv/', cluster.export_csv, name='cluster-export-csv'),
    path('host/', host.host, name='host'),
    path('host-export-csv/', host.export_csv, name='host-export-csv'),
    path('nic/', nic.nic, name='nic'),
    path('nic-export-csv/', nic.export_csv, name='nic-export-csv'),
    path('datastore/', datastore.datastore, name='datastore'),
    path('datastore-export-csv/', datastore.export_csv, name='datastore-export-csv'),
    path('multipath/', multipath.multipath, name='multipath'),
    path('multipath-export-csv/', multipath.export_csv, name='multipath-export-csv'),
    path('vswitch/', vswitch.vswitch, name='vswitch'),
    path('vswitch-export-csv/', vswitch.export_csv, name='vswitch-export-csv'),
    path('vport/', vport.vport, name='vport'),
    path('vport-export-csv/', vport.export_csv, name='vport-export-csv'),
    path('dvswitch/', dvswitch.dvswitch, name='dvswitch'),
    path('dvswitch-export-csv/', dvswitch.export_csv, name='dvswitch-export-csv'),
    path('dvport/', dvport.dvport, name='dvport'),
    path('ddvport/-export-csv/', dvport.export_csv, name='dvport-export-csv'),
    path('vsc_vmk/', vsc_vmk.vsc_vmk, name='vsc_vmk'),
    path('vsc_vmk-export-csv/', vsc_vmk.export_csv, name='vsc_vmk-export-csv'),
    path('zombie/', vhealth.zombie, name='zombie'),
    path('vmstorage/', vhealth.vmstorage, name='vmstorage'),
    path('foldername/', vhealth.foldername, name='foldername'),
    path('toolsissue/', vhealth.toolsissue, name='toolsissue'),
    path('snapshot/', vhealth.snapshot, name='snapshot'),
    path('performance/', vhealth.performance, name='performance'),
    path('cdrom/', vhealth.cdrom, name='cdrom'),
    path('usb/', vhealth.usb, name='usb'),
    path('vhealth-export-csv/', vhealth.export_csv, name='vhealth-export-csv'),
    path('vtools/', vtools.vtools, name='vtools'),
    path('vtools-export-csv/', vtools.export_csv, name='vtools-export-csv'),
    path('vsnapshot/', vsnapshot.vsnapshot, name='vsnapshot'),
    path('vsnapshot-export-csv/', vsnapshot.export_csv, name='vsnapshot-export-csv'),
    path('vcpu/', vcpu.vcpu, name='vcpu'),
    path('vcpu-export-csv/', vcpu.export_csv, name='vcpu-export-csv'),
    path('vmemory/', vmemory.vmemory, name='vmemory'),
    path('vmemory-export-csv/', vmemory.export_csv, name='vmemory-export-csv'),
    path('vpartition/', vpartition.vpartition, name='vpartition'),
    path('vpartition-export-csv/', vpartition.export_csv, name='vpartition-export-csv'),
    path('vnetwork/', vnetwork.vnetwork, name='vnetwork'),
    path('vnetwork-export-csv/', vnetwork.export_csv, name='vnetwork-export-csv'),
    path('vcd/', vcd.vcd, name='vcd'),
    path('vcd-export-csv/', vcd.export_csv, name='vcd-export-csv'),
    path('vdisk/', vdisk.vdisk, name='vdisk'),
    path('vdisk-export-csv/', vdisk.export_csv, name='vdisk-export-csv'),
    path('fnic/', fnic.fnic, name='fnic'),
    path('fnic-export-csv/', fnic.export_csv, name='fnic-export-csv'),
    path('enic/', enic.enic, name='enic'),
    path('enic-export-csv/', fnic.export_csv, name='enic-export-csv')

]
