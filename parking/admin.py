from django.contrib import admin
from .models import Tariff, TariffDetail


class TariffAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'end_date']

class TariffDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'hours', 'price', 'tariff']


admin.site.register(Tariff, TariffAdmin)
admin.site.register(TariffDetail, TariffDetailAdmin)

# Register your models here.
