from django.db import models


class Recipient(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    full_name = models.CharField(max_length=100)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'recipient'
        verbose_name_plural = 'recipients'
        ordering = ['email']


class Message(models.Model):
    subject = models.CharField(max_length=100, blank=True)
    letter = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'
        ordering = ['subject']
