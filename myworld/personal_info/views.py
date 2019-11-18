from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import Register
from .forms_1 import Form_1
from .forms_2 import Form_2
from .forms_3 import Form_3

# Create your views here.

# 读取model层的数据并展示，参数为需要展示的字段(按照HTML页面的内容进行参数获取)
def Login(request):
    '''
    这是登录界面对数据库的查询操作
    :param request:
    :param username: 用户名
    :param password: 用户密码
    :return: 查询到的用户名和用户密码
    '''
    try:
        form = Form_1(request.POST)
        if request.method == "GET":
            return render(request, 'personal_info/log.html')

        elif request.method == "POST":
            if form.is_valid():
                try:
                    # 获取登录用户
                    user_id = form.cleaned_data['username']
                    pass_id = form.cleaned_data['password']
                except ValueError:
                    return HttpResponse('warning_info:{}'.format('请输入正确的账户和密码'))
                try:
                    user = Register.objects.get(username=user_id).username
                    passwd = Register.objects.get(username=user).password
                    ncname = Register.objects.get(username=user).nickname
                    if user == user_id and passwd == pass_id:
                        return render(request,'personal_info/login.html',context={'nickname':ncname})
                except Register.DoesNotExist:
                    return HttpResponse('warning_info:{}'.format('输入账号密码错误'))
    except:
        return HttpResponse('请求值为空')

def register_user(request):
    '''
    这是对model层建立数据库的插入操作
    :param request:
    :param nickname: 昵称
    :param username: 用户名
    :param password: 用户密码
    :return: 插入数据库信息
    '''
    form = Form_2(request.POST)
    # 判断请求方式,第一层请求到页面，不提交任何内容，只返回给页面，提交方式为GET
    if request.method == "GET":
        return render(request, 'personal_info/register.html')

    elif request.method == "POST":
        # 表单校验
        if form.is_valid():
            try:
                # 表单数据
                nickname = form.cleaned_data['nickname']
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                repassword = form.cleaned_data['repassword']
            except:
                return HttpResponse('请求数据错误')

            try:
                # 判断密码是否一致
                if password == repassword:
                    # 插入数据到数据库
                    Register.objects.create(nickname=nickname, username=username, password=password)
                    return render(request, 'personal_info/log.html')
                else:
                    return HttpResponse('密码输入不一致')
            except:
                return HttpResponse('添加用户失败')

def Personal(request):
    return render(request, 'personal_info/personal.html')

def Modify_info(request):
    # 获取当前登录用户名

    form = Form_3(request.POST)
    # 判断请求方式,第一层请求到页面，不提交任何内容，只返回给页面，提交方式为GET
    if request.method == "GET":
        return render(request, 'personal_info/modify_info.html')

    elif request.method == "POST":
        # 表单校验
        if form.is_valid():
            try:
                # 表单数据
                re_nickname = form.cleaned_data['new_nickname']
                re_username = form.cleaned_data['new_username']
                re_password = form.cleaned_data['new_password']
                re_repassword = form.cleaned_data['re_new_repassword']
            except:
                return HttpResponse('请求数据错误')

            try:
                # 判断密码是否一致
                if re_password == re_repassword:
                    # 更新插入数据到数据库
                    Register.objects.filter(username=re_username).update(nickname=re_nickname, username=re_username, password=re_password)
                    return render(request, 'personal_info/personal.html')
                else:
                    return HttpResponse('密码输入不一致')
            except:
                return HttpResponse('添加用户失败')
