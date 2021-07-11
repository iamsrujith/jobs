from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View
from accounts.models import CanReg,CompReg,UserType
from .models import JobDetails,JobsApplied,FeedBack,JobReport


class CandIndex(TemplateView):
    template_name = 'candidate/cand-index.html'

class CandProfile(TemplateView):
    template_name = 'candidate/cand-profile.html'
    def get_context_data(self, **kwargs):
        context = super(CandProfile,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            candidate = CanReg.objects.filter(user_id=self.request.user.id)
            context['candidate'] =candidate
        return context

    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        candidate = CanReg.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":

            user.first_name= request.POST['name']
            user.email = request.POST['email']
            user.username = request.POST['username']
            user.save()
            file_res = FileSystemStorage()
            resume = request.FILES['resume']
            res = file_res.save(resume.name,resume)
            candidate.resume = res
            candidate.contact = request.POST['phone_no']
            candidate.address = request.POST['address']
            candidate.place = request.POST['place']
            candidate.desc = request.POST['desc']
            candidate.qual = request.POST['qual']
            candidate.workexp = request.POST['workexp']
            candidate.skills = request.POST['skills']
            candidate.gender = request.POST['gender']
            candidate.save()
            return redirect(request.META['HTTP_REFERER'],{'message':"Profile Updated"})
        else:
            user.set_password(request.POST['password'])
            user.save()
            return redirect(request.META['HTTP_REFERER'],{'message':"Password Updated"})

class Addphoto(TemplateView):
    template_name = 'candidate/cand-photo.html'
    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        candidate = CanReg.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":

            user.username = 'candidate'
            user.save()
            img = request.FILES['image']
            file = FileSystemStorage()
            image = file.save(img.name,img)
            candidate.photo = image
            candidate.save()
            return redirect('/candidate/profile')

class JobView(TemplateView):
    template_name = 'candidate/cand-jobs.html'

    def get_context_data(self, **kwargs):

        context = super(JobView, self).get_context_data(**kwargs)
        jobs = JobDetails.objects.filter(hide=0)
        context['jobs']=jobs
        return context

class JobDetail(TemplateView):
    template_name = 'candidate/cand-jdetail.html'

    def dispatch(self, request, *args, **kwargs):
        jid = request.GET['id']
        job = JobDetails.objects.filter(id=jid,hide=0)

        return render(request,'candidate/cand-jdetail.html',{'job':job})

class Apply(View):
    def dispatch(self, request, *args, **kwargs):

        jid=request.GET['id']
        job = JobDetails.objects.get(id=jid)
        com = CompReg.objects.get(id=job.comp_id)
        can = CanReg.objects.get(user_id=self.request.user.id)

        jobs = JobsApplied()
        jobs.cand = can
        jobs.job = job
        jobs.com = com
        jobs.save()

        return render(request,'candidate/cand-jobs.html')

class CandApplied(TemplateView):
    template_name = 'candidate/cand-applied.html'

    def get_context_data(self, **kwargs):
        context = super(CandApplied,self).get_context_data(**kwargs)
        if self.request.user.is_active:
            candidate = JobsApplied.objects.filter(cand__user_id=self.request.user.id)
            context['candidate'] =candidate
        return context
class FeeDBack(TemplateView):
    template_name = 'candidate/cand-feedback.html'

    def post(self,request,*args,**kwargs):

        feedback = request.POST['feedback']
        user = CanReg.objects.get(user_id=self.request.user.id)
        type = UserType.objects.get(user_id=self.request.user.id)
        feed = FeedBack()
        feed.feedback = feedback
        feed.candidate = user
        feed.usertype = type
        feed.save()
        return redirect('/candidate')

class Reply(TemplateView):
    template_name = 'candidate/cand-reply.html'
    def get_context_data(self, **kwargs):
        context = super(Reply, self).get_context_data(**kwargs)
        reply = FeedBack.objects.filter(candidate_id__user_id=self.request.user.id)
        context['reply'] = reply
        return context

class AcceptedJobs(TemplateView):
    template_name = 'candidate/cand-accepted.html'
    def get_context_data(self, **kwargs):
        context = super(AcceptedJobs, self).get_context_data(**kwargs)
        jobs = JobsApplied.objects.filter(selected='selected',cand__user_id=self.request.user.id)
        context['jobs'] = jobs
        return context

    def post(self,request,*args,**kwargs):
        status = request.POST['status']
        file = request.FILES['file']
        hidden = request.POST['hidden']

        job = JobsApplied.objects.get(id=hidden)
        cand = CanReg.objects.get(user_id=self.request.user.id)
        report = JobReport()
        report.status = status
        files = FileSystemStorage()
        filee = files.save(file.name,file)
        report.report = filee
        report.jobs=job
        report.candidate = cand
        report.save()
        return redirect(request.META['HTTP_REFERER'])

class MyReport(TemplateView):
    template_name = 'candidate/cand-report.html'

    def get_context_data(self, **kwargs):
        context = super(MyReport, self).get_context_data(**kwargs)
        report = JobReport.objects.filter(candidate_id__user_id=self.request.user.id)
        context['report']=report
        return context