from django.shortcuts import render, HttpResponse
from django import forms
from . import models


# Create your views here.
class dashModelForm(forms.ModelForm):
    class Meta:
        model = models.vHBA
        fields = '__all__'


def dash(request):
    queryset = models.vHBA.objects.all()
    return render(request, "test.html", {"queryset": queryset})


def index(request):
    queryset = models.vHBA.objects.all().order_by("host")
    for i in queryset:
        print(i.vi_sdk_uuid)

    return render(request, 'servers_list.html', {"queryset": queryset})

