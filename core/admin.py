from django.contrib import admin
from .models import Company, CustomUser, Borrower, Loan, Repayment

# Register your models here.

admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(Borrower)
admin.site.register(Loan)
admin.site.register(Repayment)