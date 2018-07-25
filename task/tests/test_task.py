import os;os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TaskTracing.settings");import django;django.setup()
from django.test import TestCase
from cauth.models import User
from task.models import Task


class TaskTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User(id=1,
             username='admin',
             nickname='admin',
             email= 'qq@qq.com',
             is_staff=True,
             is_superuser=True,
             password='pbkdf2_sha256$36000$gic6cD6CQfgr$QXWqtrAfyCFDjl/B+beGfvS9JzMMMCVUgokVJnKP8D4='
        ).save()

    def test_normal_process(self):
        task = Task.objects.first()
        user = User.objects.first()
        task.verify(user)
        task.allocate()
        task.finish()