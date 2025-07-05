from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import MailingForm, RecipientForm, MessageForm
from .models import Recipient, Message, Mailing


class HomePageView(TemplateView):
    template_name = 'mailing_service/base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mailings'] = Mailing.objects.count()
        context['active_mailings'] = Mailing.objects.filter(status='Запущена').count()
        context['unique_recipients'] = Recipient.objects.count()
        return context


class RecipientCreateView(CreateView):
    model = Recipient
    form_class = RecipientForm
    template_name = 'mailing_service/recipient_create.html'
    success_url = reverse_lazy('mailing_service:recipients_list')


class RecipientDetailView(DetailView):
    model = Recipient
    template_name = 'mailing_service/recipient_detail.html'
    context_object_name = 'recipient'


class RecipientUpdateView(UpdateView):
    model = Recipient
    form_class = RecipientForm
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
    form_class = MessageForm
    template_name = 'mailing_service/message_create.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageDetailView(DetailView):
    model = Message
    template_name = 'mailing_service/message_detail.html'
    context_object_name = 'message'


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailing_service/message_create.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailing_service/message_delete.html'
    success_url = reverse_lazy('mailing_service:messages_list')


class MessageListView(ListView):
    model = Message
    template_name = 'mailing_service/messages_list.html'
    context_object_name = 'messages'


class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing_service/mailings_list.html'
    context_object_name = 'mailings'

    def get_queryset(self):
        queryset = super().get_queryset()
        for mailing in queryset:
            mailing.update_status()
        return queryset


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_service/mailing_create.html'
    success_url = reverse_lazy('mailing_service:mailings_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_status()
        return response


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailing_service/mailing_create.html'
    success_url = reverse_lazy('mailing_service:mailings_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.update_status()
        return response


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailing_service/mailing_delete.html'
    success_url = reverse_lazy('mailing_service:mailings_list')


class MailingDetailView(DetailView):
    model = Mailing
    template_name = 'mailing_service/mailing_detail.html'
    context_object_name = 'message'


class MailingSendView(View):
    def get(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        mailing.send()
        messages.success(request, f"Рассылка #{mailing.id} отправлена вручную.")
        return redirect('mailing_service:mailings_list')
