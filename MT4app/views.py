from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView 
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Service, Review
from .forms import ServiceForm, ReviewForm


def welcome(request):
    """
    Render the welcome page.

    Returns the rendered 'welcome.html' template.
    """
    
    return render(request, 'MT4app/welcome.html')

def services(request):
    services = Service.objects.all().order_by('-id')
    reviews = Review.objects.all().order_by('-id')
    context = {
        'services': services,
        'reviews': reviews,
    }
    template = 'MT4app/services.html'

    return render(request, template, context)

@login_required
def create_services(request):
    """ Add a service to the site """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
            form = ServiceForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                print('save')
                return redirect(reverse('services'))
            else:
                form = ServiceForm()
                print('error')
    else:
            form = ServiceForm()

    template = 'MT4app/create_services.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_service(request,service_id):
    """edit service view"""

    if not request.user.is_superuser:
        return redirect(reverse('home'))

    service= get_object_or_404(Service, pk=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect(reverse('services'))
        else:
            form = ServiceForm()
    else:
        form = ServiceForm(instance=service)

    template = 'MT4app/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)

@login_required
def delete_service(request, service_id):
    """ Delete service """

    service = get_object_or_404(Service, id=service_id)
    service.delete()

    return redirect(reverse('books'))


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
