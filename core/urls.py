from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, BorrowerViewSet, LoanViewSet, RepaymentViewSet

router = DefaultRouter()
router.register('companies', CompanyViewSet)
router.register('borrowers', BorrowerViewSet)
router.register('loans', LoanViewSet)
router.register('repayments', RepaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
