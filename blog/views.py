from django.shortcuts import render
from .models import Box, Description, ContactMessage
from .forms import ContactForm

def home(request):
    boxes = Box.objects.all()
    main = Description.objects.all()
    return render(request, 'blog/index.html', {'boxes': boxes, 'main': main})

def sports(request):
    return render(request, 'blog/sports.html')

def travel(request):
    return render(request, 'blog/travel.html')

def projects(request):
    return render(request, 'blog/project.html')

def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
            form = ContactForm()  # Reset the form after saving
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {
        'form': form,
        'submitted': submitted
    })
