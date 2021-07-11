from django.urls import path
from .candidate_views import CandIndex,CandProfile,Addphoto,JobView,JobDetail,Apply,CandApplied,FeeDBack,Reply,AcceptedJobs,MyReport

urlpatterns=[
    path('',CandIndex.as_view()),
    path('profile',CandProfile.as_view()),
    path('photo',Addphoto.as_view()),
    path('jobs',JobView.as_view()),
    path('details',JobDetail.as_view()),
    path('apply',Apply.as_view()),
    path('appliedjobs',CandApplied.as_view()),
    path('feedback',FeeDBack.as_view()),
    path('reply',Reply.as_view()),
    path('jobstatus',AcceptedJobs.as_view()),
    path('myreports',MyReport.as_view())
]