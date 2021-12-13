from django.shortcuts import render
# from django.contrib import messages
from .models import (
    Skill,
    Blog,
    Portfolio,
    Certificate
)

from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        skills = Skill.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        context['skills'] = skills
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio
        
        return context

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'main/portfolio-detail.html'

class BlogView(generic.ListView):
    model = Blog
    template_name = 'main/blog.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class PortfolioDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog-detail.html'