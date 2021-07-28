from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import Recipe
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse

def add_recipe(request):
   recipes = Recipe.objects.order_by("-pub_date")
   return render(request, 'Recipes/addrecipe.html',{'recipes':recipes})

def create_recipe(request):
  # import pdb
  # pdb.set_trace()

   return render(request, 'Recipes/createrecipe.html',{})

def recipe(request):
   print(request.POST['name'])
   rec = Recipe.objects.create(name=request.POST['name'], ingredients=request.POST['ingredients'],
                               process=request.POST['process'], pub_date=timezone.now())

   return HttpResponseRedirect(reverse("Recipes:add_recipe"))

def detail(request, recipe_id):
   details = Recipe.objects.get(pk=recipe_id)
   return render(request,'Recipes/detail.html',{'details':details} )


