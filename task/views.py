from django.shortcuts import render, redirect, HttpResponse
from plug.models import JsonPlug, ScriptPlug, PlugType
from .models import Task
from django.http import JsonResponse
from django.core import serializers
from re import sub
# Create your views here.


def task_index(request, page=1):
    """
    任务模块展示
    :param request: django request
    :param page 当前页，默认值为1
    :return: html
    """
    return render(request, 'task.html')


def task_create(request):
    """
    创建任务
    :param request: django request
    :return: html
    """
    if request.method == "GET":
        if request.is_ajax():
            print('ajax')
            task_type = request.GET.get('task_type')
            print(task_type)
            json_plug_list = JsonPlug.objects.filter(plug_type__p_type=task_type)
            script_plug_list = ScriptPlug.objects.filter(plug_type__p_type=task_type)
            json_plug_list = [{'name': jp.name, 'id': jp.id, 'plug_type': jp.plug_type.p_type} for jp in json_plug_list]

            def f(path):
                # path = sub('\..*', '', path)    # 文件后缀
                path = sub('.*/', '', path)     # 路径前缀
                return path
            script_plug_list = [{'name': f(sp.script_file.name), 'id': sp.id, 'plug_type': sp.plug_type.p_type} for sp in script_plug_list]
            print(json_plug_list)
            print(script_plug_list)
            # json_plug_list = serializers.serialize("json", json_plug_list)
            # script_plug_list = serializers.serialize("json", script_plug_list)

            context = {
                'json_plug_list': json_plug_list,
                'script_plug_list': script_plug_list
            }
            return JsonResponse(context)
        else:
            print('just get')
            task_type_list = PlugType.objects.all()  # 插件类型就是任务类型
            context = {
                'task_type_list': task_type_list
            }
            return render(request, 'task_create.html', context=context)

    elif request.method == "POST":
        task_name = request.POST.get('task_name')
        task_type = request.POST.get('task_type')
        target_address = request.POST.get('target_address')
        target_port = request.POST.get('target_port')
        run_date, auto_flush, crisis_level = request.POST.getlist(
            'multi-attribute')
        task = Task.objects.create(name=task_name,
                                   run_times=run_date,
                                   task_type=task_type,
                                   crisis_level=crisis_level,
                                   target=target_address,
                                   is_auto_flush=auto_flush,
                                   port=target_port)
        plug_type = request.POST.get('ext')

        if plug_type == 'json':
            print(1)
            plug = JsonPlug.objects.filter(
                id=request.POST.get('jplug')).first()
            task.json_plugs.add(plug)
        else:
            print(2)
            plug = JsonPlug.objects.filter(
                name=request.POST.get('splug')).first()
            task.script_plugs.add(plug)
        task.save()
        return redirect('Task:task_detail', 1)


def task_detail(request, tid):
    """
    查看任务详情
    :param request: django request
    :param tid: 任务编号
    :return: html
    """
    if request.method == "GET":
        return render(request, 'task_detail.html')



