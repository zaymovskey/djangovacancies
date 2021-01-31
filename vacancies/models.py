
from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse


class Specialty(models.Model):
    code = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    picture = models.ImageField(upload_to='specialties')

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.title


class Company(models.Model):
    title = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    logo = models.ImageField(upload_to='companies')
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, related_name='company', on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('my_company_update_url', args=[self.id])


class Vacancy(models.Model):
    title = models.CharField(max_length=155)
    specialty = models.ForeignKey(Specialty, related_name='vacancies', on_delete=models.PROTECT)
    company = models.ForeignKey(Company, related_name='vacancies', on_delete=models.CASCADE)
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def get_absolute_url(self):
        return reverse('my_company_vacancies_update_url', args=[self.id])


class Application(models.Model):
    written_username = models.CharField(max_length=75)
    written_phone = models.IntegerField()
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, related_name='applications', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, related_name='applications', on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('applications_create_url', args=[self.vacancy.id])

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'
