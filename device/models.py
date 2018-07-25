from django.db import models
from cauth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.utils.functional import cached_property


class Device(models.Model):
    serial_number = models.CharField('序列号', max_length=64, help_text='设备上贴的条码编号')
    device_model = models.CharField('机型', max_length=64)
    KIND_CHOICES = ((0, '手机'),
                    (1, '笔记本'),
                    (2, 'PC'),
                    (3, 'Pad')
                    )
    kind = models.IntegerField('种类', choices=KIND_CHOICES, default=0)
    version = models.CharField('版本', max_length=128, default='', blank=True)
    manufacturer = models.CharField('厂商', max_length=256, default='', blank=True)
    system = models.CharField('系统', max_length=64)
    owner = models.ForeignKey(User, related_name='owner', verbose_name='持有人', null=True, on_delete=SET_NULL)
    created_by = models.ForeignKey(User, verbose_name='创建人', null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = ((0, '草稿'),
                      (1, '正常'),
                      (2, '无效'),
                      )
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    resolution = models.CharField('分辨率', blank=True, max_length=128)
    comment = models.CharField('备注', default='', blank=True, max_length=256)

    class Meta:
        verbose_name = '设备'
        verbose_name_plural = '设备列表'

    @cached_property
    def name(self):
        return self.device_model + '_'+ self.serial_number
