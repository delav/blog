# -*- coding:utf-8 -*-
from django import forms


class LoginForm(forms.Form):
    """
    登录表单
    """
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required"}),
                               max_length=50, error_messages={"required": "用户名不能为空",})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required"}),
                               max_length=20, error_messages={"required": "密码不能为空",}),


class RegForm(forms.Form):
    """
    注册表单
    """
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "用户名", "required": "required"}),
                               max_length=50, error_messages={"required": "用户名不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "邮箱", "required": "required"}),
                             max_length=50, error_messages={"required": "邮箱不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "个人网址", }), max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "密码", "required": "required"}),
                               max_length=20, error_messages={"required": "密码不能为空"})


class CommentForm(forms.Form):
    """
    评论表单
    """
    author = forms.CharField(widget=forms.TextInput(attrs={"id": "author", "class": "comment_input",
                                                           "required": "required", "size": "25", "tabindex": "1"}),
                             max_length=50, error_messages={"required": "用户名不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"id":"email", "type": "email", "class": "comment_input",
                                                           "required": "required", "size": "25", "tabindex": "2"}),
                             max_length=50, error_messages={"required": "邮箱不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"id": "url", "type": "url", "class": "comment_input",
                                                       "size": "25", "tabindex": "3"}), max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"id": "comment", "class": "message_input",
                                                           "required": "required", "cols": "25",
                                                           "rows": "5", "tabindex": "4"}),
                              error_messages={"required": "评论不能为空",})
    article = forms.CharField(widget=forms.HiddenInput())


