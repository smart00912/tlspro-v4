from django.shortcuts import render ,HttpResponse,render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.template import Context

# Create your views here.


#def login(q):
#	html='<h1>test</h1>'
#	return HttpResponse(html)

def showdate(q,year,month,day,home):
	return HttpResponse(year+'-'+month+'-'+day+'====='+home)

def index(q):
	info={'name':'sean.li','age':33,'gender':'Male'}
	return render_to_response('index.html',{'content':'string from views','info':info})



def bootstrap(q):
	return render(q,'bootstrap.html')

def asset(q):
	return render(q,'asset.html')

def host(q):
	#print q.path
	return render(q,'host.html')

def audit(q):
	return render(q,'audit.html')

def user(q):
	return render(q, 'host.html')

def login(request):
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
			user=authenticate(username=email.split('@')[0],password=password)              #take first part from email as username
			if user is not None:
				if user.is_active:
					return HttpResponseRedirect('/dashboard/')
				else:
					errors.append('Account disabled')
			else:
				errors.append('Invaild user')
		return render(request,'login.html',{'errors':errors})       #render will avoid csrf error
	else:		
		return render(request,'login.html')
