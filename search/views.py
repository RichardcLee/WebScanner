from django.shortcuts import render, HttpResponse
from .utils import search_method

# Create your views here.


def search(request):
    """
    search 方法只能为post请求
    :param request: django request
    :return: html
    """
    if request.method == 'POST':
        input_search = request.POST.get('input_search')
        context = {
            'obj_list': None
        }
        # 条件查询
        if ':' in input_search:
            method, data = input_search.split(':')
            return search_method.tag_search(request, data=data, method=method)
        # 全局模糊查询
        else:
            pass
        return HttpResponse('暂不支持模糊查询')
