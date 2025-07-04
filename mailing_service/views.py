from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Recipient, Message


def home(request):
    return render(request, 'mailing_service/base.html')


class RecipientCreateView(CreateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'mailing_service/recipient_create.html'
    success_url = reverse_lazy('mailing_service:recipients_list')


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'mailing_service/recipient_detail.html'
    context_object_name = 'recipient'


class RecipientUpdateView(UpdateView):
    model = Recipient
    fields = ['email', 'full_name', 'comment']
    template_name = 'mailing_service/recipient_create.html'
    success_url = reverse_lazy('mailing_service:recipients_list')


class RecipientDeleteView(DeleteView):
    model = Recipient
    template_name = 'mailing_service/recipient_delete.html'
    success_url = reverse_lazy('mailing_service:recipients_list')


class RecipientListView(ListView):
    model = Recipient
    template_name = 'mailing_service/recipients_list.html'
    context_object_name = 'recipients'


class MessageCreateView(CreateView):
    model = Message
    fields = ['subject', 'letter']
    template_name = 'mailing_service/message_create.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing_service/message_detail.html'
    context_object_name = 'message'


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['subject', 'letter']
    template_name = 'mailing_service/message_create.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing_service/message_delete.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageListView(ListView):
    model = Message
    template_name = 'mailing_service/messages_list.html'
    context_object_name = 'message'
