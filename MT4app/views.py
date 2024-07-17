from django.shortcuts import render, get_object_or_404, redirect 
from django.views.generic import TemplateView 
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Review


def welcome(request):
    """
    Render the welcome page.

    Returns the rendered 'welcome.html' template.
    """
    
    return render(request, 'MT4app/welcome.html')

def services(request):
    services = Service.objects.all()
    context = {
        'services': services
    }
    template = 'MT4app/services.html'

    return render(request, template, context)



# class DetailingView(TemplateView):
#     pass

# class ServiceListView(ListView):
#     model = Service
#     template_name = 'services/services_list.html'
#     context_object_name = 'services'

# class ServiceDetailView(DetailView):
#     model = Service
#     template_name = 'services/service_detail.html'
#     context_object_name = 'service'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['reviews'] = Review.objects.filter(service=self.object)
#         return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['content', 'rating']
    template_name = 'MT4app/services.html'
    
    def form_valid(self, form):
        form.instance.reviews = Reviews.objects.get(pk=self.kwargs['review_pk'])
        form.instance.customer = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reviews-detail', args=[self.object.review.pk])
