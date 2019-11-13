from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    '''
    return:注册表
    '''
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = {
        (STATUS_NORMAL,'已注册'),
        (STATUS_DELETE,'未注册'),
    }
    nickname = models.CharField(max_length=10,blank=False,verbose_name='昵称',unique=True)
    username = models.CharField(max_length=15,blank=False,verbose_name='用户名',unique=True)
    password = models.CharField(max_length=20,blank=False,verbose_name='账户密码')
    status = models.PositiveIntegerField(default=STATUS_NORMAL,choices=STATUS_ITEMS,verbose_name='注册状态')
    register_time = models.DateTimeField(auto_now_add=True,verbose_name='注册时间')

    def __str__(self):
        return self.nickname

    class Meta:
        db_table = 'Register'
        verbose_name = '用户注册表'
        verbose_name_plural = verbose_name
        ordering = ['-id']
