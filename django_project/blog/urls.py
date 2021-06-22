from django.conf.urls import url
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,

    KLHub,
memesView,
Internships
)
from . import views
from .views import *
urlpatterns = [
    path('discussionforum/', PostListView.as_view(), name='blog-home'),
    url(r'^user/(?P<username>\w{0,50})/$', UserPostListView.as_view(), name='user-posts'),

    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
   #path('goodies/',views.goodies,name='goodies'),
    path('',views.homepage,name='homepage'),
path('opportunities',views.opportunities,name='opp'),
path('internships',views.opportunitiesIntern,name='in'),
    path('mockInterviews/', views.mock, name='mock'),
    path('courses/', views.CoursesInterviews, name='courses'),
    path('paint/', views.paint, name='paint'),
    path('contact/',views.contact,name='contact'),

    path('memes/', views.memes, name='memes'),
    path('addMeme/',views.addMemes,name='addMemes'),

    path('addAnnouncement/', views.addAnnouncement, name='addAnnouncement'),
    url(r'^addFile/(?P<id>\d+)/$', views.addFile, name='addFile'),

    url(r'^files/(?P<id>\d+)/$',views.Showfiles,name='Showfiles'),
    url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
    url(r'^deleteCourseinKLHub/(?P<id>\d+)/$', views.deleteCourseinKLHub, name='deleteCourseinKLHub'),
    url(r'^deleteMemes/(?P<id>\d+)/$', views.deleteMemes, name='deleteMemes'),
    url(r'^deleteFellowship/(?P<id>\d+)/$', views.deleteFellowship, name='deleteFellowship'),

    url(r'^deleteInternship/(?P<id>\d+)/$', views.deleteInternship, name='deleteInternship'),
    url(r'^deleteScholarship/(?P<id>\d+)/$', views.deleteScholarship, name='deleteScholarship'),
    url(r'^deleteContent/(?P<id>\d+)/$', views.deletecontent, name='deletecontent'),
url(r'^deletecontentinKL/(?P<id>\d+)/$', views.deletecontentinKL, name='deletecontentinKL'),

url(r'^deleteAnnouncement/(?P<id>\d+)/$', views.deleteAnnouncement, name='deleteAnnouncement'),




    url(r'^deleteContest/(?P<id>\d+)/$', views.deleteContest, name='deleteContest'),
    url(r'^showContent/(?P<id>\d+)/$', views.showContent, name='showContent'),
    url(r'^addCourseContent/(?P<id>\d+)/$',views.addCourseContent,name='addCourseContent'),




    path('addFellowship/',views.addFellowship,name='addFellowship'),
    path('addInternship/', views.addInternship, name='addInternship'),
    path('addScholarship/', views.addScholarship, name='addScholarship'),




    url(r'^addContestContent/(?P<id>\d+)/$', views.addContestContent, name='addContestContent'),
    url(r'^contestDesc/(?P<id>\d+)/$', views.contestDesc, name='contestDesc'),

    path('goodies/', views.goodies, name='goodies'),
    path('KL-Hub/', views.KLHub, name='klu'),
path('contests/',views.contests,name='contests'),
    path('practice/',views.practice,name='practice'),
path('submit/',views.addurl,name='submit'),
    path('addCourse/',views.addCourse,name='addCourse'),
    path('addCourses/', views.klcourse, name='kluniversity'),
path('addContest/',views.addContest,name='addContest'),
path('addGifts/',views.addGifts,name='addgifts'),



path('thankyou/',views.thankyou,name='thankyou'),
    path('practice/sortup/', views.sortup, name='sortup'),
path('practice/sortdown/', views.sortdown, name='sortdown'),


    path('cf/', views.index, name="index"),
    path('logincf/', views.login, name="userPage"),
    path('refresh/', views.login, name="refresh"),
    path('contestscf/', views.futureContests, name="contestsTemplates"),

]
