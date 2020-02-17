from django.shortcuts import render
from plug.models import PlugType
from task.models import Task


def index(request):
    """
    扫描器首页
    :param request django request
    :return index.html
    """
    vul_type_list = PlugType.objects.all()
    task_list = Task.objects.all()

    context = {
        'vul_type_list': vul_type_list,
        'task_list': task_list
    }
    return render(request, 'index.html', context=context)
