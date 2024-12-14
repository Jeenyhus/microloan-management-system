from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    subscription_plan = models.CharField(max_length=50, default='Basic')  # Plan types (Basic, Premium, etc.)
    max_users = models.IntegerField(default=10)  # Subscription limits
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users", null=True, blank=True)
    is_admin = models.BooleanField(default=False)  # Admins manage the company account
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username

class Borrower(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="borrowers")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Loan(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, related_name="loans")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)  # Example: 12.5%
    term_in_months = models.IntegerField()  # Loan duration
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Disbursed', 'Disbursed'),
        ('Completed', 'Completed'),
        ('Defaulted', 'Defaulted'),
    ], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Loan #{self.id} - {self.borrower}"

class Repayment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="repayments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repayment of {self.amount} for Loan #{self.loan.id}"
