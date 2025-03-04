from django.contrib import admin
from django.contrib import messages
from .models import Retail, Product


@admin.register(Retail)
class RetailAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Retail.
    Позволяет управлять объектами сети (заводами, розничными сетями, ИП).
    """

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
        """
        Admin action для очистки задолженности у выбранных объектов.
        Если у пользователя нет прав, выводит сообщение об ошибке.
        """
        if not request.user.has_perm('retails.can_clear_debt'):
            self.message_user(request, "У вас нет прав для очистки задолженности.", messages.ERROR)
            return
        queryset.update(debt=0)  # Обнуляем задолженность
    clear_debt.short_description = "Очистить задолженность"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Админ-панель для модели Product.
    Позволяет управлять продуктами, связанными с объектами сети.
    """

    list_display = ('id', 'name', 'supplier', 'model', 'release_date')
    list_filter = ('name', 'supplier',)
    search_fields = ("name",)
