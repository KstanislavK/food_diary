from django.urls import path

from .views import food_intake_list, FoodIntakeCreateView, FoodIntakeUpdateView, RegisterNewUser, index

app_name = 'mainapp'

urlpatterns = [
    path('food/', food_intake_list, name='food_intake'),
    path('food/create/', FoodIntakeCreateView.as_view(), name='food_intake_create'),
    path('food/update/<int:pk>/', FoodIntakeUpdateView.as_view(), name='food_intake_update'),
    path('register/', RegisterNewUser.as_view(), name='user_register'),
    path('', index, name='index'),
]
