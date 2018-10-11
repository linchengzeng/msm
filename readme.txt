1、导入公共部分模板    {% include "public_template/head_top.html" %}


python manage.py startapp background_system



python manage.py makeg


'DIRS': [os.path.join(BASE_DIR,"templates")],
STATICFILES_DIRS = (os.path.join(BASE_DIR,"static"),)


from django.conf.urls import url
url('^user_login$', views.login),

runserver 80





