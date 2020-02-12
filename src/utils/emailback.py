from django.core.mail import EmailMessage
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template
from django.template.loader import render_to_string

def send_email(subject,to,preview):
    subject, from_email = subject, 'misperrisduoc.duoc@gmail.com'
    to = to
    preview = {'msj':preview}
    header = {'msj': 'Gracias Por Registrarte','msj2':'Para activar su cuenta acceda al siguiente link'}
    lorem = '''Lorem ipsum dolor sit amet, 
    consectetur adipiscing elit, sed do eiusmod 
    tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute 
    irure dolor in reprehenderit in voluptate velit esse cillum 
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat 
    cupidatat non proident, sunt in culpa qui officia deserunt 
    mollit anim id est laborum.'''
    body =  {'msj':lorem}
    ctx = {'preview':preview,'header':header,'body':body}
    template = get_template('email/activate-email.html').render(ctx)
    print(template)
    msg = EmailMultiAlternatives(subject, template, from_email, [to])
    msg.attach_alternative(template, "text/html")
    msg.send()





