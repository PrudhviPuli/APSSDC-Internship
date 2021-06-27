from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good evening to All...")

def htmltag(req):
	return HttpResponse("<h2>Hi Welcome to the Bootcamp</h2>")

def usrprt(request,uname):
	return HttpResponse("<h2>Welcome <span style= 'color:green'>{}</span></h2>".format(uname))

def usrage(request,un,ag):
	return HttpResponse("<h3 style='text-align:center;background-color:green'> Name is <span style='color:yellow'>{}</span> and age is <span style = 'color:red'>{}</span></h3>".format(un,ag))

def empdet(request,eid,eage,ename):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Name is {} and your age is: {} , your id is: {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})
	
def emp(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/emp.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request): 
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method == "POST":
		#print(req.POST)
		uname = req.POST["uname"] #Method 1 to get the data 
		rollno = req.POST['rollno']
		email = req.POST.get('email') # Method 2 to get the data using .get
		#No difference btw Method 1 and 2, both serve the same purpose.
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'email':email}
		return render(req,'html/display.html',data)


	return render(req,'html/myform.html')

def registration(req):
	if req.method == "POST":
		firstname = req.POST["firstname"]
		lastname = req.POST["lastname"]
		email = req.POST["email"]
		phoneno = req.POST["phoneno"]
		gender = req.POST["gender"]
		address = req.POST["address"]
		language=req.POST.getlist('language')
		data = {'firstname':firstname,'lastname':lastname,'email':email,'phoneno':phoneno,'gender':gender,'address':address,'language':language}
		return render(req,'html/regdisplay.html',data)
	
	return render(req,'html/registration.html')
	

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')

def register1(request):
	# name = "siva"
	# email = "siva@gmail.com"
	reg = Register(name = "rasool",email="rasool@gmailcom")
	reg.save()
	return HttpResponse("row inserted successfully...")

def register2(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name, email = email)
		reg.save()
		return HttpResponse("Record inserted successfully....")
	return render(request,"html/register2.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	#return HttpResponse("Your Name is: {} and your email id is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})

