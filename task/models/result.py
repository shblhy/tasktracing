from django.db import models
from cauth.models import User
from django.db.models.deletion import SET_NULL, CASCADE
from .task import Task


class TaskResult(models.Model):
    task = models.ForeignKey(Task, on_delete=CASCADE)
    stage = models.IntegerField()
    status = models.IntegerField()
    desc = models.TextField(verbose_name="结果描述")
    created_by = models.ForeignKey(User, null=True, on_delete=SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'test_taskresult'
