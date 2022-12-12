from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models import IntegerField
from django.core.validators import MinLengthValidator
from django.conf import settings

#class host_emails(models.Model):
#   host_email = models.EmailField()
def changer(mail , ps):
    settings.EMAIL_HOST_USER = mail;
    settings.EMAIL_HOST_PASSWORD = ps;
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)

class email_host(models.Model):
    name = models.CharField("имя-константа", max_length=150 , db_index=True , default ='host_of_email')
    email = models.CharField("почта", max_length=150 , db_index=True)
    password = models.CharField("пароль", max_length=150 , db_index=True)
    a_password = models.CharField("пароль sms рассылки", max_length=150 , db_index=True , default ='пароль для рассылки смс')
    a_email = models.CharField("почта sms рассылки", max_length=150 , db_index=True , default ='почта для рассылки смс')
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("suka rabotat")
        changer(self.email , self.password)


class ctg (models.Model):
     name = models.CharField("Категория", max_length=150 , db_index=True)
     active = models.BooleanField(default = False)
     def get_absolute_url(self):
         return f'/ctg/{self.pk}/'     
     def __str__(self):
        return self.name
#     def __init__(self , NAME=name):
#        self.name = NAME
     class Meta:
         verbose_name = "Категория_внешней_фильтрации"
         verbose_name_plural = "Категории_внешней фильтрации"

class product(models.Model):
    name = models.CharField (max_length=200, default ='SOME_NAME_THERE')
    price = models.IntegerField(default ='999')
    amount = models.IntegerField(default ='0')
    desc = models.TextField('Сжатое описание' , blank = True)
    full_desc = models.TextField('Полное описание' , blank = True)
    image = models.ImageField(upload_to='static\media\img',  blank = True)
    base_cat = "default"
    discount = models.BooleanField('есть скидка' , default = False)
    dis_discount = models.BooleanField('на главную' , default = False)
    old_price = models.IntegerField('старая цена' , default ='999')
    #can_be_counted = models.BooleanField('в граммах или ед.' , default = False)
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        #print(self.base_cat)
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class regions(models.Model):
    name = models.CharField (max_length=200, default ='район')
    class Meta:
        verbose_name = 'районы доставки'
        verbose_name_plural = 'районы доставки'
    def __str__ (self):
       return self.name;
#__________________________________________________________________________________  .is_authenticated


class order (models.Model):
   phone = models.CharField(null=False, blank=False, max_length=12) #unique=True ,
   adress = models.TextField('адрес проживания' , blank = True)
   products = models.ManyToManyField(product)
   desc = models.TextField('описание' , blank = True)
   class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class code (models.Model):
    CODE = IntegerField(null=False, blank=False, unique=True , max_length=4 , validators=[MinLengthValidator(4)])
#__________________________________________________________________________________

class another_product (product): 
    cat = models.ForeignKey('ctg', on_delete=models.SET_NULL , null = True , blank = True )
    class Meta:
        verbose_name = 'Другие товары'
        verbose_name_plural = 'Другие товары'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class cof (product):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        product.base_cat = "cofee"
        cof.base_cat = "cofee" # они че блинб местами меняюься
    class Meta:
        verbose_name = 'кофе'
        verbose_name_plural = 'кофе'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class sweets (product):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        product.base_cat = "sweets"
        sweets.base_cat = "sweets" # они че блинб местами меняюься
    class Meta:
        verbose_name = 'конфеты'
        verbose_name_plural = 'конфеты'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class tea (product):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        product.base_cat = "tea"
        tea.base_cat = "tea" # они че блинб местами меняюься
    class Meta:
        verbose_name = 'чай'
        verbose_name_plural = 'чаи'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class presents (product):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        product.base_cat = "presents"
        presents.base_cat = "presents" # они че блинб местами меняюься
    class Meta:
        verbose_name = 'Подарочные набор'
        verbose_name_plural = 'Подарочные наборы'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class liq (product):
    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)
        product.base_cat = "liq"
        liq.base_cat = "liq" # они че блинб местами меняюься
    class Meta:
        verbose_name = 'Сироп'
        verbose_name_plural = 'Сиропы'
    def __str__ (self):
       return self.name + " " + str(self.price) + "р";

class footer_content (models.Model):
    adr = models.TextField('адреса' , blank = True)
    cont = models.TextField('контакты' , blank = True)
    t_1 = models.TextField('доп. текст №1' , blank = True)
    t_2 = models.TextField('доп. текст №2' , blank = True)
    class Meta:
        verbose_name = 'информация "подвала"'
        verbose_name_plural = 'информация "подвала"'
# Create your models here.
