from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50, verbose_name='设备名称')
    sn = models.CharField(max_length=50, verbose_name='设备序列号', primary_key=True)
    ip = models.CharField(max_length=50, verbose_name='设备IP')
    netmask = models.CharField(max_length=50, verbose_name='子网掩码')
    netgate = models.CharField(max_length=50, verbose_name='网关')
    mac = models.CharField(max_length=50, verbose_name='MAC')
    ver = models.CharField(max_length=50, verbose_name='硬件版本', default='')
    #ver_date = models.DateTimeField(verbose_name='硬件版本时间', default='')

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
