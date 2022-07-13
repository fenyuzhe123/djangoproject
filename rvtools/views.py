from django.shortcuts import render, HttpResponse
from django import forms
from . import models


# Create your views here.
class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vHBA
        fields = '__all__'


def dash(request):
    queryset = models.vHBA.objects.all().order_by("host")

    return render(request, "test.html", {"queryset": queryset})


def index(request):
    return render(request, 'servers_list.html')

