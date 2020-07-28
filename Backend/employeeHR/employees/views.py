from django.http import HttpResponse,HttpResponseRedirect
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status,viewsets,response
from rest_framework.decorators import api_view
from .serializers import deliverysideamount,placedDay,UserDay,placedMonthly,UserDayCart,EmployeeSerializer,retrievedata,retrievedaydata,retrievericedata,LoginSerializer,adminretrievedata,getprofilename,Usermonthly
from .models import Place_order_Day,deliverySide,Place_order_Monthly,Usermonthlycart,UserRegisterWithPK,categories,Admin,daycart,Login,userregister,deliveryboyregister,oils,breakfast,cooldrink,dryfruits,detergent,homecleaners,kitchencleaners,liquiddetergents,masalas,rice,snacks,syrups,monthlcart,daycart,setname
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect,render
from django.contrib import messages
from django.urls import reverse
# Create your views here.

#Employee Registeration GET, POST
baseurl="http://localhost:4200/"
@api_view(['GET','POST'])
@csrf_exempt
def Emp_Register(request):
    print("enter register in backend")
    print(request)
    if request.method == 'POST':
        print("======EMPLOYEE REGISTER======")
        # request.header = {'Access-Control-Allow-Origin': '*'}
        employee_register = JSONParser().parse(request)
        print(employee_register)
        _obj = Admin.objects.create(shopname=employee_register.get('shopname'),firstname=employee_register.get('firstname'), e_mail=employee_register.get('e_mail'),
                                area=employee_register.get('area'), city=employee_register.get('city'),
                                password=employee_register.get('password'),mobilenumber=employee_register.get('mobilenumber'))
        data = Admin.objects.all()
        #retreive= EmployeeSerializer(data,many=True)

        for d in data:
          print (d)
        #return JsonResponse(retreive,safe=False)
       
          
def employeelogin(request):
    if request.method == 'POST':
      employee_register = JSONParser().parse(request)
      print(employee_register)
      obj = Admin.objects.all()
      
      for i in obj:
        if i.e_mail==employee_register.get('e_mail') and i.password==employee_register.get('password'):
          print(i.firstname)
          print(i.password)
          print(i.e_mail)
          #setname1(name)
          return JsonResponse(i.shopname,safe=False)
        
@api_view(['GET','POST'])
@csrf_exempt




def delivery_Register(request):
    print("enter register in backend")
    print(request)
    if request.method == 'POST':
        print("======EMPLOYEE REGISTER======")
        # request.header = {'Access-Control-Allow-Origin': '*'}
        employee_register = JSONParser().parse(request)
        print(employee_register)
        # {'firstname': 'GORJILLI AKHIL', 'Area': 'ddah', 'City': 'dfdfj', 'Mobilenumber': 'dfhj', 'Password': 'sdjfhaj', 'User': 'jfdhsa'}
        
        _obj = deliveryboyregister.objects.create(firstname=employee_register.get('firstname'), e_mail=employee_register.get('e_mail'),
                                area=employee_register.get('area'), city=employee_register.get('city'),
                                password=employee_register.get('password'),mobilenumber=employee_register.get('mobilenumber'))
        print ('---------------------------------adaad')
        data = deliveryboyregister.objects.all()
        print(data)
        print ('---------------------------------adaa1111d')
        for d in data:
          print (d)

def delivery_Login(request):
   if request.method == 'POST':
      employee_register = JSONParser().parse(request)
      print(employee_register)
      obj = deliveryboyregister.objects.all()
      for i in obj:
        if i.e_mail==employee_register.get('e_mail') and i.password==employee_register.get('password'):
          print(i.firstname)
          print(i.password)
          print(i.e_mail)
          #setname1(name)
          return JsonResponse(i.firstname,safe=False)

def user_Register(request):
  print("enter register in backend")
  print(request)
  if request.method == 'POST':
      print("======User REGISTER======")
      # request.header = {'Access-Control-Allow-Origin': '*'}
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = UserRegisterWithPK.objects.create(firstname=employee_register.get('firstname'), e_mail=employee_register.get('e_mail'),
                              area=employee_register.get('area'), city=employee_register.get('city'),
                              password=employee_register.get('password'),mobilenumber=employee_register.get('mobilenumber'))
      return HttpResponse(_obj)

def user_login(request):
     if request.method == 'POST':
      employee_register = JSONParser().parse(request)
      print(employee_register)
      obj = UserRegisterWithPK.objects.all()
      for i in obj:
        if i.e_mail==employee_register.get('e_mail') and i.password==employee_register.get('password'):
          print(i.firstname)
          print(i.password)
          print(i.e_mail)
          #setname1(name)
          return JsonResponse(i.firstname,safe=False)

def getallshops(request):
  print(request)
  if request.method == 'GET':
    # employee_register = JSONParser().parse(request)
    # print(employee_register)
    obj = Admin.objects.all()
    retreive= EmployeeSerializer(obj,many=True)
    for i in obj:
      print(i.shopname)
      print(i.firstname)
      print(i.mobilenumber)
      print(i.area)
      print(i.city)
    print (obj)
    return JsonResponse(retreive.data,safe=False)
def getrequests(request):
  print(request)
  if request.method == 'GET':
    # employee_register = JSONParser().parse(request)
    # print(employee_register)
    obj = deliverySide.objects.all()
    retreive= deliverysideamount(obj,many=True)
    for i in obj:
      print(i.customername)
      print(i.amount)
    print (obj)
    return JsonResponse(retreive.data,safe=False)

def getdetails(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into admin retrieve data")
  duplicate1=employee_register['shopname']
  print(duplicate1)
  print(request)
  if request.method == 'POST':
    obj = Place_order_Monthly.objects.filter(customername=duplicate1)
    retreive= placedMonthly(obj,many=True)
    obj1 = Admin.objects.filter(shopname=obj.shopname)
    retreive1= EmployeeSerializer(obj,many=True)

    print (obj)
    return JsonResponse(retreive1.data,safe=False)

def get_admin_monthlyorders(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into admin retrieve data")
  duplicate1=employee_register['duplicate']
  print(request)
  if request.method == 'POST':
    obj = Place_order_Monthly.objects.filter(shopname=duplicate1)
    retreive= placedMonthly(obj,many=True)
    print (obj)
    return JsonResponse(retreive.data,safe=False)

def get_admin_dayorders(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into admin retrieve data")
  duplicate1=employee_register['duplicate']
  print(request)
  if request.method == 'POST':
    obj = Place_order_Day.objects.filter(shopname=duplicate1)
    retreive= placedDay(obj,many=True)
    print (obj)
    return JsonResponse(retreive.data,safe=False)


def get_admin_allrequests(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into admin requests data")
  duplicate1=employee_register['duplicate']
  print(request)
  if request.method == 'POST':
    obj = Place_order_Monthly.objects.filter(shopname=duplicate1)
    retreive= placedMonthly(obj,many=True)
    print (obj)
    return JsonResponse(retreive.data,safe=False)



def placed_monthlyCart(request):
  print("enter monthly in backend")
  print(request)
  if request.method == 'POST':
     
      # request.header = {'Access-Control-Allow-Origin': '*'}
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = Place_order_Monthly.objects.create(servicetype=employee_register.get('servicetype'),shopname=employee_register.get('shopownername'),customername=employee_register.get('firstname'), price=employee_register.get('price'),
                              brand=employee_register.get('brand'), quantity=employee_register.get('quantity'),
                              productname=employee_register.get('productname'))
      return HttpResponse(_obj)

def placed_DayCart(request):
  print("enter monthly in backend")
  print(request)
  if request.method == 'POST':
      # request.header = {'Access-Control-Allow-Origin': '*'}
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = Place_order_Day.objects.create(servicetype=employee_register.get('servicetype'),shopname=employee_register.get('shopownername'),customername=employee_register.get('firstname'), price=employee_register.get('price'),
                              brand=employee_register.get('brand'), quantity=employee_register.get('quantity'),
                              productname=employee_register.get('productname'))
      return HttpResponse(_obj)
  
def get_placedMonthly(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into admin retrieve data")
  duplicate1=employee_register['duplicate']
  print(request)
  if request.method == 'POST':
    obj = Place_order_Monthly.objects.filter(customername=duplicate1)
    retreive= placedMonthly(obj,many=True)
    # for i in obj:
    #   print(i.shopname)
    #   print(i.servicetype)
    #   print(i.customername)
    #   print(i.productname)
    #   print(i.brand)
    #   print(i.quantity)
    print (obj)
    return JsonResponse(retreive.data,safe=False)
  
def get_placedDay(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into user daycart retrieve data")
  duplicate1=employee_register['duplicate']
  print(request)
  if request.method == 'POST':
    obj = Place_order_Day.objects.filter(customername=duplicate1)
    retreive= placedDay(obj,many=True)
    # for i in obj:
    #   print(i.shopname)
    #   print(i.servicetype)
    #   print(i.customername)
    #   print(i.productname)
    #   print(i.brand)
    #   print(i.quantity)
    print (obj)
    return JsonResponse(retreive.data,safe=False)

def Monthlypayment(request):
  i=0
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into monthlypayment")
  duplicate1=employee_register['firstname']
  price=employee_register['price']
  print(duplicate1)
  print(price)
  print(request)
  if request.method == "POST":
    print("enter into post method")
    obj=deliverySide.objects.all()
    for i in obj:
      print(i.customername)
      if i.customername==duplicate1:
        print(i.amount)
        j=1
        i.amount = price
    if j==0:
      _obj = deliverySide.objects.create(customername=duplicate1,amount=price)
    j=0
    return HttpResponse(_obj)

def oils1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = oils.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

def breakfast1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = breakfast.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

def cooldrink1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = cooldrink.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

def dryfruits1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = dryfruits.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

def detergent1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = detergent.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

def homecleaners1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = homecleaners.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))
            
def kitchencleaners1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = kitchencleaners.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))
                          


def liquiddetergents1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = liquiddetergents.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))


def masalas1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = masalas.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))


def rice1(request):
  print(request)
  if request.method == 'POST':
    print("enter into rice")
     # print("======oil add======")
      
    employee_register = JSONParser().parse(request)
    print(employee_register)
    _obj = categories.objects.create(productname=employee_register.get('productname'),category=employee_register.get('category'), brand=employee_register.get('brand'),
                            quantity=employee_register.get('quantity'), price=employee_register.get('price'),shopname=employee_register.get('shopname'))

def snacks1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = snacks.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))


def syrups1(request):
  print(request)
  if request.method == 'POST':
     # print("======oil add======")
      
      employee_register = JSONParser().parse(request)
      print(employee_register)
      _obj = syrups.objects.create(productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))

@api_view(['GET'])
@csrf_exempt
def syrups2(request,productname):
    hr_home = syrups.objects.get(productname=productname)
    if request.method == 'GET':
        print("=============syrups INFO GET=============")
       # hr_home_serializer = HomeInfoSerializer(hr_home)
        return JsonResponse(hr_home_serializer.data)

def products():
 #return rice.objects.getall()
 print("hai")

def getallriceproducts(request):
  print("enter into monthly retrieve data")
  if request.method == 'GET':
    obj = rice.objects.all()
    retreive= retrievericedata(obj,many=True)
    for i in obj:
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    print (obj)
    return JsonResponse(retreive.data,safe=False)



def addmonthlycart(request):
   print(request)
   print("hai")
   if request.method == 'POST':
    # print("======oil add======")
    employee_register = JSONParser().parse(request)
    print(employee_register)
    obj = Usermonthlycart.objects.create(Username=employee_register.get('firstname'),productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))
    for i in obj:
      print(i.Username)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    print(obj)
    return obj

def adddaycart(request):
   print(request)
   print("hai")
   if request.method == 'POST':
    # print("======oil add======")
    employee_register = JSONParser().parse(request)
    print(employee_register)
    obj = UserDayCart.objects.create(Username=employee_register.get('firstname'),productname=employee_register.get('productname'), brand=employee_register.get('brand'),
                              quantity=employee_register.get('quantity'), price=employee_register.get('price'))
   
    return obj


def retrieve_daycart(request):
  if request.method=="POST":
    print(request)
    employee_register = JSONParser().parse(request)
    print(employee_register)
    print("enter into user retrieve day cart")
    duplicate1=employee_register['duplicate']
    print(duplicate1)
    if request.method == 'POST':
      obj = UserDayCart.objects.filter(Username=duplicate1)
      retreive= UserDay(obj,many=True)
      print(retreive.data)
      print(type(retreive))
      print(obj)
      for i in obj:
        print(i.Username)
        print(i.productname)
        print(i.brand)
        print(i.quantity)
        print(i.price)
      return JsonResponse(retreive.data,safe=False)
    else:
      print("else")

def retrieve_monthlycart(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  print("enter into user retrieve monthly cart data")
  duplicate1=employee_register['duplicate']
  print(duplicate1)
  if request.method == 'POST':
    obj = Usermonthlycart.objects.filter(Username=duplicate1)
    retreive= Usermonthly(obj,many=True)
    print(obj)
    for i in obj:
      print(i.id)
      print(i.Username)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)

def delete_monthlyCart(request):
  employee_register = JSONParser().parse(request)
  id=employee_register['id']
  print(id)
  print(employee_register)
  print("enter into delete monthly cart data")
 #print(duplicate1)
  if request.method == 'POST':
    obj = Usermonthlycart.objects.get(id=id)
    obj.delete()
    
def delete_DayCart(request):
  employee_register = JSONParser().parse(request)
  id=employee_register['id']
  print(id)
  print(employee_register)
  print("enter into delete monthly cart data")
  if request.method == 'POST':
    obj = UserDayCart.objects.get(id=id)
    obj.delete()

def delete_vendorCart(request):
  employee_register = JSONParser().parse(request)
  id=employee_register['id']
  print(id)
  print(employee_register)
  print("enter into delete vendor cart")
  if request.method == 'POST':
    obj = categories.objects.get(id=id)
    obj.delete()

def admin_rice_retrieve(request):
  print("enter into admin rice retrieve data")
  if request.method == 'GET':
    obj = categories.objects.filter(category='rice')
    retreive= adminretrievedata(obj,many=True)
    print(obj)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)

def user_rice_retrieve(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  duplicate1=employee_register['duplicate']
  product1=employee_register['product']
  print("enter into admin retrieve data")
  if request.method == 'POST':
    obj = categories.objects.filter(category=product1) & categories.objects.filter(shopname=duplicate1)
    retreive= adminretrievedata(obj,many=True)
    print(obj)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)


def admin_oil_retrieve(request):
  print("enter into admin retrieve data")
  if request.method == 'GET':
    obj = categories.objects.filter(category='oil')
    retreive= adminretrievedata(obj,many=True)
    print(obj)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)

def admin_individual_retrieve(request):
  employee_register = JSONParser().parse(request)
  print(employee_register)
  duplicate1=employee_register['duplicate']
  product1=employee_register['product']
  print("enter into admin retrieve data")
  if request.method == 'POST':
    print(request)
    print(duplicate1)
    print(product1)
    obj=categories.objects.filter(category=product1) & categories.objects.filter(shopname=duplicate1)
    retreive= adminretrievedata(obj,many=True)

    print(obj)
    #print(obj1)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)

def setname1(name):
    print(name)
    _obj = setname.objects.create(name=name)
    #//_obj = setname.objects.get(name='akhil')
    #_obj.delete()

def profilenameget1(request):
  print("enter into profilenameget")
  # data = [{'name': 'akhil'}]
  # return JsonResponse(data, safe=False)
  if request.method=="GET":
    obj = setname.objects.all()
    #data=[{'name':obj.name}]
    #retreive1= getprofilename(obj,many=True)
    print(obj)
    #return JsonResponse(data, safe=False)
    #return JsonResponse(retrieve1,safe=False)
    return HttpResponse(obj)


def admin_detergent_retrieve(request):
  print("enter into admin retrieve data")
  if request.get == 'GET':
    obj = categories.objects.filter(category='detergent')
    retreive= adminretrievedata(obj,many=True)
    print(obj)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)

def admin_cooldrinks_retrieve(request):
  print("enter into admin retrieve data")
  if request.method == 'GET':
    obj = categories.objects.filter(category='cooldrinks')
    retreive= adminretrievedata(obj,many=True)
    print(obj)
    for i in obj:
      print(i.shopname)
      print(i.category)
      print(i.productname)
      print(i.brand)
      print(i.quantity)
      print(i.price)
    return JsonResponse(retreive.data,safe=False)






