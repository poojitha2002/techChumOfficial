from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage
from datetime import datetime
from operator import itemgetter
from .utils import get_plot9,get_plot10
# Import mimetypes module
import mimetypes
# import os module
import os

from .forms import *#ContactForm,ContestForm,InterviewCoursesForm,CoursesForInterviewsContentForm,ContestStart,ContestQuestionsForm,ResourceForms,InternshipForm,FellowshipForm,ScholarshipForm,CodeforcesHandleForm,GiftsForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import requests
from .models import Courses,Memes,Scholorships,Internships,ScholorshipTrack,Fellowships,Allfiles,Goodies,Contest,ContestQuestions,ContestSubmission,CoursesForInterviews,CoursesForInterviewsContent,gifts
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from  blog.extraMethods import userDetails, convertUnixTime, getTags, contestDetails

# Create your views here.

@login_required
def index(request):
    return render(request, 'blog/login.html', {'giveError': False})



def login(request):
    userInfo = False
    if('refresh' in request.POST):
        userInfo = userDetails(request.POST.get('username'), False)
    else:
        userInfo = userDetails(request.POST.get('username'), True)

    if(userInfo == False):
        return render(request, 'blog/login.html', {'giveError': True})

    dt_object = convertUnixTime(userInfo['lastOnlineTimeSeconds'])

    weakTags = getTags(userInfo['handle'], userInfo['rating'])
    verdict = []
    response = requests.get('https://codeforces.com/api/user.status?handle=' + request.POST.get('username')).json()
    for i in response['result']:
        verdict.append(i['verdict'])
    counter = Counter(verdict)
    print(counter)
    label = []
    data = []
    for verdict, count in counter.items():
        label.append(verdict)
        data.append(count)
    chart = get_plot9(label, data,data)
    verdict=[]
    res=response['result']
    for i in res:
        if i['verdict']=="OK":
            for j in (i['problem']['tags']):
                verdict.append(j)
    counter = Counter(verdict)
    print(counter)
    label = []
    data = []
    for verdict, count in counter.items():
        label.append(verdict)
        data.append(count)
    chart1 = get_plot10(label, data, data)
    return render(request, 'blog/profile.html', {'user': userInfo, 'lastOnline': dt_object, 'tags': weakTags,'chart':chart,'chart1':chart1})


def cf(request):
    return render(request,'blog/cfviz.html')

def futureContests(request):
    contestsList = contestDetails()
    return render(request, 'blog/cfcontests.html', {'contests': contestsList})


def homepage(request):
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    announcement = Announcements.objects.all()
    return render(request,'blog/homepage.html',{'c':c,'announcement':announcement})

@login_required
def home(request):

    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

@login_required
def mock(request):
    return render(request,'blog/mock.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class memesView(ListView):
    model=Memes
    template_name='blog/memes.html'
    context_object_name = 'memes'

@login_required
class ScholorshipsView(ListView):
    model=Scholorships
    template_name = 'blog/opportunities.html'
    context_object_name = 'scholorships'



@login_required

def opportunities(request):
    scholorships=Scholorships.objects.all()
    internships=Internships.objects.all()
    fellowships=Fellowships.objects.all()
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    context={'scholorships':scholorships,'internships':internships,'fellowships':fellowships,'c':c}
    return render(request,'blog/opportunities.html',context)

@login_required
def CoursesInterviews(request):
    user=str(request.user)
    courses=CoursesForInterviews.objects.all()
    #print("user= ",user)
    c=0
    if user=='poojitha':
        c=1
    #print(c)
    #print(type(user))
    context={'courses':courses,'c':c}
    return render(request,'blog/courses.html',context)

@login_required
def memes(request):
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    content=Memes.objects.all()
    context={'content':content,'c':c}
    return render(request,'blog/memes.html',context)

@login_required
def showContent(request,id):
    user = str(request.user)
    content=CoursesForInterviewsContent.objects.filter(course=id)
    c = 0
    if user == 'poojitha':
        c = 1
    context={'content':content,'c':c,'id':id}
    return render(request,'blog/coursecontent.html',context)


@login_required
def addCourse(request):
    if request.method=='POST':
        form=InterviewCoursesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your Course was Added ')
            return redirect('courses')
    else:
        form=InterviewCoursesForm()
    return render(request,'blog/addCourse.html',{'form':form})

def addAnnouncement(request):
    if request.method=='POST':
        form=AnnouncementsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Announcement Posted!')
            return redirect('homepage')
    else:
        form=AnnouncementsForm()
    return render(request,'blog/addAnnouncement.html',{'form':form})


@login_required
def KLHub(request):
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    content = KLCourse.objects.all()
    context = {'content': content, 'c': c}
    return render(request, 'blog/kl.html', context)


@login_required
def klcourse(request):
    if request.method=='POST':

        form=KLCourseForm(request.POST,request.FILES)
        if form.is_valid():
            print("Saved")
            form.save()
            messages.success(request,f'Your Course was Added ')
            return redirect('klu')
    else:
        form=KLCourseForm()
    return render(request,'blog/addCourse1.html',{'form':form})

@login_required
def addGifts(request):
    if request.method=='POST':
        form=GiftsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,f'Your gift was Added ')
            return redirect('goodies')
    else:
        form=GiftsForm()
    return render(request,'blog/addGifts.html',{'form':form})

@login_required
def addMemes(request):
    if request.method=='POST':
        form=MemesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Meme was Added ')
            return redirect('memes')
    else:
        form=MemesForm()
    return render(request,'blog/addMeme.html',{'form':form})


@login_required
def addContest(request):
    if request.method=='POST':
        form=ContestStart(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            #x=CoursesForInterviews(courseName=courseName,image=image,content=content)
            x.save()

            messages.success(request,f'Contest was Added ')
            return redirect('contests')
    else:
        form=ContestStart()
    return render(request,'blog/addContest.html',{'form':form})

@login_required
def addInternship(request):
    if request.method=='POST':
        form=InternshipForm(request.POST,request.FILES)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            x=Internships.objects.create(url=url)
            #x=CoursesForInterviews(courseName=courseName,image=image,content=content)
            x.save()

            messages.success(request,f'Internship was Added ')
            return redirect('opp')
    else:
        form=InternshipForm()
    return render(request,'blog/addInternship.html',{'form':form})


@login_required
def addFellowship(request):
    if request.method=='POST':
        form=FellowshipForm(request.POST,request.FILES)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            x=Fellowships.objects.create(url=url)
            #x=CoursesForInterviews(courseName=courseName,image=image,content=content)
            x.save()

            messages.success(request,f'Fellowship was Added ')
            return redirect('opp')
    else:
        form=FellowshipForm()
    return render(request,'blog/addFellowship.html',{'form':form})

@login_required
def addScholarship(request):
    if request.method=='POST':
        form=ScholarshipForm(request.POST,request.FILES)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            x=Scholorships.objects.create(url=url)
            #x=CoursesForInterviews(courseName=courseName,image=image,content=content)
            x.save()

            messages.success(request,f'Scholarship was Added ')
            return redirect('opp')
    else:
        form=ScholarshipForm()
    return render(request,'blog/addScholarship.html',{'form':form})




@login_required
def addCourseContent(request,id):
    if request.method=='POST':
        form=CoursesForInterviewsContentForm(request.POST,request.FILES)
        if form.is_valid():
            course=form.cleaned_data.get('course')
            day=form.cleaned_data.get('day')
            content=form.cleaned_data.get('content')
            x=CoursesForInterviewsContent.objects.create(course=course,day=day,content=content)
            #x=CoursesForInterviews(courseName=courseName,image=image,content=content)
            x.save()

            messages.success(request,f'Your Content was Added ')
            return redirect('courses')
    else:
        form=CoursesForInterviewsContentForm()
    return render(request,'blog/addcoursecontent.html',{'form':form})



@login_required
def addContestContent(request,id):
    if request.method=='POST':
        form=ContestQuestionsForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            messages.success(request,f' Contest Questions were Added Successfully ')
            return redirect('contests')
    else:
        form=ContestQuestionsForm()
    return render(request,'blog/addcontestcontent.html',{'form':form})


@login_required
def sortup(request):
    response = requests.get('https://codeforces.com/api/problemset.problems').json()
    # print(response['result'])
    stuff = response['result']['problems']
    final = []
    for i in stuff:
        if 'rating' in i.keys():
            final.append(i)
    final= (sorted(final, key=lambda i: i['rating']))
    p = Paginator(final, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'items': page}
    return render(request, 'blog/practicesortup.html', context)

@login_required
def sortdown(request):
    response = requests.get('https://codeforces.com/api/problemset.problems').json()
    # print(response['result'])
    stuff = response['result']['problems']
    final = []
    for i in stuff:
        if 'rating' in i.keys():
            final.append(i)
    final= (sorted(final, key=lambda i: i['rating'],reverse=True))
    p = Paginator(final, 10)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)

    context = {'items': page}
    return render(request, 'blog/practicesortdown.html', context)


@login_required
def practice(request):
    response=requests.get('https://codeforces.com/api/problemset.problems').json()
    #print(response['result'])
    stuff=response['result']['problems']

    final=[]
    for i in stuff:
        if 'rating' in i.keys():
            final.append(i)

    p=Paginator(final,10)
    if request.method=="POST":
        some_var = request.POST.getlist('checks[]')
        print("Check boxes: \n",some_var)
        ll=request.POST['ll']
        ul=request.POST['ul']
        print("ll=",ll)
        print('ul= ',ul)

        if len(ll)!=0 and len(ul)!=0:
            stuff2 = []
            for i in final:
                if   i['rating'] >= int(ll) and i['rating'] <=int(ul):
                    stuff2.append(i)
            p=Paginator(stuff2,10)
        else:
            p=Paginator(final,10)


    page_num=request.GET.get('page',1)
    try:
        page=p.page(page_num)
    except EmptyPage:
        page=p.page(1)


    context={'items':page}
    return render(request,'blog/practice.html',context)


@login_required
def opportunitiesIntern(request):
    internships=Internships.objects.all()
    context={'internships':internships}
    return render(request,'blog/opportunities.html',context)

@login_required
def Showfiles(request,id):
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    allfiles=Allfiles.objects.filter(course=id)
    context={'allfiles':allfiles,'c':c,'id':id}
    return render(request,'blog/files.html',context)

@login_required
def addFile(request,id):
    if request.method=='POST':
        form=Files(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your File was Added ')
            return redirect('Showfiles',id)
    else:
        form=Files()
    return render(request,'blog/addFile.html',{'form':form})




@login_required
def delete(request,id):
    i=CoursesForInterviews.objects.filter(pk=id).delete()
    courses = CoursesForInterviews.objects.all()
    messages.success(request, f'Your Course was deleted successfully ')
    context = {'courses': courses }
    return redirect('courses')

@login_required
def deleteCourseinKLHub(request,id):
    i=KLCourse.objects.filter(pk=id).delete()
    courses = KLCourse.objects.all()
    messages.success(request, f'Your Course was deleted successfully ')
    context = {'courses': courses }
    return redirect('klu')

@login_required
def deleteMemes(request,id):
    i=Memes.objects.filter(pk=id).delete()
    messages.success(request,f'Meme deleted successfully')
    return redirect('memes')

@login_required
def deleteFellowship(request,id):
    i=Fellowships.objects.filter(pk=id).delete()
    messages.success(request, f'Fellowship was deleted successfully ')
    return redirect('opp')

@login_required
def deleteInternship(request,id):
    i=Internships.objects.filter(pk=id).delete()
    messages.success(request, f'Internship was deleted successfully ')
    return redirect('opp')

@login_required
def deleteScholarship(request,id):
    i=Scholorships.objects.filter(pk=id).delete()
    messages.success(request, f'Scholarship was deleted successfully ')
    return redirect('opp')
@login_required
def deletecontent(request,id):
    i=CoursesForInterviewsContent.objects.filter(pk=id).delete()
    messages.success(request, f'Your Course content was deleted successfully ')
    return redirect('showContent',id)

@login_required
def deletecontentinKL(request,id):
    i=Allfiles.objects.filter(pk=id).delete()
    messages.success(request, f'Your File was deleted successfully ')
    return redirect('Showfiles',id)
@login_required
def deleteAnnouncement(request,id):
    i=Announcements.objects.filter(pk=id).delete()
    messages.success(request, f'Your Announcement was deleted successfully ')
    return redirect('homepage')
@login_required
def deleteContest(request,id):
    i=Contest.objects.filter(pk=id).delete()
    messages.success(request, f'Your  contest was deleted successfully ')
    return redirect('contests')

@login_required
def contests(request):
    cont=Contest.objects.all()
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    context={'cont':cont,'c':c}
    return render(request,'blog/contests.html',context)
@login_required
def contestDesc(request,id):
    user = str(request.user)

    c1 = 0
    if user == 'poojitha':
        c1 = 1
    desc=ContestQuestions.objects.filter(contest=id)
    obj = Contest.objects.get(pk=id)
    c=0
    if obj.start.replace(tzinfo=None) <= datetime.now().replace(tzinfo=None) <= obj.end.replace(tzinfo=None):
        c=1
    print(c)
    context={'desc':desc,'c':c,'c1':c1,'id':id}
    return render(request,'blog/contestDesc.html',context)

@login_required
def addurl(request):
    if request.method=='POST':
        form=ContestForm(request.POST)
        if form.is_valid():
            current_user = request.user
            print(current_user)

            url=form.cleaned_data.get('url')
            x=ContestSubmission(author=current_user,url=url)
            x.save()

            messages.success(request,f'Your Submission was recorded ')
            return redirect('thankyou')
    else:
        form=ContestForm()
    return render(request,'blog/submit.html',{'form':form})

@login_required
def thankyou(request):
    return render(request,'blog/thanks.html')


@login_required
def goodies(request):
    vouchers = gifts.objects.all()
    current_user = request.user
    user = str(request.user)
    c = 0
    if user == 'poojitha':
        c = 1
    print(vouchers)
    print(current_user.username)
    good=Goodies.objects.filter(author=current_user.username)
    print(good)
    context={'good':good,'vouchers':vouchers,'c':c}

    return render(request,'blog/goodies.html',context)

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class GoodiesView:
    model=Goodies
    template_name='blog/goodies.html'
    context_object_name='goodies'

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Goodies.objects.filter(author=user)

class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
@login_required
def paint(request):
    return render(request,'blog/paint.html');
@login_required
def courses(request):
    return render(request,'blog/courses.html');

@login_required
def contact(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',message, settings.EMAIL_HOST_USER,['ravuri.poojitha123@gmail.com'], fail_silently=False)
	return render(request, 'blog/contactus.html')


@login_required
def viewScholorships(request):

    return render(request,'blog/opportunities.html',{'jlist':ScholorshipTrack.objects.all()})
