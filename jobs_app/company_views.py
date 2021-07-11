from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.base import View

from accounts.models import CompReg, UserType
from .models import JobDetails, JobsApplied, CanReg, FeedBack, JobReport


class CompIndex(TemplateView):
    template_name = 'company/comp-index.html'

class CompProfile(TemplateView):
    template_name = 'company/comp-profile.html'
    def get_context_data(self, **kwargs):
        context = super(CompProfile,self).get_context_data(**kwargs)
        context['user'] = self.request.user
        if self.request.user.is_active:
            company = CompReg.objects.filter(user_id=self.request.user.id)
            context['company'] =company
        return context

    def post(self,request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        company = CompReg.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":

            user.first_name= request.POST['name']
            user.email = request.POST['email']
            user.username = request.POST['username']
            user.save()
            company.contact = request.POST['phone_no']
            company.address = request.POST['address']
            company.place = request.POST['place']
            company.Desc = request.POST['desc']
            company.comtype = request.POST['ctype']
            company.NofEmp = request.POST['noe']
            company.RegDate = request.POST['regdate']
            company.rnum = request.POST['rnum']
            company.save()
            return redirect(request.META['HTTP_REFERER'],{'message':"Profile Updated"})
        else:
            user.set_password(request.POST['password'])
            user.save()
            return redirect(request.META['HTTP_REFERER'],{'message':"Password Updated"})

class AddJob(TemplateView):
    template_name = 'company/comp-addjob.html'

    def post(self,request,*args,**kwargs):

        co = CompReg.objects.get(user_id=self.request.user.id)
        title = request.POST['title']
        type = request.POST['type']
        clength = request.POST['clength']
        salary = request.POST['salary']
        qual = request.POST['qual']
        desc = request.POST['desc']
        wrkexp = request.POST['wrkexp']
        jobreq = request.POST['jobreq']

        job = JobDetails()
        job.jtitle = title
        job.jtype = type
        job.clength = clength
        job.salary = salary
        job.qualreq = qual
        job.desc = desc
        job.comp = co
        job.wrkexp = wrkexp
        job.jobreq = jobreq
        job.save()
        return redirect(request.META['HTTP_REFERER'], {'message': "Job added"})

class AppliedCan(TemplateView):
    template_name = 'company/comp-applied.html'

    def get_context_data(self, **kwargs):
        context = super(AppliedCan,self).get_context_data(**kwargs)
        if self.request.user.is_active:
            company = JobsApplied.objects.filter(com__user_id=self.request.user.id,selected="")
            context['company'] =company
        return context

class PostedJobs(TemplateView):
    template_name = 'company/comp-jobs.html'

    def get_context_data(self, **kwargs):
        context = super(PostedJobs,self).get_context_data(**kwargs)
        if self.request.user.is_active:
            company = JobDetails.objects.filter(comp__user_id=self.request.user.id,hide=0)
            context['company'] =company
        return context

class JobDetail(TemplateView):
    template_name = 'company/comp-jdetail.html'

    def dispatch(self, request, *args, **kwargs):
        jid = request.GET['id']
        job = JobDetails.objects.filter(id=jid)

        return render(request,'company/comp-jdetail.html',{'job':job})

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        job = JobDetails.objects.get(id=id)
        job.hide = '1'
        job.save()
        return redirect('/company/jobs')

class CandDetails(TemplateView):
    template_name = 'company/comp-candetails.html'

    def dispatch(self, request, *args, **kwargs):
        cid = request.GET['id']

        cand = CanReg.objects.filter(user_id=cid)

        return render(request,'company/comp-candetails.html',{'cand':cand})

class AcceptCand(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        job = JobsApplied.objects.get(id=id)
        job.selected = 'selected'
        job.message = 'you have your interview in 3 days'
        job.save()
        return redirect(request.META['HTTP_REFERER'])

class RejectCand(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        job = JobsApplied.objects.get(id=id)
        job.selected = 'rejected'
        job.message = 'sorry not qualified'
        job.save()
        return redirect(request.META['HTTP_REFERER'])


class AcceptedCan(TemplateView):
    template_name = 'company/comp-accepted.html'

    def get_context_data(self, **kwargs):
        context = super(AcceptedCan,self).get_context_data(**kwargs)
        if self.request.user.is_active:
            company = JobsApplied.objects.filter(com__user_id=self.request.user.id,selected="selected")
            context['company'] =company
        return context

class FeeDBack(TemplateView):
    template_name = 'company/comp-feedback.html'

    def post(self,request,*args,**kwargs):

        feedback = request.POST['feedback']
        user = CompReg.objects.get(user_id=self.request.user.id)
        type = UserType.objects.filter(user_id=self.request.user.id)
        feed = FeedBack()
        feed.feedback = feedback
        feed.usertype = type
        feed.company = user
        feed.save()
        return redirect('/company')

class Reply(TemplateView):
    template_name = 'company/comp-reply.html'
    def get_context_data(self, **kwargs):
        context = super(Reply, self).get_context_data(**kwargs)
        reply = FeedBack.objects.filter(company_id__user_id=self.request.user.id)
        context['reply'] = reply
        return context

class MyReport(TemplateView):
    template_name = 'company/comp-report.html'

    def get_context_data(self, **kwargs):
        context = super(MyReport, self).get_context_data(**kwargs)
        report = JobReport.objects.filter(jobs__com__user_id=self.request.user.id)
        context['report']=report
        return context

class Addphoto(TemplateView):
    template_name = 'company/comp-photo.html'
    def post(self,request,*args,**kwargs):
        company = CompReg.objects.get(user_id=self.request.user.id)
        if request.POST['profile'] == "profile":
            img = request.FILES['image']
            file = FileSystemStorage()
            image = file.save(img.name,img)
            company.logo = image
            company.save()
            return redirect('/company/profile')