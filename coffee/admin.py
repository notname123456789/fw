from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget

#_____________________________#
admin.site.register (product)
admin.site.register (ctg)
#_____________________________#

class cofr(resources.ModelResource):
    class Meta:
        model = cof
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class coffee(ImportExportModelAdmin):
    resource_classes = [cofr]
admin.site.register (cof , coffee)
#-----------------------------------#
class liqr(resources.ModelResource):
    class Meta:
        model = liq
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class liq_i(ImportExportModelAdmin):
    resource_classes = [liqr]
admin.site.register (liq , liq_i)
#-----------------------------------#
class presentsr(resources.ModelResource):
    class Meta:
        model = presents
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class presents_i(ImportExportModelAdmin):
    resource_classes = [presentsr]
admin.site.register (presents , presents_i)

#-----------------------------------#
class tear(resources.ModelResource):
    class Meta:
        model = tea
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class tea_i(ImportExportModelAdmin):
    resource_classes = [tear]
admin.site.register (tea , tea_i)

#-----------------------------------#
class sweetsr(resources.ModelResource):
    class Meta:
        model = sweets
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class sweets_i(ImportExportModelAdmin):
    resource_classes = [liqr]
admin.site.register (sweets , sweets_i)

#-----------------------------------#
class another_productr(resources.ModelResource):
    class Meta:
        model = another_product
        list_display = ('name', 'price', 'amount', 'desc', 'full_desc' , 'image')
        exclude = ('product_ptr')
class another_product_i(ImportExportModelAdmin):
    resource_classes = [another_productr]
admin.site.register (another_product , another_product_i)

admin.site.register(order)
admin.site.register(email_host)
admin.site.register(footer_content)
admin.site.register(regions)
# Register your models here.
