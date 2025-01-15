from django.contrib import admin

from Ecomsite.models import Product, Order

# Register your models here.
admin.site.site_header= 'Ecomsite'
admin.site.index_title = "Mange Ecomsite"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        self.change_category_to_default.short_description = 'Default Category'
    list_display = ('title','price','discount_price','category','description','image')
    search_fields = ('title',)
    fields = ('title',)
    list_editable = ('price','category',)





admin.site.register(Product,ProductAdmin)
admin.site.register(Order)