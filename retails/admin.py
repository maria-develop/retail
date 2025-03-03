from django.contrib import admin
from django.contrib import messages
from .models import Retail, Product

@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'debt', 'created_at')
    list_filter = ('city',)  # Фильтр по городу
    actions = ['clear_debt']  # Регистрация действия

    # Ссылка на поставщика
    def supplier(self, obj):
        if obj.supplier:
            return obj.supplier.name
        return "-"
    supplier.short_description = 'Supplier'

    # Admin action для очистки задолженности
    def clear_debt(self, request, queryset):
        if not request.user.has_perm('retails.can_clear_debt'):
            self.message_user(request, "You don't have permission to clear debts.", messages.ERROR)
            return
        queryset.update(debt=0)
    clear_debt.short_description = "Clear debt for selected retails"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'supplier', 'model', 'release_date')
    list_filter = ('name', 'supplier',)
    search_fields = ("name",)
