from django.contrib import admin

from .models import Ventas
# Register your models here.

class VentasAdmin(admin.ModelAdmin):
    icon_name = 'account_balance_wallet'
    list_display = ['producto', 'cantidad', 'vendedor', 'cliente' ]
    # prepopulated_fields = {'vendedor': ('nombre',)}


admin.site.register(Ventas, VentasAdmin)