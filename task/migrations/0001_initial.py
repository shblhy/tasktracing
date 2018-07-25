# Generated by Django 2.0.7 on 2018-07-25 18:41

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('function_name', models.CharField(max_length=64, verbose_name='功能名称')),
                ('state', models.IntegerField(choices=[(0, '正常'), (1, '异常')], default=0, verbose_name='用例类型')),
                ('precondition', models.CharField(default='', help_text='最多256字符', max_length=256, verbose_name='预置条件')),
                ('desc', models.TextField(verbose_name='用例描述')),
                ('steps', models.TextField(default='', verbose_name='操作步骤')),
                ('expected_res', models.TextField(default='', verbose_name='预期结果')),
                ('priority', models.IntegerField(choices=[(1, '重要'), (2, '一般'), (3, '可延后')], default=2, verbose_name='优先级别')),
                ('new_added', models.BooleanField(default=False, verbose_name='是否新增修改')),
                ('comment', models.CharField(blank=True, default='', max_length=256, verbose_name='备注')),
                ('status', models.IntegerField(choices=[(0, '草稿'), (1, '有效'), (2, '作废')], default=0, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='项目')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例列表',
                'db_table': 'test_case',
            },
        ),
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('filepath', models.FileField(null=True, upload_to='files/casefile/')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Case')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '用例附件',
                'verbose_name_plural': '用例附件',
                'db_table': 'test_casefile',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_case', jsonfield.fields.JSONField(blank=True, max_length=2560, null=True, verbose_name='测试用例')),
                ('start_time', models.DateField(verbose_name='开始时间')),
                ('end_time', models.DateField(verbose_name='结束时间')),
                ('commit', models.TextField(blank=True, default='', help_text='测试重点和其它要求', verbose_name='重点说明')),
                ('verify_ready_time', models.DateTimeField(null=True, verbose_name='可审核时间')),
                ('verify_time', models.DateTimeField(null=True, verbose_name='审核时间')),
                ('allocate_time', models.DateTimeField(null=True, verbose_name='分配时间')),
                ('executor_ids', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[(0, '草稿'), (1, '待审核'), (2, '待分配'), (3, '待执行'), (4, '执行中'), (5, '结果确认中'), (6, '已完成'), (8, '审核失败'), (9, '已作废')], default=0, verbose_name='状态')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='item.Item', verbose_name='项目')),
                ('verifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verifier', to=settings.AUTH_USER_MODEL, verbose_name='审核人')),
            ],
            options={
                'verbose_name': '测试任务',
                'verbose_name_plural': '测试任务列表',
                'db_table': 'test_task',
            },
        ),
        migrations.CreateModel(
            name='TaskResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField()),
                ('status', models.IntegerField()),
                ('desc', models.TextField(verbose_name='结果描述')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Task')),
            ],
            options={
                'db_table': 'test_taskresult',
            },
        ),
    ]