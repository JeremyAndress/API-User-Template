from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

def send_email():
    subject, from_email, to = 'Subject', 'from@xxx.com', 'jeremysilvasilva@gmail.com'
    template = get_template('email/activate.html')
    context = Context({'header':header,'body':body})
    content = template.render(context)
    msg = EmailMessage(subject, content, from_email,[to])
    msg.send()