from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import * 
from django.forms.models import model_to_dict
from django.shortcuts import *
import datetime
from smsaero import SmsAero
from pprint import pprint
from django.core.mail import send_mail
from django.contrib.auth.models import User
#from settings import EMAIL_HOST_USER
now = datetime.datetime.now()
import random
from .forms import order_f
from .forms import code_f
from .forms import Reg_f
from django.conf import settings
#глобальные переменные - не трогать
chek = True
alarma = False
#функции:
#функция отправки сообщения
user_to_send =[]
def send (x , y):
      send_mail (
          'ARABICA',
          y,
          settings.DEFAULT_FROM_EMAIL,
          x,
          fail_silently=False ,          
      )
#функция корзины
bsk_data = {} ;
def basket_mech (x):
# t = list(d.items())
# scones["Вишня"] = 10
    global chek
    if x.session.get('bas') is None:
        x.session['bas'] = {}
        print("session reset , try again")

    ID = x.POST.get ('to_basket');
    QW = x.POST.get ('quantity');
    if 'to_basket' in x.POST:          
        for el in product.objects.all() :
            if int(ID) == int (el.id) :

                if int(x.POST['quantity']) > int(el.amount):
                    global alarma; alarma = True
                    return redirect ('coffee/cof.html')

                if x.session['bas'] != None :
                    bsk_data = x.session['bas']
                if el.id in bsk_data:
                    bsk_data[el.id] = x.POST['quantity'] 
                    print("=)"); chek = False
                if str(el.id) in bsk_data:
                    bsk_data[str(el.id)] = x.POST['quantity']
                    x.session['bas'] = bsk_data
                    print("=)"); chek = False
                if chek :
                    bsk_data[int(el.id)] = x.POST['quantity']
                    x.session['bas'] = bsk_data
                    print(x.session['bas'])
                chek = True


#_________________________________________________#
    ID = x.POST.get ('delete_from_basket');
    if 'delete_from_basket' in x.POST:
        for el in product.objects.all() :
            if int(ID) == int (el.id) : 
                if x.session['bas'] != None :
                    bsk_data = x.session['bas']
                print(bsk_data , "--->" , el.id)
                bsk_data.pop(str(el.id) , None)
                x.session['bas'] = bsk_data
#функция лайка
like_data = [];
def like_mech (x):
    if x.session.get('fav') is None:
        x.session['fav'] = []
        print("session reset , try again")

    ID = x.POST.get ('to_like');
    if 'to_like' in x.POST:          
        for el in product.objects.all() :
            if int(ID) == int (el.id) :
                if x.session['fav'] != None :
                    like_data = x.session['fav']
                if not(str(el.id) in str(x.session.get('fav'))):
                    print("аххахаха")
                    like_data.append(el.id)
                    x.session['fav'] = like_data

    ID = x.POST.get ('delete_from_like');
    if 'delete_from_like' in x.POST:
        for el in product.objects.all() :
            if int(ID) == int (el.id) : 
                if x.session['fav'] != None :
                    like_data = x.session['fav']
                print(like_data , "--->" , el.id)
                like_data.remove(el.id)
                x.session['fav'] = like_data
#функция покупки
order_form_onsite = order_f()
code_form_onsite = code_f()
Reg_f_form = Reg_f()
def buy(x):
    mess_to_send = ""
    full_price = 0;
    new_order = order();
    #user_who_send = email_host.objects.all()
    if x.method == 'POST':        
        if 'confirm_code' in x.POST:
            code_form_onsite = code_f(x.POST)
            print("".join(map(str,x.session['cod'])) , "--->" , x.POST['CODE'])
            #--
            if x.POST['CODE'] == "".join(map(str,x.session['cod'])):
                users_list = User.objects.all()
                for el_2 in users_list:
                    if el_2.is_superuser:
                        global user_to_send; user_to_send.append(str(el_2.email))
                #___________формирование сообщения заказа____________
                for el in product.objects.all() :
                    if str(el.id) in x.session.get('bas').keys():
                        mess_to_send += str(el.name) + "-по цене:" + str(el.price) + "\n"
                        full_price+=int(el.price)
                mess_to_send += "\n" + str(full_price) + "\n" + str(x.session.get('pho')) + "   " + str(x.session.get('adr'))
                #___________формирование сообщения заказа____________
                print(user_to_send); send(user_to_send , mess_to_send) 
                print(x.session.get('bas'))#вместо этого отправляем заказ на почту и сохраняем в базе
                new_order.phone = str(x.session.get('pho'))
                new_order.adress = str(x.session.get('adr'))
                new_order.desc = mess_to_send
                new_order.save();
                for el in product.objects.all():
                    if str(el.id) in x.session.get('bas').keys():
                        new_order.products.add(el);
                print(new_order.products)

        if 'send_code' in x.POST:
            order_form_onsite = order_f(x.POST)
            x.session['adr'] = x.POST['adress']
            x.session['pho'] = x.POST['phone']
            random.seed(now.microsecond)
            four = []; four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));four.append (int(random.randrange(0 , 9)));
            x.session['cod'] = []
            x.session['cod'] = four

            #api = SmsAero('arabicatest7@gmail.com', 'WXEEtMZ2ZT3XHJhEJJOhyaEcCZ7U') !!!!!!!!!!!
            #print(api.send(str(x.session.get('pho')) , str(x.session.get('cod')))) !!!!!!!!!!!!!

            print(x.session['cod'])#сюда высылка кода

        order_form_onsite = order_f()
# не забудь сбросить код к None

def home (x):
    #for el in order.objects.all():
        #print(el.products.all())
    foot = footer_content.objects.all()
    ctg_on_site = ctg.objects.all()
    product_on_site = product.objects.filter(amount__gte=50).filter(dis_discount=True).order_by('?')[:3]

    return render (x , 'coffee/home.html' , {'foot' : foot , 'ctg_on_site' : ctg_on_site ,'product_on_site' :product_on_site})

def cofee_page(x, pk):
    amount = 10;
    page = Paginator(cof.objects.all() , amount).page(pk)
    ran = Paginator(cof.objects.all() , amount).page_range
    product_on_site = cof.objects.order_by('price')
    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    #________________________________________________#
    for el in order.objects.all():
        print(el.products.all())
    foot = footer_content.objects.all()
    #________________________________________________#
    ctg_on_site = ctg.objects.all()
    return render (x , 'coffee/cof.html' ,
                 {
                'product_on_site' : product_on_site,
                'ctg_on_site' : ctg_on_site ,
                'foot' : foot ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })
def liq_page(x, pk):
    amount = 10;
    page = Paginator(liq.objects.all() , amount).page(pk)
    ran = Paginator(liq.objects.all() , amount).page_range
    product_on_site = liq.objects.order_by('price')
    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    #________________________________________________#
    for el in order.objects.all():
       print(el.products.all())
    foot = footer_content.objects.all()
    #________________________________________________#
    ctg_on_site = ctg.objects.all()
    return render (x , 'coffee/cof.html' ,
                 {
                'foot' : foot ,
                'product_on_site' : product_on_site,
                'ctg_on_site' : ctg_on_site ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })
def presents_page(x, pk):
    amount = 10;
    page = Paginator(presents.objects.all() , amount).page(pk)
    ran = Paginator(presents.objects.all() , amount).page_range
    product_on_site = presents.objects.order_by('price')
    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    #________________________________________________#
    ctg_on_site = ctg.objects.all()
    foot = footer_content.objects.all()
    return render (x , 'coffee/cof.html' ,
                 {
                'foot' : foot ,
                'product_on_site' : product_on_site,
                'ctg_on_site' : ctg_on_site ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })
def tea_page(x, pk):
    amount = 10;
    page = Paginator(tea.objects.all() , amount).page(pk)
    ran = Paginator(tea.objects.all() , amount).page_range
    product_on_site = tea.objects.order_by('price')
    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    #________________________________________________#
    ctg_on_site = ctg.objects.all()
    foot = footer_content.objects.all()
    return render (x , 'coffee/cof.html' ,
                 {
                'foot' : foot ,
                'product_on_site' : product_on_site,
                'ctg_on_site' : ctg_on_site ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })
def sweets_page(x, pk):
    amount = 10;
    page = Paginator(sweets.objects.all() , amount).page(pk)
    ran = Paginator(sweets.objects.all() , amount).page_range
    product_on_site = sweets.objects.order_by('price')
    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    #________________________________________________#
    ctg_on_site = ctg.objects.all()
    foot = footer_content.objects.all()
    return render (x , 'coffee/cof.html' ,
                 {
                'foot' : foot ,
                'product_on_site' : product_on_site,
                'ctg_on_site' : ctg_on_site ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })
#___________________________basket________________________________#
def bsk (x):

    bsk_data_now = []
    for el in product.objects.all():
        if x.session.get('bas') != None:
            for mel in list(x.session.get('bas').keys()):
                if (str(el.id) == mel):
                    bsk_data_now.append(el)
    buy(x);
    foot = footer_content.objects.all()
    return render (x , 'coffee/basket.html' , {'foot' : foot ,'pib' : bsk_data_now ,'Reg': Reg_f_form, 'buy_out' : order_form_onsite ,'code_out' : code_form_onsite})
#___________________________basket________________________________#

def like (x):

    like_data_now = []
    for el in product.objects.all():
        if x.session.get('fav') != None:
            for mel in x.session.get('fav'):
                if (el.id == mel):
                    like_data_now.append(el)             
    foot = footer_content.objects.all()
    return render (x , 'coffee/like.html' , {'foot' : foot , 'pib' : like_data_now})

class coffee_dv (DetailView):
    model = product
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
def cat_page(x , pk):    

    product_on_site = another_product.objects.filter(cat = pk)
    amount = 10;
    page = Paginator(product_on_site , amount).page(pk)
    ran = Paginator(product_on_site , amount).page_range

    #________________________________________________#
    basket_mech(x);
    like_mech(x);
    #________________________________________________#
    #t = list(d.keys())
    #b_data = ""
    print(x.session.get('bas'))
    s_data = x.session.get('fav')
    b_data = list(x.session.get('bas').keys()); b_data = [int(item) for item in b_data]
    b_data_gramm = x.session.get('bas'); 
    print("like ---->", s_data)
    print("keys ---->" , b_data)
    print("something---->" , b_data_gramm)
    foot = footer_content.objects.all()
    return render (x, 'coffee/cof.html' , 
                {
                'foot' : foot ,
                'product_on_site' : product_on_site ,
                'amount': ran ,
                's_data' : s_data ,
                'b_data' : b_data ,
                'b_data_gramm' : b_data_gramm ,
                'alarma' : alarma
                })


# Create your views here.
'''

    for el in cof.objects.order_by('price'):
        print("----->" , el.name , "<--->" , el.base_cat)
        

    print("____________________")

    for el in product.objects.all() :
        print("----->" , el.name , "<--->" , el.base_cat)

class coffee_dv (DetailView):
    model = cof
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
class liq_dv (DetailView):
    model = liq
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
class presents_dv (DetailView):
    model = presents
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
class tea_dv (DetailView):
    model = tea
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
class sweets_dv (DetailView):
    model = sweets
    template_name = 'coffee/coffee_dv.html'
    context_object_name = 'el'
'''