from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.api.v1.views import (
    UserViewSet,
    StatusViewSet,
    TypeViewSet,
    CategoryViewSet,
    SubCategoryViewSet,
    TransactionViewSet
)


app_name = 'api'

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('statuses', StatusViewSet, basename='status')
router.register('types', TypeViewSet, basename='type')
router.register('categories', CategoryViewSet, basename='category')
router.register('subcategories', SubCategoryViewSet, basename='subcategory')
router.register('transactions', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('', include(router.urls)),
]
