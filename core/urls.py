from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import CompanyViewSet, BorrowerViewSet, LoanViewSet, RepaymentViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('borrowers', BorrowerViewSet)
router.register('loans', LoanViewSet)
router.register('repayments', RepaymentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
]
