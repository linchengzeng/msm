from django.db import models

# Create your models here.

class Department(models.Model):
    """
    用户所属部门
    :param department_name:部门名
    """
    department_name = models.CharField(max_length=32)


class UserType(models.Model):
    """
    用户类型表，用于判断用户权限级别
    :param type_name：类型名称
    """
    user_type_name = models.CharField(max_length=32)


class UserInfo(models.Model):
    """
    用户信息表
    :param username:用户名
    :param password:密码
    :param user_type:用户权限级别
    :param user_department:用户所属部门
    :param email:邮箱
    """
    user_name = models.CharField(max_length=32)
    pass_word = models.CharField(max_length=32)
    user_type = models.ForeignKey(UserType, blank=True, null=True, on_delete=models.SET_NULL)
    user_department = models.ForeignKey(Department, blank=True, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(null=True)

class ProductType(models.Model):
    """
    物资类型表
    :param material_name类型名称
    一类物资：指设备类物资；单位价值在2000元以上（含2000元）或使用期限超过1年并明显具备重复利用性质的，与研发活动有关的设备、软件、仪器仪表、备品备件、器具、工具等。
    二类物资：指材料类物资；单位价值在2000元以下，与研发活动有关的备品备件、器具、工具等。研发测试用手机、平板电脑（PAD）等终端设备由于技术更新较快，使用期限较短，将其归结为材料类物资，按资产管理。
    三类物资：指资产属性不属于工商银行北京分行帐套或总部帐套，主要来自研发项目用于合作研发实验测试的合作伙伴、设备厂家的外部物资。
    """
    material_name = models.CharField(max_length=32)


class ProductInfo(models.Model):
    """
    产品信息表
    :param product_name:产品名称
    :param product_type:物资类型
    :param product_num:库存数量
    :param product_buyer:采购员
    :param purchase_date:采购时间
    """
    product_name = models.CharField(max_length=32)
    product_type = models.ForeignKey(ProductType, blank=True,null=True, on_delete=models.SET_NULL)
    unit_price = models.IntegerField
    product_buyer = models.ForeignKey(UserInfo, blank=True,null=True, on_delete=models.SET_NULL)
    purchase_date = models.DateField



class MaterialUseRequest(models.Model):
    """
    物资使用申请单
    :param applicant:申请人
    :param application_dep:申请部门
    :param application_basis:申请依据
    :param purpose_of_use:使用目的
    :param material_obj:物资对象
    :param request_num:申请数量
    :param use_date:使用期限
    :param audit_opinion:审核意见（利旧或新购）
    :param request_date:申请日期
    """
    applicant = models.ForeignKey(UserInfo, blank=True,null=True, on_delete=models.SET_NULL,related_name="applicant")
    application_dep = models.ForeignKey(UserInfo, blank=True,null=True, on_delete=models.SET_NULL,related_name="application_department")
    application_basis = models.CharField(max_length=32)
    material_obj = models.ForeignKey(ProductInfo, blank=True,null=True, on_delete=models.SET_NULL)
    request_num = models.IntegerField
    use_date = models.DateField
    audit_opinion = models.CharField(max_length=32)
    request_date = models.DateField


class MaterialOutRequest(models.Model):
    """
    物资出库单
    :param applicant:申请人
    :param out_date:出库时间
    :param out_numb:申请数量
    :param use_department:申请部门
    :param use_date:使用期限
    :param use_add:使用地点
    :param out_date:出库日期
    :param operator_id:操作员ID
    """
    applicant = models.ForeignKey(UserInfo, blank=True,null=True, on_delete=models.SET_NULL,related_name="applicant_id")
    out_date = models.DateField
    material_obj = models.ForeignKey(ProductInfo, blank=True,null=True, on_delete=models.SET_NULL)
    use_department = models.ForeignKey(Department, blank=True,null=True, on_delete=models.SET_NULL)
    use_date = models.DateField
    use_add = models.CharField(max_length=32)
    out_numb = models.IntegerField
    out_date = models.DateField
    operator_id = models.ForeignKey(UserInfo, blank=True,null=True, on_delete=models.SET_NULL, related_name="Material_Out_operator_id")


class Warehouse(models.Model):
    """
    仓库
    :param ware_name:仓库名称
    """
    ware_name = models.CharField(max_length=32)


class PurchaseWarehouse(models.Model):
    """
    采购物资入库
    :param material_obj:物资对象
    :param ware_num:入库数量
    :param purchase_basis:采购依据
    :param ware_date:入库时间
    :param ware_req_user:入库申请人
    :param operator_id:操作员ID
    """
    material_obj = models.ForeignKey(ProductInfo,blank=True,null=True, on_delete=models.SET_NULL)
    ware_num = models.IntegerField
    purchase_basis= models.CharField(max_length=32)
    ware_date = models.DateField
    warehouse_request_user = models.ForeignKey(UserInfo,blank=True,null=True, on_delete=models.SET_NULL,related_name="warehouse_request_user")
    operator_id = models.ForeignKey(UserInfo,blank=True,null=True, on_delete=models.SET_NULL,related_name="operator_id")
    wareh = models.ForeignKey(Warehouse,blank=True,null=True, on_delete=models.SET_NULL)


class ReturnWarehouse(models.Model):
    """
    归还物资入库单
    :param material_obj:物资对象
    :param return_num:归还数量
    :param use_user:使用人
    :param user_department:使用部门
    :param use_date:使用期限
    :param return_date:归还时间
    :param operator_id:操作员ID
    """
    material_obj = models.ForeignKey(ProductInfo,blank=True,null=True, on_delete=models.SET_NULL)
    return_num = models.IntegerField
    use_user = models.ForeignKey(UserInfo,blank=True,null=True, on_delete=models.SET_NULL,related_name="use_user")
    user_department = models.ForeignKey(UserInfo,blank=True,null=True, on_delete=models.SET_NULL,related_name="ReturnWarehouse_user_department")
    use_date= models.DateField
    return_date = models.DateField
    operator_id = models.ForeignKey(UserInfo,blank=True,null=True, on_delete=models.SET_NULL,related_name="Return_Warehouse_operator_id")


