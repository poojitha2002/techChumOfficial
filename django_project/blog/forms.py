from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import ModelForm
from django.contrib.auth import authenticate, get_user_model
from .models import  * #Contest,ContestSubmission,CoursesForInterviews,CoursesForInterviewsContent,ContestQuestions,Resource,Internships,Fellowships,Scholorships,gifts,Memes
class ContactForm(forms.Form):
    name=forms.CharField(max_length=100)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class ContestStart(ModelForm):
    class Meta:
        model=Contest
        fields="__all__"

class ContestQuestionsForm(ModelForm):
    class Meta:
        model=ContestQuestions
        fields="__all__"

class ContestForm(ModelForm):
    class Meta:
        model = ContestSubmission
        fields = ['url']

class InterviewCoursesForm(ModelForm):
    class Meta:
        model=CoursesForInterviews
        fields="__all__"

class KLCourseForm(ModelForm):
    class Meta:
        model=KLCourse
        fields="__all__"



class InternshipForm(ModelForm):
    class Meta:
        model=Internships
        fields=['url']

class ScholarshipForm(ModelForm):
    class Meta:
        model=Scholorships
        fields=['url']

class FellowshipForm(ModelForm):
    class Meta:
        model=Fellowships
        fields=['url']

class GiftsForm(ModelForm):
    class Meta:
        model=gifts
        fields="__all__"

class CodeforcesHandleForm(forms.Form):
    handle=forms.CharField(max_length=200)

class CoursesForInterviewsContentForm(ModelForm):
    class Meta:
        model=CoursesForInterviewsContent
        fields="__all__"


class MemesForm(ModelForm):
    class Meta:
        model=Memes
        fields="__all__"


class Files(ModelForm):
    class Meta:
        model=Allfiles
        fields="__all__"

class AnnouncementsForm(ModelForm):
    class Meta:
        model=Announcements
        fields="__all__"