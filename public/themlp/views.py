from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from .models import Customer

class FirstView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = Customer.objects.filter(id=1)
        return context

class StartView(TemplateView):
    template_name = "t_start.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer"] = Customer.objects.filter(id=1)
        return context
