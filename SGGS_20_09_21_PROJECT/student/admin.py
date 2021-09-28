from django.contrib import admin
from django.utils.html import format_html
from .models import Country,City,Percentage

# admin.site.register(City)
# admin.site.register(Country)
# admin.site.register(Subject1)

class CountryAdmin(admin.ModelAdmin):

    list_display  = ['name']
    search_fields = ['name']

admin.site.register(Country,CountryAdmin)

class CityAdmin(admin.ModelAdmin):

    list_display  = ['Name','Country_field', 'Population', 'State', 'field', 'image_tag']
    # def name_colored(self, obj):
    #     if obj.are_you_Student:
    #         color_code = '00FF00'
    #     else:
    #         color_code = 'FF0000'

    #     html = '<span style="color: #{};">{}</span>'.format(color_code, obj.name)
    #     return format_html(html)
        
    # name_colored.Country_field = 'Name'
    # name_colored.short_description = 'Name'

    list_per_page = 10
    search_fields = ['name','population']
    readonly_fields = ['field']

admin.site.register(City,CityAdmin)

class PercentageAdmin(admin.ModelAdmin):

    list_per_page = 6
    list_display  = ['marks']
    search_fields = ['marks']

admin.site.register(Percentage,PercentageAdmin)

