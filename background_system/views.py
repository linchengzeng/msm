from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from background_system import models
from static import appsetting


def default(request):
    return render(request,"login.html",{"app_name":appsetting.app_name})


def login(request):
    print("this is login action")
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)
    request.session["username"] = username
    return render(request,"index.html",{"app_name":appsetting.app_name})

######用户管理#####

def user_list(request):
    user_list_info = models.UserInfo.objects.all()
    return render(request,"usermanage/user_list.html",{"user_list_info":user_list_info})


def add_user(request):
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)
    email = request.POST.get("email",None)
    result = models.UserInfo(user_name=username,pass_word=password,user_type_id="",user_department_id="",email=email)
    result.save()
    return redirect("usermanage/user_list.html")


def edit_uesr_info(request):
    uid = request.POST.get("uid", None)
    username = request.POST.get("username",None)
    password = request.POST.get("password",None)
    user_type = request.POST.get("user_type",None)
    user_department = request.POST.get("user_department",None)
    email = request.POST.get("email", None)
    new_userinfo = {"id": uid, "user_name": username, "pass_word": password, "user_type_id": user_type,
                        "user_department_id": user_department, "email": email}
    models.UserInfo.objects.filter(id=uid).update(**new_userinfo)
    return render(request,"success.html",{"editor_res":"success","url_path":"get_userinfo.html?uid="+uid})


def get_unit_userinfo(request):
    uid = request.GET.get("uid",None)
    user_obj = models.UserInfo.objects.filter(id = uid).first()
    user_type_list_obj = models.UserType.objects.filter()
    department_list_obj = models.Department.objects.filter()
    dicts = {"user_obj":user_obj,"user_type_list_obj":user_type_list_obj,"department_list_obj":department_list_obj}
    # print(user_obj)
    # print(user_obj.user_name)
    # print(user_obj.pass_word)
    # print(user_obj.user_type)
    # print(user_obj.user_department_id)
    # print(user_obj.email)
    return render(request,"usermanage/userinfo_editor.html",dicts)


def del_userinfo(request):
    user_id = request.GET.get("uid",None)
    models.UserInfo.objects.filter(id = user_id).delete()
    return redirect("usermanage/user_list.html")

######用户组管理#####

def user_type_list(request):
    """
    用户组列表
    :param request:
    :return:
    """
    user_type_list_obj = models.UserType.objects.all()
    return render(request,"usertypemanage/user_type_list.html",{"user_type_list_obj":user_type_list_obj})


def user_type_add(request):
    """
    用户组添加
    :param request:
    :return:
    """
    user_type_name = request.POST.get("user_type_name",None)
    models.UserType.objects.create(user_type_name = user_type_name)
    return redirect("user_group_list.html")

def user_type_editor(request,user_type_id):
    """
    用户组修改
    :param request:
    :return:
    """
    # user_type_id = request.POST.get("user_type_id",None)
    user_type_name = request.POST.get("user_type_name",None)
    models.UserType.objects.filter(id = user_type_id).update(user_type_name = user_type_name)
    return render(request,"success.html",{"editor_res":"success","url_path":"get-user-type-"+user_type_id+".html"})


def get_unit_user_type(request, usertypeid):
    """
    获得单个用户类型
    :param request:
    :return:
    """
    # user_type_name = request.POST.get("user_type_name",None)
    # user_type_obj = {"id":usertypeid,"user_type_name":user_type_name}
    # models.UserType.objects.filter(id=usertypeid).update(**user_type_obj)
    user_type_obj = models.UserType.objects.filter(id = usertypeid).first()
    return render(request,"usertypemanage/user_type_editor.html",{"user_type_obj":user_type_obj})


def user_type_del(request):
    """
    用户组删除
    :param request:
    :return:
    """
    user_type_id = request.GET.get("user_type_id",None)
    models.UserType.objects.filter(id = user_type_id).delete()
    return redirect("user_type_list.html")


######部门管理#####
def department_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    department_list_obj = models.Department.objects.all()
    return render(request,"departmentmanage/department_list.html",{"department_list_obj":department_list_obj})


def add_department(request):
    """
    添加部门
    :param request:
    :return:
    """
    department_name = request.POST.get("department_name",None)
    # print(department_name)
    models.Department.objects.create(department_name = department_name)
    return redirect("department_list.html")


def get_unit_department(request,dep_id):
    """
    获取单个部门信息
    :param request:
    :return:
    """
    department_obj = models.Department.objects.filter(id = dep_id).first()
    return render(request,"departmentmanage/department_editor.html",{"department_obj":department_obj})


def edit_department(request):
    """
    修改部门信息
    :param request:
    :return:
    """
    dep_id = request.POST.get("department_id",None)
    department_name = request.POST.get("department_name",None)
    models.Department.objects.filter(id = dep_id).update(department_name = department_name)
    # print(request.path)
    return render(request, "success.html", {"editor_res": "success","url_path":"get_unit_department-"+dep_id+".html"})


######物资类型管理#####
def material_list(request):
    """
    物资类型列表
    :param request:
    :return:
    """
    material_list_obj = models.ProductType.objects.filter()
    # print(material_list_obj)
    return render(request, "materialmanage/material_list.html", {"material_list_obj": material_list_obj})

def add_material(request):
    """
    添加物资类型
    :param request:
    :return:
    """
    material_name = request.POST.get("material_name",None)
    models.ProductType.objects.create(material_name = material_name)
    # print(material_name)
    return redirect("material_list$")


def test(request):
    print("这是一个测试方法")
    return render(request,"layouts-fixed-footer.html")