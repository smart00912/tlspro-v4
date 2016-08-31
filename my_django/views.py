from django.shortcuts import render ,HttpResponse,render_to_response
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from my_django.models import Upload
from time import strftime,gmtime



# Create your views here.


#def login(q):
#	html='<h1>test</h1>'
#	return HttpResponse(html)

def showdate(q,year,month,day,home):
	return HttpResponse(year+'-'+month+'-'+day+'====='+home)

def index(q):
	info={'name':'sean.li','age':33,'gender':'Male'}
	return render_to_response('index.html',{'content':'string from views','info':info})


@login_required(login_url="/yunwei/",redirect_field_name='login')
def bootstrap(q):
	return render(q,'dashboard.html',{'debug':False})

@login_required(login_url="/yunwei/",redirect_field_name='login')
def asset(q):
	return render(q,'asset.html',{'debug':False})

@login_required(login_url="/yunwei/",redirect_field_name='login')
def host(request):
	#print q.path
	return render(request,'host.html',{'debug':False})

@login_required(login_url="/yunwei/",redirect_field_name='login')
def audit(q):
	return render(q,'audit.html',{'debug':False})

@login_required(login_url='/yunwei/',redirect_field_name='login',)
def user(q):
	return render(q, 'host.html',{'debug':False})

@login_required(login_url='/yunwei/',redirect_field_name='login',)
def syslog(q):
	return render(q, 'logs/system.html',{'debug':False})
@login_required(login_url='/yunwei/',redirect_field_name='login',)
def userlog(q):
	return render(q, 'logs/user.html',{'debug':False})
@login_required(login_url='/yunwei/',redirect_field_name='login',)
def adm(q):
	ud = Upload.objects.all()
	return render(q, 'admin/adm.html',{'debug':False,'ud':ud})


@login_required(login_url='/yunwei/',redirect_field_name='login',)
def upload(request):
	if request.method=='POST':
		f=request.FILES.get('uploadfile')
		pa=request.POST.get('phrase')
		filename='/'.join(('/home/sean/upload',f.name+strftime("%Y-%m-%d-%H:%M:%S", gmtime())))
		with open(filename,'a+') as keys:
			for chunk in f.chunks():
				keys.write(chunk)
		uf=Upload(username=request.user,headImg=filename,phrase=pa)
		uf.save()
		ud = Upload.objects.all()
		return render(request,'admin/adm.html',{'result':'ok','ud':ud})

def acc_login(request):
	errors=[]
	post_u=None
	post_p=None
	if  request.method=="POST":
		if not request.POST.get('u'):
			errors.append('Please Enter username')
		else:
			post_u= request.POST.get('u')
		if not request.POST.get('p'):
			errors.append('can not be empty password')
		else:
			post_p=request.POST.get('p')
		if post_u is not None and post_p is not None:
		#	acc_user=email.split('@')[0]
			user=authenticate(username=post_u,password=post_p)              #take first part from email as username
			if user is not None:
				if user.is_active:
					login(request,user)
					ud = Upload.objects.all()
					return HttpResponseRedirect(reverse('my_django:dashboard'))
				else:
					errors.append('Account disabled')
			else:
				errors.append('Invaild user')
		return render(request,'loginb.html',{'errors':errors})       #render will avoid csrf error
	else:		
		return render(request,'loginb.html')

def acc_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('my_django:login'))