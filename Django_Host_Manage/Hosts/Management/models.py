from django.db import models

# Create your models here.

#本地管理员表
class admin(models.Model):
    email=models.EmailField(max_length=64)
    password=models.CharField(max_length=32)

#业务线
class Business(models.Model):
    # id
    caption = models.CharField(max_length=32)

#主机
class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(protocol="ipv4",db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey(to="Business", to_field='id')
# 10
#程序
class Application(models.Model):
    name = models.CharField(max_length=32,unique=True)
    r = models.ManyToManyField("Host")
