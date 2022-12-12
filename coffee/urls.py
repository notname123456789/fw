from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name = "home" ),
    path('basket' , views.bsk , name = 'basket'),
    path('like' , views.like , name = 'like'),


    path('coffee/' , views.cofee_page , name = 'coffee'),
    path('coffee/<int:pk>' , views.cofee_page , name = 'coffee'),
    
    
    path('liq/' , views.liq_page , name = 'liq'),
    path('liq/<int:pk>' , views.liq_page , name = 'liq'),
    

    path('presents/' , views.presents_page , name = 'presents'),
    path('presents/<int:pk>' , views.presents_page , name = 'presents'),
   

    path('tea/' , views.tea_page , name = 'tea'),
    path('tea/<int:pk>' , views.tea_page , name = 'tea'),
    

    path('sweets/' , views.sweets_page , name = 'sweets'),
    path('sweets/<int:pk>' , views.sweets_page , name = 'sweets'),
    
    path('coffee_dv/<int:pk>' , views.coffee_dv.as_view() , name = 'coffee_dv'),

    path ('ctg/<int:pk>/' , views.cat_page , name = 'category'),
]
