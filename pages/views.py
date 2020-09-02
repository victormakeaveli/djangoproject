from django.views.generic import TemplateView

from .models import Post 


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Post

class AboutPageView(TemplateView):
    template_name = 'about.html'