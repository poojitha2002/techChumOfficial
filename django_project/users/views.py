from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from pathlib import Path
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.decorators import login_required

import blog
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Goodies,ContestSubmission,clgModel
from .models import UserDummy,Ratings
from .utils import get_plot
from django.conf import settings
from django.core.mail import send_mail
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            clg=form.cleaned_data.get('clg')
            print(clg)
            b=Goodies(coins=0,author=username)
            b.save()
            u=UserDummy(author=username)
            u.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            '''subject = 'Welcome to TechChum'
            message = f'Hello {username}!\nYou have successfully created a TechChum account.Thank you for teaming up with us, the best place to prepare for your dream Tech job.\nUse our site and avail the following benefits\n1.Get updated with latest Internships, Fellowships and Scholarships.\n2.Get access to structured courses and ace your interviews.\n3.Practice Mock Interviews and boost up your confidence\n4.Get your doubts resolved using our Discussion Forums and many more..\n\nSo what are you waiting for....Go ahead and avail all the benefits.\nOur social handles:\nLinkedIn: https://www.linkedin.com/company/techchum/\nFacebook:https://www.facebook.com/techchum.techchum\nInstagram:https://www.instagram.com/techchum/\nTelegram:https://t.me/techchum'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list) 
            subject, from_email, to = 'Welcome to TechChum', settings.EMAIL_HOST_USER, email
            text_content = 'This is an important message.'
            html_content ='{% load static %}' \
                          '<p>Hello {{username}}!<br>' \
                          'You have successfully created a TechChum account.' \
                          'Thank you for teaming up with us, the best place to prepare for your dream Tech job.' \
                          '<br>Use our site and avail the following benefits<br>1.Get updated with latest Internships, ' \
                          'Fellowships and Scholarships.<br>2.Get access to structured courses and ace your interviews.' \
                          '<br>3.Practice Mock Interviews and boost up your confidence<br>4.Get your doubts resolved using our' \
                          ' Discussion Forums and many more..<br><br>So what are you waiting for....Go ahead and avail all the benefits. ' \
                          '<img src="{% static 'blog/mail.png' %}" <br>Our social handles:' \
                                                            '<br>LinkedIn: https://www.linkedin.com/company/techchum/ <br>' \
                                                            'Facebook:https://www.facebook.com/techchum.techchum <br>' \
                                                            'Instagram:https://www.instagram.com/techchum/' \
                                                            ' <br>Telegram:https://t.me/techchum</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            '''
            recipient =email
            sender = settings.EMAIL_HOST_USER
            image_path = 'blog/static/blog/mail.png'
            image_name = Path(image_path).name
            subject = "Welcome to TechChum"
            text_message = f"Email with a nice embedded image {image_name}."
            html_message = f"""
            <!doctype html>
                <html lang=en>
                    <head>
                        <meta charset=utf-8>
                        <title>Some title.</title>
                    </head>
                    <body>
                      
                         <p>Hello!<br>You have successfully created a TechChum account.<br>Thank you for teaming up with us, the best place to prepare for your dream Tech job.<br>Use our site and avail the following benefits<br>1.Get updated with latest Internships, Fellowships and Scholarships.<br>2.Get access to structured courses and ace your interviews.<br>3.Practice Mock Interviews and boost up your confidence<br>4.Get your doubts resolved using our Discussion Forums and many more..<br><br>So what are you waiting for....Go ahead and avail all the benefits.<br> 
                        <img src='cid:{image_name}'/>
                        <br>
                        <br>Our social handles:<br>LinkedIn: https://www.linkedin.com/company/techchum/ <br> 
                                                            Facebook:https://www.facebook.com/techchum.techchum <br> 
                                                            Instagram:https://www.instagram.com/techchum/
                                                             <br>Telegram:https://t.me/techchum</p>
                     
                    </body>
                </html>
            """

            # the function for sending an email
            def send_email(subject, text_content, html_content=None, sender=sender, recipient=recipient,
                           image_path=None, image_name=None):
                email = EmailMultiAlternatives(subject=subject, body=text_content, from_email=sender,
                                               to=recipient if isinstance(recipient, list) else [recipient])
                if all([html_content, image_path, image_name]):
                    email.attach_alternative(html_content, "text/html")
                    email.content_subtype = 'html'  # set the primary content to be text/html
                    email.mixed_subtype = 'related'  # it is an important part that ensures embedding of an image
                    with open(image_path, mode='rb') as f:
                        image = MIMEImage(f.read())
                        email.attach(image)
                        image.add_header('Content-ID', f"<{image_name}>")
                email.send()

            # send an test email
            send_email(subject=subject, text_content=text_message, html_content=html_message, sender=sender,
                       recipient=recipient, image_path=image_path, image_name=image_name)
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    current_user = request.user
    print(current_user)
    #place = UserDummy.objects.get(author=current_user)
    qs = Ratings.objects.filter(author=current_user)
    print(qs)
    x = [x.contest for x in qs]
    y = [y.rating for y in qs]
    chart = get_plot(x, y)
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'chart':chart,
    }

    return render(request, 'users/profile.html', context)
def ratings_view(request,id):
    current_user=request.user
    qs=Ratings.objects.filter(author=id)
    print(qs)
    x=[x.contest for x in qs]
    y=[y.rating for y in qs]
    chart=get_plot(x,y)
    return render(request,'users/profile.html',{'chart':chart})