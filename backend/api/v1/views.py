from django.contrib.auth import get_user_model
from rest_framework import viewsets

from backend.money.models import (
    Status,
    Type,
    Category,
    SubCategory,
    Transaction
)

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """Представление модели пользователя."""

    queryset = User.objects.all()


class StatusViewSet(viewsets.ModelViewSet):
    """Представление модели статуса."""

    queryset = Status.objects.all()


class TypeViewSet(viewsets.ModelViewSet):
    """Представление модели типа транзакции."""

    queryset = Type.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    """Представление модели категории."""

    queryset = Category.objects.all()


class SubCategoryViewSet(viewsets.ModelViewSet):
    """Представление модели подкатегории."""

    queryset = SubCategory.objects.all()


class TransactionViewSet(viewsets.ModelViewSet):
    """Представление модели транзакции."""

    queryset = Transaction.objects.all()
