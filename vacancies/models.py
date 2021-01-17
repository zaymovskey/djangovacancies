from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    picture = models.URLField(default='https://place-hold.it/100x60')


class Company(models.Model):
    title = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=155)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published = models.DateField()
