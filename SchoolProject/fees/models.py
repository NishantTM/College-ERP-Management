from django.db import models

from students.models import Student


# Create your models here.
class Fees(models.Model):
    FEE_STATUS = [("Pending", "Pending"), ("Partial", "Partial"), ("Paid", "Paid")]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="fees")
    amount = models.DecimalField(
    max_digits=10,
    decimal_places=2
)

    paid_amount = models.DecimalField(
    max_digits=10,
    decimal_places=2,
    default=0
)

    due_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=100, choices=FEE_STATUS, default="Pending")

    def __str__(self):
        return f"{self.student.name} - {self.amount}"
