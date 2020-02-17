from django.shortcuts import render, redirect, HttpResponse
from .models import JsonPlug, ScriptPlug, PlugType
from collections import defaultdict
import os
from django.db.models import F
from django.core.files import File


def plug_list(request, plug_type):
    """
    显示某个分类的插件列表
    :param request:
    :param plug_type: plug type, eg.localhost:8000/plug/认证绕过 type=认证绕过
    :return:
    """
    plug_type = plug_type.rstrip('/')
    print(plug_type)

    # if type 在数据库中不存在:
    #     return(request, 'error.html', context={'info': '没有此类型的插件列表！请仔细确认后重试。'})

    if request.method == 'GET':
        # 略，此处获取相应插件列表
        json_plugs = JsonPlug.objects.filter(plug_type__p_type=plug_type).all()
        script_plugs = ScriptPlug.objects.filter(plug_type__p_type=plug_type).all()
        return render(request, 'plug_list.html', context={'json_list': json_plugs, 'script_list': script_plugs, 'type': plug_type})
    else:
        # 返回error.html
        # return redirect(request, 'error.html', context={'info': '出错了，非法访问。'})
        return render(request, 'error.html', context={'info': '出错了，非法访问。'})


def add_plug(request):
    """
    添加插件，仅返回html页面
    :param request:
    :return:
    """
    plug_type_list = PlugType.objects.all()
    context = {
        'plug_type_list': plug_type_list
    }
    return render(request, 'add_plug.html', context=context)


def upload_json(request):
    """
    上传json插件
    :param request:
    :return:
    """
    # ... 数据库存取
    print('————————json————————')
    print(request.POST)
    plug_name = request.POST.get('plug_name')
    plug_info = request.POST.get('plug_intor')
    plug_author = request.POST.get('plug_author')
    plug_author_link = request.POST.get('author_link')
    plug_content = request.POST.get('plug_content')
    analyzing_data = request.POST.get('analysis_sample')
    search_tag = request.POST.get('search_condition')
    tag = request.POST.get('plug_tag')
    crisis_level, analyzing_type, plug_type = request.POST.getlist(
        'multi-attribute')
    if plug_type == 'user-define-json':
        plug_type = request.POST.get('user-define-json').replace(' ', '').replace('.', '')   # 不可有空格和'.'
        if PlugType.objects.filter(p_type=plug_type).first() is None:
            try:
                PlugType.objects.create(p_type=plug_type, num=0).save()
            except Exception as e:
                print("![ERROR] %s" % e)
            else:
                print("*[SUCCESS] 创建成功")
    else:
        plug_type = PlugType.objects.filter(id=plug_type).first().p_type  # 因为本来传过来的是id（非用户自定义类型）

    PlugType.objects.filter(p_type=plug_type).update(num=F('num')+1)    # num+1
    plug_type = PlugType.objects.filter(p_type=plug_type).first()
    try:
        JsonPlug.objects.create(plug_type=plug_type,
                                name=plug_name,
                                crisis_level=crisis_level,
                                info=plug_info,
                                author=plug_author,
                                plug_url=plug_author_link,
                                analyzing_type=analyzing_type,
                                analyzing_data=analyzing_data,
                                content=plug_content,
                                search_tag=search_tag,
                                tag=tag,
                                )
    except Exception as e:
        print("![ERROR] %s" % e)
    return redirect('index')


def upload_script(request):
    """
    上传script插件
    :param request:
    :return:
    """
    print('————————script————————')
    print('is ajax?: ', request.is_ajax())  # 如果是ajax，不会也不应该重定向
    print(request.POST)
    print(request.FILES)

    file = request.FILES.get('files[]', None)
    print(file, type(file))

    if file is None:  # 避免未知错误造成重大影响
        return render(request, 'error.html', context={'info': '上传失败，请重试！'})

    fn = request.POST.get('csrfmiddlewaretoken', None)
    if fn is None:  # 其实不会是None
        fn = 'None'

    with open('./media/plug/tmp/%s-%s.tmp' % (fn, file.name), "wb") as f:
        for chunk in file.chunks():
            f.write(chunk)

    return HttpResponse("ok")
    # return redirect('index')


def upload_script_done(request):
    '''
    确认上传
    :param request:
    :return:
    '''
    print('————————script done————————')
    print(request.POST)

    tk = request.POST.get('csrfmiddlewaretoken', None)
    ud = request.POST.get('user-define-script', None)
    pt = request.POST.get('plug_type', None)
    print(tk, ud, pt)

    if tk is None:
        tk = 'None'

    # 自定义类型
    if pt == 'user-define-script':
        pt = ud.replace(' ', '').replace('.', '')  # 不可有空格和'.'
        if PlugType.objects.filter(p_type=pt).first() is None:
            try:
                PlugType.objects.create(p_type=pt, num=0).save()
            except Exception as e:
                print("![ERROR] %s" % e)
            else:
                print("*[SUCCESS] 创建成功")
    else:
        pt = PlugType.objects.filter(id=pt).first().p_type  # 因为本来传过来的是id（非用户自定义类型）

    # 寻找tmp file
    tmp_file = os.listdir('./media/plug/tmp')
    tmp = None
    for file in tmp_file:
        if file.startswith(tk):
            tmp = file
    if tmp is None:  # 若未找到
        return HttpResponse('failed! unable to done with upload script, reason: cant find tmp file.')

    PlugType.objects.filter(p_type=pt).update(num=F('num') + 1)  # num+1
    pt_ = pt
    pt = PlugType.objects.filter(p_type=pt).first()  # pt_是字符串 pt是对象

    with open('./media/plug/tmp/%s' % tmp, 'rb') as f:
        try:
            file = File(f)
            print(file.name)
            file.name = file.name.replace('./media/plug/tmp/'+tk+'-', '').replace('.tmp', '')
            print(file.name)
            ScriptPlug.objects.create(plug_type=pt, script_file=file)
        except Exception as e:
            print("![ERROR] %s" % e)

    # 别忘了删除tmp文件
    if os.path.exists('./media/plug/tmp/%s' % tmp):
        os.remove('./media/plug/tmp/%s' % tmp)

    return redirect('index')


def remove_script(request):
    """
    删除上传的文件
    :param request:
    :return:
    """
    print('————————remove script————————')
    print(request.POST)
    tk = request.POST.get('csrfmiddlewaretoken', None)
    fn = request.POST.get('file', None)
    if fn is None:
        return HttpResponse('failed! no such file?')

    if tk is None:
        tk = 'None'

    if os.path.exists('./media/plug/tmp/%s-%s.tmp' % (tk, fn)):
        os.remove('./media/plug/tmp/%s-%s.tmp' % (tk, fn))

    return HttpResponse("ok")
