from django.db import models


# Create your models here.
# vHBA sheet
class vHBA(models.Model):
    host = models.CharField(verbose_name='Host', max_length=64, blank=True, null=True)
    datacenter = models.CharField(verbose_name='Datacenter', max_length=64, blank=True, null=True)
    cluster = models.CharField(verbose_name='Cluster', max_length=64, blank=True, null=True)
    device = models.CharField(verbose_name='Device', max_length=64, blank=True, null=True)
    type = models.CharField(verbose_name='Type', max_length=64, blank=True, null=True)
    status = models.CharField(verbose_name='Status', max_length=64, blank=True, null=True)
    bus = models.IntegerField(verbose_name='Bus', blank=True, null=True)
    pci = models.CharField(verbose_name='Pci', max_length=64, blank=True, null=True)
    driver = models.CharField(verbose_name='Driver', max_length=64, blank=True, null=True)
    model = models.CharField(verbose_name='Model', max_length=255, blank=True, null=True)
    wwn = models.CharField(verbose_name='Wwn', max_length=255, blank=True, null=True)
    vi_sdk_server = models.CharField(verbose_name='vCenter地址', max_length=64, blank=True, null=True)
    vi_sdk_uuid = models.CharField(verbose_name='vCenter UUID', max_length=255, blank=True, null=True)
