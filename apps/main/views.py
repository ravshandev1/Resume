from django.shortcuts import render, redirect
from .models import Carousel
from person.models import About, Resume, Service, Skill, Project
from blog.models import Blog
from .forms import ContactForm
from django.contrib import messages


def home(request):
    carousel = Carousel.objects.all()
    about = About.objects.last()
    resumes = Resume.objects.all()[:6]
    services = Service.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.order_by('-id').all()[:6]
    blogs = Blog.objects.order_by('-id').all()
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, f"<strong>Your message successfully sent!!</strong>")
        return redirect('.')
    context = {
        'items': carousel,
        'about': about,
        'resumes': resumes,
        'services': services,
        'skills': skills,
        'projects': projects,
        'blogs': blogs,
        'form': form
    }
    return render(request, 'index.html', context)
