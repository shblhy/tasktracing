import datetime
from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.deletion import CASCADE, SET_DEFAULT, SET_NULL
from django.utils.functional import cached_property
from jsonfield import JSONField
from item.models import Item
from cauth.models import User


class Task(models.Model):
    item = models.ForeignKey(Item, verbose_name='项目', null=True, on_delete=CASCADE)
    test_case = JSONField('测试用例', max_length=2560, blank=True, null=True)
    start_time = models.DateField('开始时间')
    end_time = models.DateField('结束时间')
    commit = models.TextField('重点说明', default='', blank=True, help_text='测试重点和其它要求')
    verify_ready_time = models.DateTimeField('可审核时间', null=True)
    verifier = models.ForeignKey(User, related_name='verifier', verbose_name='审核人', null=True, on_delete=SET_NULL)
    verify_time = models.DateTimeField('审核时间', null=True)
    allocate_time = models.DateTimeField('分配时间', null=True)
    executor_ids = models.CharField(validators=[validate_comma_separated_integer_list], null=True, blank=True, max_length=256)
    created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = ((0, '草稿'),
                   (1, '待审核'),
                   (2, '待分配'),
                   (3, '待执行'),
                   (4, '执行中'),
                   (5, '结果确认中'),
                   (6, '已完成'),
                   (8, '审核失败'),
                   (9, '已作废'),
                   )
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=0)

    class Meta:
        db_table = 'test_task'
        verbose_name = '测试任务'
        verbose_name_plural = '测试任务列表'

    @property
    def name(self):
        return self.item.name + '_' + str(self.id)

    @cached_property
    def executors(self):
        if self.executor_ids:
            return User.objects.filter(id__in=self.executor_ids.split(','))
        else:
            return []

    def verify(self, user):
        self.status = 2
        self.verifier = user
        self.verify_time = datetime.datetime.now()
        self.save()
        return 'success'

    def can_verify(self):
        return self.status in [0, 1] and self.verify_condition_ready()

    def verify_condition_ready(self):
        device_ready = (self.apply_device == 1 and self.custom_devices) or self.apply_device == 0
        now_time = datetime.datetime.now()
        time_ready = self.start_time > now_time and self.end_time > now_time
        return self.workload and device_ready and time_ready

    def add_executors(self, executor_ids):
        executor_ids_list = self.executor_ids.split(',') if self.executor_ids else []
        executor_ids_list.extend([str(e) for e in executor_ids])
        self.executor_ids = ','.join(executor_ids_list)
        self.save()

    def delete_executors(self, executor_ids):
        executor_ids_list = self.executor_ids.split(',') if self.executor_ids else []
        for executor_id in executor_ids:
            executor_ids_list.remove(str(executor_id))
        self.executor_ids = ','.join(executor_ids_list)
        self.save()

    def allocate(self):
        self.status = 4
        self.allocate_time = datetime.datetime.now()
        self.save()

    def finish(self):
        self.status = 6
        self.save()