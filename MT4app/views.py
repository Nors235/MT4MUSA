from django.shortcuts import render

from django.views.generic import TemplateView 
from .models import Post

class PostList(generic.ListView):
    model = Post
class DetailingView(TemplateView):
    pass

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service, Review

class ServiceListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(service=self.object)
        return context

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ['content', 'rating']
    template_name = 'reviews/create_review.html'
    
    def form_valid(self, form):
        form.instance.service = Service.objects.get(pk=self.kwargs['service_pk'])
        form.instance.customer = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('services-detail', args=[self.object.service.pk])
