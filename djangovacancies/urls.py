from django.contrib import admin
from django.urls import path
from vacancies.views import MainView, VacanciesListView, VacancyDetailView, VacanciesSpecialtiesListView, CompanyVacanciesListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_url'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_list_url'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail_url'),
    path('vacancies/cat/<str:vacancies>/', VacanciesSpecialtiesListView.as_view(), name='vacancies_specialties_list_url'),
    path('companies/<int:pk>/', CompanyVacanciesListView.as_view(), name='company_vacancies_list_url')
]
