from django.shortcuts import render
from .models import Specialty, Vacancy, Company
from django.views.generic import ListView, DetailView, TemplateView


class MainView(ListView):
    template_name = 'vacancies/main.html'

    def get_queryset(self):
        queryset = {
            'specialties': Specialty.objects.all(),
            'companies': Company.objects.all()
        }
        return queryset


class VacanciesListView(ListView):
    template_name = 'vacancies/vacancies_list.html'

    def get_queryset(self):
        queryset = {
            'vacancies': Vacancy.objects.all()
        }
        return queryset


class VacancyDetailView(DetailView):
    model = Vacancy
    template_name = 'vacancies/vacancy_detail.html'


class VacanciesSpecialtiesListView(ListView):
    template_name = 'vacancies/vacancies_list.html'

    def get_queryset(self):
        vacancies = Vacancy.objects.filter(specialty__code=self.kwargs['vacancies'])
        queryset = {
            'vacancies': vacancies,
        }
        return queryset


class CompanyVacanciesListView(DetailView):
    model = Company
    template_name = 'vacancies/company_detail.html'
