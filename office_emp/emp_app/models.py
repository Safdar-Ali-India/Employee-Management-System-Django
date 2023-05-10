from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50)

    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    hire_date = models.DateField()
    job_title = models.ForeignKey(Title, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
    #     # return f"{self.first_name} {self.last_name}"
        return f"{self.first_name} {self.last_name} - {self.job_title.name}"
    
    # class Meta:
    #     db_table='employeename'
