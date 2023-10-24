from django.shortcuts import render
from django.views.generic import View, TemplateView

class LangingViewPage(TemplateView):
    template_name = "userauth/index.html"