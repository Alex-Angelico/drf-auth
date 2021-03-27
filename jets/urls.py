from django.urls import path
from .views import JetsListView, JetsDetailView

urlpatterns = [
    path('', JetsListView.as_view(), name='jets_list'),
    path('<int:pk>/', JetsDetailView.as_view(), name='jets_detail'),
]