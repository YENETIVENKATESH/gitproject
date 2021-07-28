from django.urls import path,include
from . import views


app_name = 'Recipes'
urlpatterns =[
    path('', views.add_recipe, name='add_recipe'),
    path('create/',views.create_recipe, name='create_recipe'),
    path('<int:recipe_id>/detail/', views.detail, name= 'detail'),
    path('recipe/',views.recipe, name='recipe'),
]