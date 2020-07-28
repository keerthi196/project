from django.conf.urls import url
from django.urls import path
from .views import getdetails,get_admin_dayorders,get_admin_allrequests,get_admin_monthlyorders,getrequests,delete_vendorCart,delete_DayCart,placed_DayCart,delivery_Login,get_placedDay,Monthlypayment,profilenameget1,adddaycart,Emp_Register,user_Register,employeelogin,delivery_Register,oils1,breakfast1,cooldrink1,dryfruits1,detergent1,homecleaners1,kitchencleaners1,liquiddetergents1,masalas1,rice1,snacks1,syrups1,user_login,addmonthlycart,retrieve_monthlycart,retrieve_daycart,getallriceproducts,admin_rice_retrieve,admin_oil_retrieve,admin_detergent_retrieve,admin_cooldrinks_retrieve,setname1,getallshops,admin_individual_retrieve,user_rice_retrieve,delete_monthlyCart,placed_monthlyCart,get_placedMonthly


urlpatterns = [

    #Employee Login GET
    url(r'^employees/login/$', employeelogin),

    #Employee Register POST
    url(r'^employees/register/$', Emp_Register),

    #Employee monthlyorders POST
    url(r'^employees/retrieve_admin_MonthlyOrders/$', get_admin_monthlyorders),

    #Employee orders POST
    url(r'^employees/retrieve_admin_DayOrders/$', get_admin_dayorders),

    #Employee orders POST
    url(r'^employees/retrieve_admin_allrequests/$', get_admin_allrequests),

    #Employee orders amounts POST
    url(r'^employees/getallrequestsamounts/$', getrequests),

    #delivery Register POST
    url(r'^delivery/deliveryregister/$', delivery_Register),

    #delivery login POST
    url(r'^delivery/LoginDeliveryBoy/$', delivery_Login),

    #delivery getrequests
    url(r'^delivery/getallrequests/$', getrequests),

    #delivery getrequests
    url(r'^delivery/getalldetails/$', getdetails),



    #user register
    url(r'^user/register/$',user_Register),

    #user login
    url(r'^user/login/$',user_login),

    #user add monthly products
    url(r'^user/addmonthly/$',addmonthlycart),

        #user add monthly products
    url(r'^user/addday/$',adddaycart),

    #user add monthly products
    url(r'^user/deletemonthly/$',delete_monthlyCart),

    #user add day products
    url(r'^user/deleteDay/$',delete_DayCart),

     #delete vendor prodcts
    url(r'^user/deleteVendor/$',delete_vendorCart),

    #user placed monthly products
    url(r'^user/placedMonthly/$',placed_monthlyCart),

    #user placed Day products
    url(r'^user/placedDay/$',placed_DayCart),

    #user placed monthly products
    url(r'^user/RetrievePlacedMonthly1/$',get_placedMonthly),

    #user placed monthly products
    url(r'^user/RetrievePlacedDay/$',get_placedDay),

        #user placed monthly products
    url(r'^user/MonthlyPayment/$',Monthlypayment),

    #user retrieve monthly products
    url(r'^user/retrievemonthly1/$',retrieve_monthlycart),
   

    #user retrieve monthly products
    url(r'^user/retrieveday1/$',retrieve_daycart),

    #user retrieve all rice products
    url(r'^user/getallproducts/$',getallriceproducts),

    #admin retrieve admin products
    url(r'^employees/retrieve_adminrice_data/$',admin_rice_retrieve),

    #admin retrieve admin products
    url(r'^employees/retrieve_adminoil_data/$',admin_oil_retrieve),

    #admin retrieve admin products
    url(r'^employees/retrieve_admindryfruits_data/$',admin_individual_retrieve),

    #admin retrieve admin products
    url(r'^employees/retrieve_admindetergent_data/$',admin_detergent_retrieve),

     #admin retrieve admin products
    url(r'^employees/retrieve_admincooldrinks_data/$',admin_cooldrinks_retrieve),

    #admin retrieve admin products
    #url(r'^employees/retrieve_adminmasalas_data/$',),

    #admin setprofile name
    url(r'^employees/setname2/$',setname1),

    #admin setprofile name
    url(r'^employees/profilenameget/$',profilenameget1),

    #admin  get all shops in user
    url(r'^user/getallshops/$',getallshops),

    #admin retrieve user products
    url(r'^user/getproducts/$',user_rice_retrieve),



     #admin shops identity name
    #url(r'^user/shopidentity/$',shopidentity),

    #vendor products
    url(r'^add/oils/$',oils1),
    url(r'^add/breakfast/$',breakfast1),
    url(r'^add/drinks/$',cooldrink1),
    url(r'^add/dryfruits/$',dryfruits1),
    url(r'^add/detergent/$',detergent1),
    url(r'^add/homecleaners/$',homecleaners1),
    url(r'^add/kitchencleaners/$',kitchencleaners1),
    url(r'^add/liquiddetergents/$',liquiddetergents1),
    url(r'^add/masalas/$',masalas1),
    url(r'^add/rice/$',rice1),
    url(r'^add/snacks/$',snacks1),
    url(r'^add/syrups/$',syrups1),
]