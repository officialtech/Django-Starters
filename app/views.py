# New everything
from django.views.generic import TemplateView

class AppHomePage(TemplateView):
    template_name = "app/home.html"