from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'Index.html'

class DediPageView(TemplateView):
    template_name = 'Dedicatoria.html'
