 # -*- coding:utf-8 -*- 
 
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import  User


class Host(models.Model):
	hostname=models.CharField(max_length=64,unique=True)
	ip_addr=models.GenericIPAddressField(unique=True)
	port = models.IntegerField(default=22)
	
	system_type_choose = (
		('centos','LINUX'),
		('win10','windows'),
	)
	
	system_type=models.CharField(choices=system_type_choose,max_length=32)
	idc=models.ForeignKey('IDC')
	groups=models.ManyToManyField('HostGroup')
	enabled =models.BooleanField(default=True)
	online_date=models.DateField()
	create_date=models.DateTimeField(auto_now_add=True)	
	def __unicode__(self):
		return self.hostname
	
	
class IDC(models.Model):
	name=models.CharField(max_length=64,unique=True)
	def __unicode__(self):
		return self.name
	
class HostGroup(models.Model):
	name = models.CharField(max_length=64,unique=True)
	def __unicode__(self):
		return self.name
	
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	name=models.CharField(max_length=64,unique=True)
	host_group=models.ManyToManyField('HostGroup',blank=True,null=True)
	hosts=models.ManyToManyField('Host',blank=True,null=True)
	
	def __unicode__(self):
		return self.name
	

class Upload(models.Model):
    username = models.CharField(max_length = 30,default='Unknow')
    phrase = models.CharField(max_length = 80,default='xxxxxxxxxx')
    headImg = models.FileField(upload_to = './upload/')
    create_date=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username

'''
CURD操作有两种方法：
第一种：
h=models.Host.objects.create(hostname='cnwebp01',ip_addr='10.10.91.2',port='9022',system_type='linux',idc_id=1,online_date=datetime.now())
all_groups=models.HostGroup.objects.all()
h.groups.add(*all_groups)

第二种：直接实例化HOST类然后save
de= models.Host(hostname='win',ip_addr='10.10.91.3',port='9022',system_type='win10',idc_id=1,online_date=datetime.now())
de.save()
'''