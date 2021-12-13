from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolios'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name='portfolio'),
    path('blog/', views.BlogView.as_view(), name='blogs'),
    path('blog/<slug:slug>', views.PortfolioView.as_view(), name='blog'),
]