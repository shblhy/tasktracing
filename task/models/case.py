from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE
from item.models import Item
from cauth.models import User


class Case(models.Model):
    item = models.ForeignKey(Item, verbose_name='项目', on_delete=CASCADE)
    function_name = models.CharField('功能名称', max_length=64)
    STATE_CHOICES = ((0, '正常'), (1, '异常'))
    state = models.IntegerField('用例类型', choices=STATE_CHOICES, default=0)
    precondition = models.CharField('预置条件', default='', max_length=256, help_text='最多256字符')
    desc = models.TextField('用例描述')
    steps = models.TextField('操作步骤', default='')
    expected_res = models.TextField('预期结果', default='')
    PRIORITY_CHOICES = ((1, '重要'),
                        (2, '一般'),
                        (3, '可延后'))
    priority = models.IntegerField('优先级别', default=2, choices=PRIORITY_CHOICES)
    new_added = models.BooleanField('是否新增修改', default=False)
    comment = models.CharField('备注', default='', blank=True, max_length=256)
    STATUS_CHOICES = ((0, '草稿'),
                      (1, '有效'),
                      (2, '作废'),
                      )
    status = models.IntegerField('状态', choices=STATUS_CHOICES, default=0)
    created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'test_case'
        verbose_name = '测试用例'
        verbose_name_plural = '测试用例列表'

    @property
    def attachment(self):
        return self.casefile_set.all().first()

    @property
    def name(self):
        return self.function_name or (self.submodule + self.serial_number)


class CaseFile(models.Model):
    name = models.CharField('名称', max_length=128)
    filepath = models.FileField(upload_to='files/casefile/', null=True)
    case = models.ForeignKey(Case, on_delete=CASCADE)
    created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'test_casefile'
        verbose_name = '用例附件'
        verbose_name_plural = '用例附件'

    def __unicode__(self):
        return self.name