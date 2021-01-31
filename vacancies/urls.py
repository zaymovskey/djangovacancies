from django.urls import path
from vacancies.views import MainView, VacanciesListView, VacancyDetailView, VacanciesSpecialtiesListView, \
    CompanyVacanciesView, ApplicationCreateView, MyCompanyCreateView, MyCompanyVacanciesView, RegisterView, \
    LoginSiteView, LogoutSiteView, MyCompanyToCreateView, MyCompanyUpdateView, \
    VacancyCreateView, MyCompanyVacanciesUpdateView, SearchView, Error404View, Error505View

urlpatterns = [
    path('', MainView.as_view(), name='main_url'),
    path('vacancies/', VacanciesListView.as_view(), name='vacancies_list_url'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy_detail_url'),
    path('vacancies/cat/<str:vacancies>/', VacanciesSpecialtiesListView.as_view(),
         name='vacancies_specialties_list_url'),
    path('companies/<int:pk>/', CompanyVacanciesView.as_view(), name='company_vacancies_list_url'),
    path('vacancies/<int:vacancy_id>/send/', ApplicationCreateView.as_view(), name='applications_create_url'),
    path('my_company/', MyCompanyCreateView.as_view(), name='my_company_url'),
    path('my_vacancies/<int:pk>/', MyCompanyVacanciesView.as_view(), name='my_company_vacancies_url'),
    path('register/', RegisterView.as_view(), name='register_url'),
    path('login/', LoginSiteView.as_view(), name='login_url'),
    path('logout/', LogoutSiteView.as_view(), name='logout_url'),
    path('my_company_to_create/', MyCompanyToCreateView.as_view(), name='my_company_to_create_url'),
    path('my_company_update/<int:pk>/', MyCompanyUpdateView.as_view(), name='my_company_update_url'),
    path('my_vacancy_create/', VacancyCreateView.as_view(), name='vacancy_create_url'),
    path('my_vacancies/<int:pk>/update', MyCompanyVacanciesUpdateView.as_view(),
         name='my_company_vacancies_update_url'),
    path('search/', SearchView.as_view(), name='search_url')
]


handler404 = Error404View.as_view()
handler505 = Error505View.as_view()