from django.views.generic import TemplateView

from .models import Post 


class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    model = Post

    template_name = 'about.html'