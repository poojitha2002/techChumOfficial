from django.contrib import admin
from .models import Post,Courses,Memes,Scholorships,ScholorshipTrack,Allfiles,Internships,Fellowships,Contest,ContestQuestions,Goodies,gifts,ContestSubmission,Codeforces,CoursesForInterviews,CoursesForInterviewsContent,clgModel

admin.site.register(Post)
admin.site.register(Courses)
admin.site.register(Memes)
admin.site.register(Scholorships)
admin.site.register(ScholorshipTrack)
admin.site.register(Allfiles)
admin.site.register(Internships)
admin.site.register(Fellowships)
admin.site.register(Contest)
admin.site.register(ContestQuestions)
admin.site.register(clgModel)
admin.site.register(Goodies)

admin.site.register(Codeforces)
admin.site.register(ContestSubmission)

admin.site.register(gifts)

admin.site.register(CoursesForInterviews)
admin.site.register(CoursesForInterviewsContent)

