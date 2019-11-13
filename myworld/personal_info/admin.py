from django.contrib import admin
from .models import Register
from .adminforms import RegisterFOrm
from myworld.custom_site import custom_site

from django.contrib.admin.models import LogEntry
# Register your models here.

@admin.register(Register,site=custom_site)
class RegisterAdmin(admin.ModelAdmin):
    list_display = [
        'nickname','status','register_time','username','password'
    ]
    # 需求字段展示装饰调用
    form = RegisterFOrm
    # 限定展示字段
    fieldsets = (
        ('基础配置',{
            'description':'基础配置描述',
            'fields':(
                'nickname',
                'username',
                'password',
                'register_time',
                'status'
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(RegisterAdmin,self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(RegisterAdmin,self).get_queryset(request)
        return qs.filter(user=request.user)


@admin.register(LogEntry,site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = [
        'user'
    ]
