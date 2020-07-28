from rest_framework import serializers
from .models import deliverySide,Place_order_Day,Place_order_Monthly,UserRegisterWithPK,Admin,rice,Login,userregister,deliveryboyregister,monthlcart,daycart,categories,setname,Usermonthlycart,UserDayCart

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = ('__all__')   
    
class userregisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegisterWithPK
        fields=('__all__')
    fields=('firstname','e_mail','password','mobilenumber','area','city')

class Usermonthly(serializers.ModelSerializer):
    class Meta:
        model = Usermonthlycart
        fields =('id','Username','productname','brand','quantity','price')

class UserDay(serializers.ModelSerializer):
    class Meta:
        model = UserDayCart
        fields =('id','Username','productname','brand','quantity','price')

class retrievedata(serializers.ModelSerializer):
    class Meta:
        model=monthlcart
        fields=('productname','brand','quantity','price')

class placedMonthly(serializers.ModelSerializer):
    class Meta:
        model=Place_order_Monthly
        fields=('servicetype','shopname','customername','productname','brand','quantity','price')

class placedDay(serializers.ModelSerializer):
    class Meta:
        model=Place_order_Day
        fields=('servicetype','shopname','customername','productname','brand','quantity','price')


class adminretrievedata(serializers.ModelSerializer):
    class Meta:
        model=categories
        fields=('id','shopname','category','productname','brand','quantity','price')

class deliverysideamount(serializers.ModelSerializer):
        class Meta:
            model=deliverySide
            fields=('customername','amount')

class retrievericedata(serializers.ModelSerializer):
    class Meta:
        model=rice
        fields=('productname','brand','quantity','price')

class retrievedaydata(serializers.ModelSerializer):
    class Meta:
        model=daycart
        fields=('productname','brand','quantity','price')

class profileset(serializers.ModelSerializer):
    class Meta:
        model=setname
        fields=('name')

class getprofilename():
    class Meta:
        model=setname
        fields=('name')

   

class deliveryboy_register(serializers.ModelSerializer):
    class Meta:
        model = deliveryboyregister
        fields=('__all__')
    def id_valid(self):
        return True

