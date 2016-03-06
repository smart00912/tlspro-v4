from django.shortcuts import render ,HttpResponse,render_to_response
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.template import Context
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

# Create your views here.


#def login(q):
#	html='<h1>test</h1>'
#	return HttpResponse(html)

def showdate(q,year,month,day,home):
	return HttpResponse(year+'-'+month+'-'+day+'====='+home)

def index(q):
	info={'name':'sean.li','age':33,'gender':'Male'}
	return render_to_response('index.html',{'content':'string from views','info':info})


@login_required(login_url='/',redirect_field_name='fuck')
def bootstrap(q):
	return render(q,'bootstrap.html',{'debug':False})

@login_required(login_url='/',redirect_field_name='fuck')
def asset(q):
	return render(q,'asset.html',{'debug':False})

@login_required(login_url='/',redirect_field_name='fuck')
def host(request):
	#print q.path
	return render(request,'host.html',{'debug':False})

@login_required(login_url='/',redirect_field_name='fuck')
def audit(q):
	return render(q,'audit.html',{'debug':False})

@login_required(login_url='/',redirect_field_name='fuck')
def user(q):
	return render(q, 'host.html',{'debug':False})


def acc_login(request):
	errors=[]
	email=None
	password=None
	if  request.method=="POST":
		if not request.POST.get('email'):
			errors.append('Please Enter email')
		else:
			email = request.POST.get('email')
		if not request.POST.get('password'):
			errors.append('can not be empty password')
		else:
			password=request.POST.get('password')
		if email is not None and password is not None:
			acc_user=email.split('@')[0]
			user=authenticate(username=acc_user,password=password)              #take first part from email as username
			if user is not None:
				if user.is_active:
					login(request,user)
					return HttpResponseRedirect(reverse('my_django:dashboard'))
				else:
					errors.append('Account disabled')
			else:
				errors.append('Invaild user')
		return render(request,'login.html',{'errors':errors})       #render will avoid csrf error
	else:		
		return render(request,'login.html')

def acc_logout(request):
	logout(request)
	return HttpResponseRedirect('/')