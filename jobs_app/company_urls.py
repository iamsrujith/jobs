from django.urls import path
from .company_views import CompIndex,CompProfile,AddJob,AppliedCan,PostedJobs,JobDetail,RejectView,CandDetails, \
    AcceptCand,RejectCand,AcceptedCan,FeeDBack,Reply,MyReport,Addphoto

urlpatterns=[
    path('',CompIndex.as_view()),
    path('profile',CompProfile.as_view()),
    path('addjob',AddJob.as_view()),
    path('aplist',AppliedCan.as_view()),
    path('jobs',PostedJobs.as_view()),
    path('details',JobDetail.as_view()),
    path('delete',RejectView.as_view()),
    path('viewdetails',CandDetails.as_view()),
    path('accept',AcceptCand.as_view()),
    path('reject',RejectCand.as_view()),
    path('accepted',AcceptedCan.as_view()),
    path('feedback',FeeDBack.as_view()),
    path('reply',Reply.as_view()),
    path('reports',MyReport.as_view()),
    path('addphoto',Addphoto.as_view())

]