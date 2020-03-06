# -*- encoding: utf-8 -*-
"""
@File    : helpers.py
@Time    : 2020/3/4 9:50 下午
@Author  : peterWang
"""
from functools import wraps
from django.http import HttpResponseBadRequest
from django.views import View
from django.core.exceptions import PermissionDenied


def ajax_required(f):

    @wraps(f)
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest('不是AJAX请求！')
        return f(request, *args, **kwargs)
    return wrap


class AuthorRequiredMixin(View):
    """验证是否为原作者，用于状态删除和文章编辑"""
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().user.username != request.user.username:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

