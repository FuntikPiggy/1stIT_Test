from django.contrib import admin
from django.contrib.auth import get_user_model
from rangefilter.filters import DateRangeFilter


from .models import Type, Status, Category, SubCategory, Transaction

User = get_user_model()


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    """Настройки раздела Типы админ-панели."""

    list_display = ('name', 'get_name_display',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    """Настройки раздела Статусы админ-панели."""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки раздела Категории админ-панели."""


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    """Настройки раздела Подкатегории админ-панели."""


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    """Настройки раздела Транзакции админ-панели."""

    list_display = ('created', 'status_name', 'type_name', 'category', 'sub_categories', 'amount', 'comment',)
    list_filter = (('created', DateRangeFilter), 'status', 'type', 'category', 'sub_categories',)
    list_display_links = ('created',)

    @admin.display(description='Статус',)
    def status_name(self, transaction):
        return str(transaction.status)

    @admin.display(description='Тип',)
    def type_name(self, transaction):
        return str(transaction.type)