from django.contrib import admin
from .models import Cliente, Categoria, Produto, Venda, DetVenda


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'email', 'fone', 'criado_em')
    date_hierarchy = 'criado_em'


class ProdutoAdmin(admin.ModelAdmin):
    ordering = ['produto']
    list_display = ('produto', 'categoria', 'preco')


class DetVendaInline(admin.TabularInline):
    list_display = ['produto', 'quantidade', 'precovenda', 'valor_total']
    readonly_fields = ['valor_total']
    model = DetVenda
    extra = 0


class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', '__unicode__')
    inlines = [DetVendaInline]


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Venda, VendaAdmin)
