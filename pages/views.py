from django.views.generic import TemplateView, ListView

from .models import Post 


class HomePageView(TemplateView):
    template_name = 'home.html'
    model = Post

class AboutPageView(ListView):
    template_name = 'about.html'