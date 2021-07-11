from django.urls import path
from accounts import views
from .views import CompanyReg,CandidateReg,LoginView,Logout


urlpatterns=[
    path('compreg',CompanyReg.as_view()),
    path('candreg',CandidateReg.as_view()),
    path('login/',LoginView.as_view()),
    path('logout',views.Logout,name='logout')

]