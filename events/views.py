from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Registration


def event_list(request):
    search = request.GET.get('search')

    if search:
        events = Event.objects.filter(title__icontains=search).order_by('date')
    else:
        events = Event.objects.all().order_by('date')

    return render(request, 'index.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    registered_count = Registration.objects.filter(event=event).count()

    if registered_count >= event.total_slots:
        return render(request, 'registration_closed.html', {'event': event})

    return render(request, 'event_detail.html', {'event': event})


def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        college_name = request.POST['college_name']
        department = request.POST['department']
        current_year = request.POST['current_year']

        existing_registration = Registration.objects.filter(
            event=event,
            email=email
        ).first()

        if existing_registration:
            return render(request, 'already_registered.html', {'event': event})

        registered_count = Registration.objects.filter(event=event).count()

        if registered_count >= event.total_slots:
            return render(request, 'registration_closed.html', {'event': event})

        Registration.objects.create(
            event=event,
            name=name,
            email=email,
            phone=phone,
            college_name=college_name,
            department=department,
            current_year=current_year
        )

        return render(request, 'success.html', {'event': event})

    return render(request, 'register.html', {'event': event})


def registrations(request):
    registrations = Registration.objects.all()
    return render(request, 'registrations.html', {'registrations': registrations})


def cancel_registration(request, reg_id):
    registration = get_object_or_404(Registration, id=reg_id)
    registration.delete()
    return redirect('registrations')