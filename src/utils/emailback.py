from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



def send_email():
    template = get_template('email/email.html')
    context = Context({'user': user, 'other_info': info})
    content = template.render(context)
    msg = EmailMessage(subject, content, from, to=[user.email,])
    msg.send()