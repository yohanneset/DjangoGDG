from django.urls import path
from .views import (
    LoanListView, 
    LoanCreateView,
    LoanUpdateView,
    LoanDeleteView,
    LoanDetailView,
    )

urlpatterns = [
    path('', LoanListView.as_view(), name='index'),
    path('add/', LoanCreateView.as_view(), name='add'),
    path('<int:pk>/u/', LoanUpdateView.as_view(), name='update'),
    path('<int:pk>/del/', LoanDeleteView.as_view(), name='delete'),
    path('<int:pk>/det/', LoanDetailView.as_view(), name='detail'),

]