from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse, reverse
from Management import models

import json,hashlib

# Create your views here.

#装饰器，通过cookie判读是否已经登录
def auth(func):
    def inner(reqeust,*args,**kwargs):
        v = reqeust.COOKIES.get('email')
        if not v:
            return redirect('/login/')
        return func(reqeust, *args,**kwargs)
    return inner


@auth
def index(request):
    obj_list=models.Business.objects.all()
    return render(request,'index.html',{'obj_list':obj_list})


def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    elif request.method=='POST':
        e=request.POST.get('email')
        p=request.POST.get('pwd')

        obj = hashlib.md5()
        obj.update(bytes(p, encoding='utf8'))
        p = obj.hexdigest()
       # print(e, p)

#比较输入的密码转换为hash值之后是否和数据库中的值一样
        num = models.admin.objects.filter(email=e, password=p).count()

        if num >= 1:
            # 用户名密码一致则设置一个cookie作为标识
            print(num)
            res = redirect('/index/')
            value = {'Found': True}
            LOGINSTATUS = True
            res.set_cookie('email', e)
            return res

        else:
            print("该用户名或者密码不正确！")
            value = {'Found': False, 'display': True}
            return render(request, 'login.html', {'data': value})
            # 如果是直接进入的页面，返回页面
    else:
        return render(request, 'login.html', {'data': {'disyplay': False}})

# Create your views here.

#删除业务线
def businessdel(request,nid):
    if request.method=='GET':
        models.Business.objects.filter(id=nid).delete()
        return redirect('/business')

#修改业务线的名字，打开一个新的网页
def businessedit(request,nid):
    if request.method=='GET':
        obj=models.Business.objects.filter(id=nid)
        print(obj[0].id,obj[0].caption)
        return render(request,'businessedit.html',{'v1':obj[0]})
    elif request.method=='POST':
        n=request.POST.get('caption')
        nid=request.POST.get('id')
        models.Business.objects.filter(id=nid).update(caption=n)
        return redirect('/business')

@auth
def business(request):
    if request.method=='GET':
        v1 = models.Business.objects.all()
        print(v1)

        return render(request, 'business.html', {'v1': v1})

    elif request.method=='POST':
        u=request.POST.get('caption')
        models.Business.objects.create(caption=u)
        return  redirect('/business')

#调用一个分页的类
LIST =[]
from utils import pagination

@auth
def host(request):
    print('/host request ')
    if request.method == "GET":
        v1 = models.Host.objects.all()
        # print(v1)
        b_list = models.Business.objects.all()

        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        # print(request.COOKIES)
        val = request.COOKIES.get('count',5)
        # #非常的诡异？？cookie获取不到会报错，或者获取到奇怪的值？？！！！
        # val=request.COOKIES['per_page_count']
        # print(val)
        # if val.isdigit():
        #     val=int(val)
        # else:
        #     val=5

        print(current_page,len(v1),val)


        val= int(val)
        page_obj = pagination.Page(current_page, len(v1),val)
        s=(page_obj.start)
        print(s)
        v1 = v1[page_obj.start:page_obj.end]
        print(v1)
        page_str = page_obj.page_str("/host/")
        #返回分页的效果
        return render(request, 'host.html', { 'page_str': page_str,'v1':v1,'b_list':b_list})



    elif request.method == "POST":

        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        models.Host.objects.create(hostname=h,
                                   ip=i,
                                   port=p,
                                   b_id=b
                                   )
        return redirect('/host')


#Ajax删除app
def del_app_ajax(request):

    ret = {'status': True, 'error': None, 'data': None}
    try:
        appname=request.POST.get('app')
        hostlist=request.POST.get('hostlist')
        print(appname)
        print(hostlist)
        ll=hostlist.split()
        print(ll)

        obj=models.Application.objects.get(name=appname)

        obj.r.clear()
        obj.delete()

    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
        print('error')
    return HttpResponse(json.dumps(ret))


#添加主机
def test_ajax(request):

    ret = {'status': True, 'error': None, 'data': None}
    try:
        h = request.POST.get('hostname')
        i = request.POST.get('ip')
        p = request.POST.get('port')
        b = request.POST.get('b_id')
        if h and len(h) > 5:
            models.Host.objects.create(hostname=h,
                                           ip=i,
                                           port=p,
                                           b_id=b)
        else:
            ret['status'] = False
            ret['error'] = "主机名字太短了"
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'
        print('error')
    return HttpResponse(json.dumps(ret))


#app修改
def app_edit_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    print('ready')
    try:
        print(request.POST)
        aid=request.POST.get('nid')
        app = request.POST.get('app')
        h_id = request.POST.getlist('host_list')
        print(aid,app,h_id)

        obj = models.Application.objects.get(id=aid)
        obj.name = app
        obj.save()
        obj.r.set(h_id)



    except Exception as e:
        print(e)
        ret['error'] = 'DB Error!'
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


#删除host
def del_host_ajax(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        h_id = request.POST.get('host_id')
        b_id=request.POST.get('business_id')

        print(h_id,b_id)
        models.Host.objects.filter(nid=h_id).delete()

    except Exception as e:
        ret['error'] = 'DB Error!'
        ret['status'] = False
    return HttpResponse(json.dumps(ret))


#修改主机
def host_modify_ajax(request):
    ret={'status':True,'error':None, 'data':None}
    print(request.method)
    try:
        n_id=request.POST.get('nid')
        h=request.POST.get('hostname')
        ipaddr=request.POST.get('ip')
        p = request.POST.get('port')
        b=request.POST.get('b_id')

        print(n_id,h,p,b)
        models.Host.objects.filter(nid=n_id).update(hostname=h,ip=ipaddr,port=p,b_id=b)

    except Exception as e:
        ret['error']='DB Error!'
        ret['status']=False

    print(ret)
    return HttpResponse(json.dumps(ret))

#注销，删掉cookie
def logout(request):
    res=render(request,'login.html')
    res.delete_cookie('email')
    res.delete_cookie('count')
    return res


#app的页面
@auth
def app(request):
    if request.method == "GET":
        app_list = models.Application.objects.all()

        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        # print(request.COOKIES)
        val = request.COOKIES.get('count', 5)

        val = int(val)
        page_obj = pagination.Page(current_page, len(app_list), val)
        s = (page_obj.start)
        print(s)
        app_list = app_list[page_obj.start:page_obj.end]
        # print(v1)
        page_str = page_obj.page_str("/app/")
        # 返回分页的效果

        host_list = models.Host.objects.all()
        return render(request, 'app.html', {'app_list':app_list,'page_str': page_str, 'host_list': host_list})
        # for row in app_list:
        #     print(row.name,row.r.all())

        # return render(request,'app.html',{"app_list": app_list,})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        # print(app_name,host_list)

        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)

        return redirect('/app')

#添加app
def ajax_add_app(request):
    ret = {'status':True, 'error':None, 'data': None}
    try:
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)
    except Exception as e:
        ret['status'] = False
        ret['error'] = '请求错误'

    # print(ret)

    return HttpResponse(json.dumps(ret))