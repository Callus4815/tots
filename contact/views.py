from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

from contact.forms import contactForm

# Create your views here.


def contact(request):
	title = 'Contact'
	form = contactForm(request.POST or None)
	template = 'contact.html'
	confirm_message = None


	if form.is_valid():
		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		subject = 'Message from MYSITE.com'
		message = '{} {}'.format(comment, name)
		email_from = form.cleaned_data['email']
		email_to = [settings.EMAIL_HOST_USER]
		send_mail(subject, message, email_from, email_to, fail_silently=True)
		title = "Thanks"
		confirm_message = "Thanks for the message!"
		form = None

	context = {'title': title, 'form': form, 'confirm_message': confirm_message}
	return render(request, template, context)