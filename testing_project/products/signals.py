from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from products.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):

    if created:
        send_mail(
            "Welcome!",
            "Thanks for signing up!",
            "admin@django.com",
            [instance.email],
            fail_silently=False
        )