from django import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, primary_key=True, unique=True)
    address = models.TextField()

    def __str__(self):
        return self.name


