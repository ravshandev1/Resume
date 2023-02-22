from django.shortcuts import render, redirect
from .models import Blog, Category, Tag
from .forms import CommentForm
from django.contrib import messages
from django.contrib.admin import site


def single(request, pk):
    blog = Blog.objects.filter(id=pk).first()
    categories = Category.objects.all()
    blogs = Blog.objects.order_by('-id').all()[:3]
    tags = Tag.objects.all()
    form = CommentForm(request.POST or None, request.FILES)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.blog = blog
        obj.save()
        messages.success(request, f"<strong>Your message successfully sent!!</strong>")
        return redirect('.')
    context = {
        'blog': blog,
        'form': form,
        'categories': categories,
        'blogs': blogs,
        'tags': tags
    }
    return render(request, 'single.html', context)
