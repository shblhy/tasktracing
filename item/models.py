from django.db import models
from cauth.models import User
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL


class Item(models.Model):
    name = models.CharField('名称', max_length=256)
    desc = models.TextField('描述')
    STATUS_CHOICES = ((0, '草稿'),
                      (1, '正常'),
                      (2, '关闭'),
                      )
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=1)
    created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    weight = models.IntegerField(default=0)
    comment = models.CharField('备注', default='', blank=True, max_length=256)
    users = models.ManyToManyField(User, related_name='item_user')

    class Meta:
        db_table = 'task_item'
        verbose_name = '项目'
        verbose_name_plural = '项目列表'
        ordering = ['-weight']

    def __unicode__(self):
        return self.name