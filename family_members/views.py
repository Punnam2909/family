from django.shortcuts import render
from django.shortcuts import HttpResponse


def FamilyApp(request):
    Punnams=Punnam.objects.all()
    context={
        "Punnams":Punnams,
    }

    return render(request, "Family_Members APP/indexfammem.html", context)

def Punnam(request):
    return render(request,"Family_Members APP/punnam.html",{})

def Ramala(request):
    return render(request,"Family_Members APP/ramala.html",{})
