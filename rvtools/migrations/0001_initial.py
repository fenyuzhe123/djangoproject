# Generated by Django 4.0.6 on 2022-08-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.CreateModel(
            name='vHBA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(blank=True, max_length=64, null=True, verbose_name='Host')),
                ('datacenter', models.CharField(blank=True, max_length=64, null=True, verbose_name='Datacenter')),
                ('cluster', models.CharField(blank=True, max_length=64, null=True, verbose_name='Cluster')),
                ('device', models.CharField(blank=True, max_length=64, null=True, verbose_name='Device')),
                ('type', models.CharField(blank=True, max_length=64, null=True, verbose_name='Type')),
                ('status', models.CharField(blank=True, max_length=64, null=True, verbose_name='Status')),
                ('bus', models.IntegerField(blank=True, null=True, verbose_name='Bus')),
                ('pci', models.CharField(blank=True, max_length=64, null=True, verbose_name='Pci')),
                ('driver', models.CharField(blank=True, max_length=64, null=True, verbose_name='Driver')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Model')),
                ('wwn', models.CharField(blank=True, max_length=255, null=True, verbose_name='Wwn')),
                ('vi_sdk_server', models.CharField(blank=True, max_length=64, null=True, verbose_name='vCenter地址')),
                ('vi_sdk_uuid', models.CharField(blank=True, max_length=255, null=True, verbose_name='vCenter UUID')),
            ],
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vmname', models.CharField(blank=True, max_length=64, null=True, verbose_name='vmname')),
                ('powerstate', models.CharField(blank=True, max_length=64, null=True, verbose_name='powerstate')),
                ('template', models.CharField(blank=True, max_length=64, null=True, verbose_name='template')),
                ('srmplaceholder', models.CharField(blank=True, max_length=64, null=True, verbose_name='srmplaceholde')),
                ('configstatus', models.CharField(blank=True, max_length=64, null=True, verbose_name='configstatus')),
                ('guesthostname', models.CharField(blank=True, max_length=64, null=True, verbose_name='guesthostname')),
                ('connectionstate', models.CharField(blank=True, max_length=64, null=True, verbose_name='connectionstate')),
                ('gueststate', models.CharField(blank=True, max_length=64, null=True, verbose_name='gueststate')),
                ('heartbeat', models.CharField(blank=True, max_length=64, null=True, verbose_name='heartbeat')),
                ('consolidationneeded', models.CharField(blank=True, max_length=64, null=True, verbose_name='heartbeat')),
                ('boottime', models.CharField(blank=True, max_length=64, null=True, verbose_name='boottime')),
                ('suspendtime', models.CharField(blank=True, max_length=64, null=True, verbose_name='suspendtime')),
                ('createdate', models.CharField(blank=True, max_length=64, null=True, verbose_name='createdate')),
                ('changeversion', models.CharField(blank=True, max_length=64, null=True, verbose_name='changeversion')),
                ('cpus', models.CharField(blank=True, max_length=64, null=True, verbose_name='cpus')),
                ('memory', models.CharField(blank=True, max_length=64, null=True, verbose_name='memory')),
                ('nics', models.CharField(blank=True, max_length=64, null=True, verbose_name='nics')),
                ('virtualdisks', models.CharField(blank=True, max_length=64, null=True, verbose_name='virtualdisks')),
                ('requiredevcmodekey', models.CharField(blank=True, max_length=64, null=True, verbose_name='requiredevcmodekey')),
                ('latencysensitivity', models.CharField(blank=True, max_length=64, null=True, verbose_name='latencysensitivity')),
                ('enableuuid', models.CharField(blank=True, max_length=64, null=True, verbose_name='enableuuid')),
                ('cbt', models.CharField(blank=True, max_length=64, null=True, verbose_name='cbt')),
                ('primaryip', models.CharField(blank=True, max_length=64, null=True, verbose_name='primaryip')),
                ('network1', models.CharField(blank=True, max_length=64, null=True, verbose_name='network1')),
                ('network2', models.CharField(blank=True, max_length=64, null=True, verbose_name='network2')),
                ('network3', models.CharField(blank=True, max_length=64, null=True, verbose_name='network3')),
                ('network4', models.CharField(blank=True, max_length=64, null=True, verbose_name='network4')),
                ('network5', models.CharField(blank=True, max_length=64, null=True, verbose_name='network5')),
                ('network6', models.CharField(blank=True, max_length=64, null=True, verbose_name='network6')),
                ('network7', models.CharField(blank=True, max_length=64, null=True, verbose_name='network7')),
                ('network8', models.CharField(blank=True, max_length=64, null=True, verbose_name='network8')),
                ('numdisplay', models.CharField(blank=True, max_length=64, null=True, verbose_name='network8')),
                ('videoram', models.CharField(blank=True, max_length=64, null=True, verbose_name='videoram')),
                ('resourcepool', models.CharField(blank=True, max_length=64, null=True, verbose_name='resourcepool')),
                ('folder', models.CharField(blank=True, max_length=64, null=True, verbose_name='folder')),
                ('vapp', models.CharField(blank=True, max_length=64, null=True, verbose_name='vapp')),
                ('dasprotection', models.CharField(blank=True, max_length=64, null=True, verbose_name='dasprotection')),
                ('ftstate', models.CharField(blank=True, max_length=64, null=True, verbose_name='ftstate')),
                ('ftlatencystatus', models.CharField(blank=True, max_length=64, null=True, verbose_name='ftlatencystatus')),
                ('ftbandwidth', models.CharField(blank=True, max_length=64, null=True, verbose_name='ftbandwidth')),
                ('ftsecondarylatency', models.CharField(blank=True, max_length=64, null=True, verbose_name='ftsecondarylatency')),
                ('provisioned', models.CharField(blank=True, max_length=64, null=True, verbose_name='provisioned')),
                ('inuse', models.CharField(blank=True, max_length=64, null=True, verbose_name='inuse')),
                ('unshared', models.CharField(blank=True, max_length=64, null=True, verbose_name='unshared')),
                ('harestartpriority', models.CharField(blank=True, max_length=64, null=True, verbose_name='harestartpriority')),
                ('haisolatinresponse', models.CharField(blank=True, max_length=64, null=True, verbose_name='haisolatinresponse')),
                ('vmmonitoring', models.CharField(blank=True, max_length=64, null=True, verbose_name='vmmonitoring')),
                ('clusterrule', models.CharField(blank=True, max_length=64, null=True, verbose_name='clusterrule')),
                ('clusterrulename', models.CharField(blank=True, max_length=64, null=True, verbose_name='clusterrulename')),
                ('installbootrequired', models.CharField(blank=True, max_length=64, null=True, verbose_name='installbootrequired')),
                ('bootdelay', models.CharField(blank=True, max_length=64, null=True, verbose_name='bootdelay')),
                ('bootretrydelay', models.CharField(blank=True, max_length=64, null=True, verbose_name='bootretrydelay')),
                ('bootretryenabled', models.CharField(blank=True, max_length=64, null=True, verbose_name='bootretryenabled')),
                ('bootbios', models.CharField(blank=True, max_length=64, null=True, verbose_name='bootretrydelay')),
                ('firmware', models.CharField(blank=True, max_length=64, null=True, verbose_name='firmware')),
                ('hwversion', models.CharField(blank=True, max_length=64, null=True, verbose_name='hwversion')),
                ('hwupgradestatus', models.CharField(blank=True, max_length=64, null=True, verbose_name='hwupgradestatus')),
                ('hwupgradepolicy', models.CharField(blank=True, max_length=64, null=True, verbose_name='hwupgradestatus')),
                ('hwtarget', models.CharField(blank=True, max_length=64, null=True, verbose_name='hwtarget')),
                ('path', models.CharField(blank=True, max_length=256, null=True, verbose_name='path')),
                ('logdir', models.CharField(blank=True, max_length=256, null=True, verbose_name='logdir')),
                ('snapshotdir', models.CharField(blank=True, max_length=256, null=True, verbose_name='snapshotdir')),
                ('suspenddir', models.CharField(blank=True, max_length=256, null=True, verbose_name='suspenddir')),
                ('notes', models.CharField(blank=True, max_length=512, null=True, verbose_name='notes')),
                ('datacenter', models.CharField(blank=True, max_length=64, null=True, verbose_name='datacenter')),
                ('cluster', models.CharField(blank=True, max_length=64, null=True, verbose_name='cluster')),
                ('host', models.CharField(blank=True, max_length=64, null=True, verbose_name='host')),
                ('os', models.CharField(blank=True, max_length=64, null=True, verbose_name='os')),
                ('ostools', models.CharField(blank=True, max_length=64, null=True, verbose_name='ostools')),
                ('objectid', models.CharField(blank=True, max_length=64, null=True, verbose_name='objectid')),
                ('uuid', models.CharField(blank=True, max_length=64, null=True, verbose_name='uuid')),
                ('visdkservertype', models.CharField(blank=True, max_length=64, null=True, verbose_name='visdkservertype')),
                ('visdkapi', models.CharField(blank=True, max_length=64, null=True, verbose_name='visdkapi')),
                ('vmtag', models.CharField(blank=True, max_length=64, null=True, verbose_name='vmtag')),
                ('vcenter', models.CharField(blank=True, max_length=64, null=True, verbose_name='vcenter')),
                ('vcenteruuid', models.CharField(blank=True, max_length=64, null=True, verbose_name='vcenteruuid')),
            ],
        ),
    ]
