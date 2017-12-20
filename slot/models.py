from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EmployeeSlot(models.Model):
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    employee = models.ForeignKey(Employee, related_name='slots')


class CandidateSlot(models.Model):
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    candidate = models.ForeignKey(Candidate, related_name='slots')




