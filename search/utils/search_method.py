from plug.models import JsonPlug
from task.models import Task
from django.shortcuts import HttpResponse, render


def tag_search(request, data, method='port'):
    """
    根据标签查询
    :param request: django request
    :param data: str 查询数据
    :param method: str 查询方法标签，port=》端口查询，tag=》插件查询， task=》任务查询, target=》服务器目标
    :return:
    """
    res = {}
    if method == 'port':
        res['obj_list'] = Task.objects.filter(port=data).all()
        print('===>> port')
    elif method == 'tag':
        res['json_list'] = JsonPlug.objects.filter(search_tag__icontains=data).all()
        res['type'] = data
        print('===>> tag')
        return render(request, 'plug_list.html', context=res)
    elif method == 'task':
        res['obj_list'] = Task.objects.filter(name__icontains=data).all()
        print('===>> task')
    elif method == 'target':
        res['obj_list'] = Task.objects.filter(target=data).all()
        print('===>> target')
    print('---->', data)
    return HttpResponse('ok')


def global_search(data):
    """
    全局模糊查询
    :param data: str查询条件
    :return:
    """
    pass
