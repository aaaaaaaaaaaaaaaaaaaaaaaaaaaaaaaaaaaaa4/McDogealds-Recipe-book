from django.http import HttpResponse
from django.shortcuts import render
from django import forms
from django.utils.html import strip_tags
from django.shortcuts import redirect
from . import items
import markdown

items = items.items

def index(request):
    return render(request, "site/index.html")

def things(request):
    return render(request, "site/things.html", {"items": items})
def recipe(request, recipeid):
    return render(request, "site/recipe.html", {"item": items[int(recipeid)-1], "theitems": items})
class AddRecipeForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Title'}))
    about = forms.CharField(label="",  widget=forms.Textarea(attrs={'style': 'margin-top: 0px; margin-bottom: 0px; height: 184px;', 'placeholder': "About"}))
    recipe = forms.CharField(label="",  widget=forms.Textarea(attrs={'style': 'margin-top: 0px; margin-bottom: 0px; height: 184px;', 'placeholder': "Recipe"}))
    price = forms.IntegerField(label="", widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    url = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Image Url'}))
def add(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            title = strip_tags(form.cleaned_data["title"])
            about = strip_tags(form.cleaned_data["about"])
            recipe = strip_tags(form.cleaned_data["recipe"])
            url = strip_tags(form.cleaned_data["url"])
            price = int(strip_tags(form.cleaned_data["price"]))
            newid = items[-1]["ide"]+1
            items.append({"thing": title, "about": about, "recipe": markdown.markdown(recipe), "price": price, "ide": newid, "url": url})
            return redirect('/things')
        else:
            return render(request, "site/add.html", {
                "form": form
                })
    return render(request, "site/add.html", {
        "form": AddRecipeForm()
    })
def tools(request):
    return render(request, "site/tools.html", {"theitems": items})
def savecode(request):
    return HttpResponse("items = " + str(items))
