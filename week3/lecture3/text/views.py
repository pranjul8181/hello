from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


#text = ["foo", "bar","baz"]
#text = []
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    

def index(request):
    if "text" not in request.session:
        request.session["text"]=[]
    return render(request, "text/index.html", {
        "text" : request.session["text"] 
    })

def add(request):
    if request.method =="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            #text.append(task)
            request.session["text"] += [task]
            return HttpResponseRedirect(reverse("text:index"))
        else:
            return render(request,"text/add.html",{
                "form": form
            })

    return render(request, "text/add.html",{
        "form": NewTaskForm() 
    })
