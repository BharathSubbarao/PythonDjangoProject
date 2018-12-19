from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

from django.views.generic import TemplateView

# Create your views here.

##Class based view with explicit get method
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

##Class based view using template_name attribute. It internally invokes get automatically.
class AboutPageView(TemplateView):
    template_name = "about.html"

##A Django view is just a Python function that receives an HttpRequest object and returns an HttpResponse.
def MyProfileView(request):
    title = 'Architect'
    name = 'Bharath Subbarao'
    html = render_to_string('profile.html', {'title': title, 'name': name})
    return HttpResponse(html)