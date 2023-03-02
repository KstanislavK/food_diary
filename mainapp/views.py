from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from .forms import FoodIntakeCRUDForm, SearchForm, UserRegistrationForm
from .models import FoodIntake

def index(request):
    return render(request, 'layout/index.html')


@login_required
def food_intake_list(request):
    objects = FoodIntake.objects.filter(user=request.user)
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            search_results = []
            data_for_search = form.data['data_for_search'].lower()

            search_results = set(list(FoodIntake.objects.filter(user=request.user, food__contains=data_for_search)) + search_results)

            context = {
                'title': 'Приемы еды',
                'objects': search_results,
                'dfs': data_for_search,
            }
            return render(request, 'mainapp/food.html', context)

    context = {
        'title': 'Приемы еды',
        'objects': objects,
    }
    return render(request, 'mainapp/food.html', context)


class FoodIntakeCreateView(LoginRequiredMixin, CreateView):
    model = FoodIntake
    template_name = 'mainapp/food_intake_crud.html'
    form_class = FoodIntakeCRUDForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(FoodIntakeCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(FoodIntakeCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Добавление записи'
        return context


class FoodIntakeUpdateView(LoginRequiredMixin, UpdateView):
    model = FoodIntake
    context_object_name = 'object'
    template_name = 'mainapp/food_intake_crud.html'
    form_class = FoodIntakeCRUDForm

    def get_context_data(self, **kwargs):
        context = super(FoodIntakeUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование записи'
        return context


class RegisterNewUser(CreateView):
    form_class = UserRegistrationForm
    success_url = '/'
    template_name = 'registration/register_new_user.html'
