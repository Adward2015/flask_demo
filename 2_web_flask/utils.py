# -*- coding: utf-8 -*-
from flask import session, redirect, request
from functools import wraps


def login_required(view_func):
    @wraps(view_func)
    def inner(*args, **kwargs):
        if not session.get('user_info'):
            # 如果是通过其他页面跳转到登录页面的,记录当前页面的path,方便登录之后跳转
            if request.path != "/login":
                session['redirect'] = request.path
            return redirect('/login')
        return view_func(*args, **kwargs)

    return inner
