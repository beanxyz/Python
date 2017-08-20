from django.shortcuts import render
from django.shortcuts import redirect, HttpResponse, reverse
from Management import models

import json,hashlib

# Create your views here.
def auth(func):
    def inner(reqeust,*args,**kwargs):
        v = reqeust.COOKIES.get('email')
        if not v:
            return redirect('/login/')
        return func(reqeust, *args,**kwargs)
    return inner


@auth
def index(request):

    #插入一些测试的数据

    #单表
    # li=['IT','Finance','HR','DEVELOPMENT','SALES','PR']
    # for i in range(len(li)):
    #     models.Business.objects.create(caption=li[i])

    #
    #
    # obj = hashlib.md5()
    # obj.update(bytes('password', encoding='utf8'))
    # result = obj.hexdigest()
    #
    # models.admin.objects.create(email='admin@aa.com',password=result)


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


        print(e, p)

        num = models.admin.objects.filter(email=e, password=p).count()

        if num >= 1:
            print("Bingo")
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


def businessdel(request,nid):
    if request.method=='GET':
        models.Business.objects.filter(id=nid).delete()
        return redirect('/business')

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

LIST =[]
from utils import pagination

@auth
def host(request):
    print('/host request ')
    if request.method == "GET":
        v1 = models.Host.objects.filter(nid__gt=0)
        # v2 = models.Host.objects.filter(nid__gt=0).values('nid','hostname','b_id','b__caption')
        # v3 = models.Host.objects.filter(nid__gt=0).values_list('nid','hostname','b_id','b__caption')

        b_list = models.Business.objects.all()

        current_page = request.GET.get('p', 1)
        current_page = int(current_page)
        print(request.COOKIES)
        # val = request.COOKIES.get('per_page_count',5)
        val=request.COOKIES['per_page_count']
        if val.isdigit():
            val=int(val)
        else:
            val=5

        print(val)

        val= int(val)
        page_obj = pagination.Page(current_page, len(v1),val)
        print("%d,%d"%(page_obj.start,page_obj.end))
        v1 = v1[page_obj.start:page_obj.end]

        page_str = page_obj.page_str("/host/")

        # print(v1,len(v1))

        # print(page_str)

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

def logout(request):
    res=render(request,'login.html')
    res.delete_cookie('email')
    res.delete_cookie('per_page_count')
    return res


@auth
def app(request):
    if request.method == "GET":
        app_list = models.Application.objects.all()
        # for row in app_list:
        #     print(row.name,row.r.all())

        host_list = models.Host.objects.all()
        return render(request,'app.html',{"app_list": app_list,'host_list': host_list})
    elif request.method == "POST":
        app_name = request.POST.get('app_name')
        host_list = request.POST.getlist('host_list')
        # print(app_name,host_list)

        obj = models.Application.objects.create(name=app_name)
        obj.r.add(*host_list)

        return redirect('/app')


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