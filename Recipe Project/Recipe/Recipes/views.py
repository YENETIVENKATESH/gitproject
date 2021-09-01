from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from .models import Recipe
from django.utils import timezone



def add_recipe(request):
    recipes = Recipe.objects.order_by("-pub_date")
    return render(request, 'Recipes/addrecipe.html', {'recipes': recipes})


def create_recipe(request):
    return render(request, 'Recipes/createrecipe.html')


def recipe(request):

    if request.method == "POST" and request.FILES['upload_image']:
        rec = Recipe.objects.create(name=request.POST['name'], ingredients=request.POST['ingredients'],
                                    process=request.POST['process'], images=request.FILES['upload_image'],
                                    pub_date=timezone.now())
        return HttpResponseRedirect(reverse("Recipes:add_recipe"))


def detail(request, recipe_id):
    details = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'Recipes/detail.html', {'details': details})


def delete_recipe(request, recipe_id):
    # if request.GET == "delete":
    recipe_del = get_object_or_404(Recipe, pk=recipe_id)
    print(recipe_del)
    recipe_del.delete()
    return HttpResponseRedirect(reverse("Recipes:add_recipe"))


def editable(request, recipe_id):
    if request.method == "GET":
        edited_recipe = get_object_or_404(Recipe, pk=recipe_id)
        return render(request, "Recipes/edit.html", {"edited_recipe": edited_recipe})
    else:
        rec = get_object_or_404(Recipe, pk=recipe_id)
        rec.name = request.POST['name']
        rec.ingredients = request.POST['ingredients']
        rec.process = request.POST['process']
        rec.images = request.FILES['upload_image']
        rec.save()
        return HttpResponseRedirect(reverse("Recipes:add_recipe"))
