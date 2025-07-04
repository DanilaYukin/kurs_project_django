from django.urls import path

from . import views
from .apps import MailingServiceConfig
from .views import RecipientCreateView, RecipientListView, RecipientDeleteView, RecipientDetailView, \
    RecipientUpdateView, MessageListView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageUpdateView

app_name = MailingServiceConfig.name

urlpatterns = [
    path('home/', views.home, name='home'),
    path('recipients_list/', RecipientListView.as_view(), name='recipients_list'),
    path('recipient_create/', RecipientCreateView.as_view(), name='recipient_create'),
    path('recipient_detail/<int:pk>/', RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipient_update/<int:pk>/', RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipient_delete/<int:pk>/', RecipientDeleteView.as_view(), name='recipient_delete'),
    path('messages_list/', MessageListView.as_view(), name='messages_list'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_detail/<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
    path('message_update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('message_delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
]
