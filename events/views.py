from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.core.mail import send_mail
from django.conf import settings
from .models import Service, Event, Contact


def home(request):
    """Home page with all sections"""
    services = Service.objects.all()
    events = Event.objects.filter(featured=True)[:3]

    context = {
        'services': services,
        'events': events,
    }
    return render(request, 'events/home.html', context)


def services(request):
    """Services listing page"""
    services = Service.objects.all()

    # Group services by pillar
    pillars = {}
    for service in services:
        pillar = service.get_pillar_display()
        if pillar not in pillars:
            pillars[pillar] = []
        pillars[pillar].append(service)

    context = {
        'services': services,
        'pillars': pillars,
    }
    return render(request, 'events/services.html', context)


class EventListView(ListView):
    """Events portfolio listing"""
    model = Event
    template_name = 'events/events_list.html'
    context_object_name = 'events'
    paginate_by = 12

    def get_queryset(self):
        return Event.objects.all().order_by('-date')


class EventDetailView(DetailView):
    """Single event detail page"""
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


def contact(request):
    """Contact form page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save to database
        contact_obj = Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Send email to admin
        try:
            send_mail(
                f'Nouvelle demande de contact de {name}',
                f'Email: {email}\nTéléphone: {phone}\n\nMessage:\n{message}',
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=True,
            )
        except Exception:
            pass

        return redirect('contact_success')

    return render(request, 'events/contact.html')


def contact_success(request):
    """Contact form success page"""
    return render(request, 'events/contact_success.html')


def about(request):
    """About SEYNARA page"""
    services = Service.objects.all()

    context = {
        'services': services,
    }
    return render(request, 'events/about.html', context)
