from django.db import models
from smart_selects.db_fields import ChainedForeignKey

BUSINESS = 'business'
PERSONAL = 'personal'
TAX = 'tax'

STATUSES = (
    (BUSINESS, 'Бизнес',),
    (PERSONAL, 'Личное',),
    (TAX, 'Налог',),
)

REFILL = 'refill'
WITHDRAWAL = 'withdrawals'


TYPES = (
    (REFILL, 'Пополнение'),
    (WITHDRAWAL, 'Списание'),
)


class Status(models.Model):
    """Модель статуса транзакции"""

    name = models.CharField(
        choices=STATUSES,
        max_length=max(map(lambda x: len(x[0]), STATUSES)),
    )

    class Meta:
        verbose_name = 'статус транзакции'
        verbose_name_plural = 'Статусы транзакции'
        default_related_name = 'statuses'
        ordering = ('name',)

    def __str__(self):
        return self.get_name_display()[:32]


class Type(models.Model):
    """Модель типа транзакции"""

    name = models.CharField(
        choices=TYPES,
        max_length=max(map(lambda x: len(x[0]), TYPES)),
    )

    class Meta:
        verbose_name = 'тип транзакции'
        verbose_name_plural = 'Типы транзакции'
        default_related_name = 'types'
        ordering = ('name',)

    def __str__(self):
        return self.get_name_display()[:32]


class Category(models.Model):
    """Модель категории"""

    name = models.CharField(
        verbose_name='Наименование',
        max_length=100,
    )
    text = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    type = models.ForeignKey(
        Type,
        verbose_name='Тип транзакции',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        default_related_name = 'categories'
        ordering = ('name',)

    def __str__(self):
        return self.name[:32]


class SubCategory(models.Model):
    """Модель подкатегории"""

    name = models.CharField(
        max_length=100,
        verbose_name='Наименование',
    )
    text = models.TextField(
        blank=True,
        verbose_name='Описание',
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.PROTECT,
    )

    class Meta:
        verbose_name = 'подкатегория'
        verbose_name_plural = 'Подкатегории'
        default_related_name = 'sub_categories'
        ordering = ('name',)

    def __str__(self):
        return self.name[:32]


class Transaction(models.Model):
    """Модель записи о движении денежных средств"""

    created = models.DateTimeField(
        verbose_name='Дата',
        auto_now_add=True
    )
    status = models.ForeignKey(
        Status,
        verbose_name='Статус',
        on_delete=models.PROTECT,
    )
    type = models.ForeignKey(
        Type,
        verbose_name='Тип',
        on_delete=models.PROTECT,
    )
    category = ChainedForeignKey(
        Category,
        verbose_name='Категория',
        chained_field="type",
        chained_model_field="type",
    )
    sub_categories = ChainedForeignKey(
        SubCategory,
        verbose_name='Подкатегории',
        chained_field="category",
        chained_model_field="category",
    )
    amount = models.DecimalField(
        verbose_name='Сумма, р.',
        max_digits=10,
        decimal_places=2,
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )

    class Meta:
        verbose_name = 'запись о ДДС'
        verbose_name_plural = 'Записи о ДДС'
        default_related_name = 'transactions'
        ordering = ['created']

    def __str__(self):
        return f'{self.type} - {self.amount} {self.comment}'
