from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.urls import reverse
from .models import Specialty, Vacancy, Company
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from .forms import ApplicationForm, RegisterForm, LoginForm, CompanyForm, VacancyForm


class MainView(TemplateView):
    template_name = 'vacancies/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'specialties': Specialty.objects.all(),
                'companies': Company.objects.all()
            }
        )
        return context


class VacanciesListView(ListView):
    template_name = 'vacancies/vacancies_list.html'
    queryset = Vacancy.objects.all()
    context_object_name = 'vacancies'


class VacancyDetailView(DetailView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = ApplicationForm()
        form.helper.form_action = reverse('applications_create_url', args=[kwargs['object'].id])
        context['application_form'] = form
        return context


class VacanciesSpecialtiesListView(ListView):
    template_name = 'vacancies/vacancies_list.html'

    def get_queryset(self):
        queryset = Vacancy.objects.filter(specialty__code=self.kwargs['vacancies'])
        self.context_object_name = 'vacancies'
        return queryset


class CompanyVacanciesView(DetailView):
    model = Company
    template_name = 'vacancies/company_detail.html'


class ApplicationCreateView(CreateView):
    form_class = ApplicationForm
    template_name = 'vacancies/sent.html'

    def form_valid(self, form):
        form.instance.vacancy = Vacancy.objects.get(id=self.kwargs['vacancy_id'])
        form.instance.user = User.objects.get(username=self.request.user)
        return super().form_valid(form)


class MyCompanyCreateView(CreateView):
    template_name = 'vacancies/company_create.html'
    model = Company
    form_class = CompanyForm

    def form_valid(self, form):
        form.instance.owner = User.objects.get(username=self.request.user)
        return super().form_valid(form)


class MyCompanyUpdateView(UpdateView):
    template_name = 'vacancies/company_update.html'
    form_class = CompanyForm
    model = Company

    def form_valid(self, form):
        success_message = 'Информация сохранена'
        messages.success(self.request, success_message)
        return super().form_valid(form)


class MyCompanyToCreateView(TemplateView):
    template_name = 'vacancies/company_to_create.html'


class MyCompanyVacanciesView(DetailView):
    template_name = 'vacancies/my_company_vacancies.html'
    context_object_name = 'company'
    model = Company


class MyCompanyVacanciesUpdateView(UpdateView):
    template_name = 'vacancies/vacancy_update.html'
    form_class = VacancyForm
    model = Vacancy

    def form_valid(self, form):
        success_message = 'Информация сохранена'
        messages.success(self.request, success_message)
        return super().form_valid(form)


class VacancyCreateView(CreateView):
    template_name = 'vacancies/vacancy_create.html'
    model = Company
    form_class = VacancyForm

    def form_valid(self, form):
        success_message = 'Вакансия создана'
        messages.success(self.request, success_message)
        form.instance.company = Company.objects.get(id=self.request.user.company.id)
        return super().form_valid(form)


class LoginSiteView(LoginView):
    template_name = 'vacancies/login.html'
    form_class = LoginForm


class LogoutSiteView(LogoutView):
    next_page = '/'


class RegisterView(CreateView):
    template_name = 'vacancies/register.html'
    form_class = RegisterForm
    model = User
    success_url = '/login/'


class SearchView(ListView):
    model = Vacancy
    template_name = 'vacancies/search.html'
    context_object_name = 'vacancies'

    def get_queryset(self):
        q = self.request.GET.get('q')
        queryset = Vacancy.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
        return queryset


class Error404View(TemplateView):
    template_name = '404.html'


class Error505View(TemplateView):
    template_name = '505.html'
