from rest_framework.viewsets import ModelViewSet
from .models import Company, Borrower, Loan, Repayment
from .serializers import CompanySerializer, BorrowerSerializer, LoanSerializer, RepaymentSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

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
