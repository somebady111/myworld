#! /usr/bin/python3
# ! _*_ coding:utf-8 _*_

# 定制展示在后台的字段,配置在需求的admin字段展示中
from django import forms

class RegisterFOrm(forms.ModelForm):
    nickname = forms.CharField(widget=forms.TextInput,label='昵称',required=False)
