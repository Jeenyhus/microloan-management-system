from rest_framework.viewsets import ModelViewSet
from .models import Company, Borrower, Loan, Repayment, LoanApplication, PaymentSchedule
from .serializers import CompanySerializer, BorrowerSerializer, LoanSerializer, RepaymentSerializer, LoanApplicationSerializer, PaymentScheduleSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def api_documentation(request):
    return render(request, 'core/api_documentation.html')

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class BorrowerViewSet(ModelViewSet):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    permission_classes = [IsAuthenticated]

class LoanViewSet(ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsAuthenticated]

class RepaymentViewSet(ModelViewSet):
    queryset = Repayment.objects.all()
    serializer_class = RepaymentSerializer
    permission_classes = [IsAuthenticated]

class LoanApplicationViewSet(ModelViewSet):
    queryset = LoanApplication.objects.all()
    serializer_class = LoanApplicationSerializer
    permission_classes = [IsAuthenticated]

class PaymentScheduleViewSet(ModelViewSet):
    queryset = PaymentSchedule.objects.all()
    serializer_class = PaymentScheduleSerializer
    permission_classes = [IsAuthenticated]

