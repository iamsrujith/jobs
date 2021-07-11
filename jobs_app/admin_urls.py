from django.urls import path
from .admin_views import AdminIndex,CompApprove,CandApprove,ApproveView,RejectView,ViewCand,ViewComp,CandDetails, \
    CompDetails,Jobslist,DetailsJob,SelectedCan,FeeDBack


urlpatterns=[
    path('',AdminIndex.as_view()),
    path('aprcom',CompApprove.as_view()),
    path('aprcan',CandApprove.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('companies',ViewComp.as_view()),
    path('candidates',ViewCand.as_view()),
    path('viewdetails',CandDetails.as_view()),
    path('viewdetail',CompDetails.as_view()),
    path('jobs',Jobslist.as_view()),
    path('details',DetailsJob.as_view()),
    path('appliedcan',SelectedCan.as_view()),
    path('feedback',FeeDBack.as_view())
    ]