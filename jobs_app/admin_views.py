from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView,View

from accounts.views import CompReg,CanReg
from .models import JobDetails, JobsApplied, FeedBack


class AdminIndex(TemplateView):
    template_name = 'admin/adindex.html'

class CompApprove(TemplateView):
    template_name = 'admin/comp-approve.html'
    def get_context_data(self, **kwargs):

        context = super(CompApprove, self).get_context_data(**kwargs)

        company= CompReg.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')
        context['company']=company
        return context

class CandApprove(TemplateView):
    template_name = 'admin/cand-approve.html'
    def get_context_data(self, **kwargs):

        context = super(CandApprove, self).get_context_data(**kwargs)

        candidate= CanReg.objects.filter(user__last_name='0', user__is_staff='0', user__is_active='1')
        context['candidate']=candidate
        return context

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):

        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return redirect(request.META['HTTP_REFERER'])


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return redirect(request.META['HTTP_REFERER'])

class ViewCand(TemplateView):
    template_name = 'admin/cand-view.html'
    def get_context_data(self, **kwargs):

        context = super(ViewCand, self).get_context_data(**kwargs)

        candidate= CanReg.objects.filter(user__last_name='1', user__is_staff='0', user__is_active='1')
        context['candidate']=candidate
        return context

class ViewComp(TemplateView):
    template_name = 'admin/comp-view.html'
    def get_context_data(self, **kwargs):

        context = super(ViewComp, self).get_context_data(**kwargs)

        company= CompReg.objects.filter(user__last_name='1', user__is_staff='0', user__is_active='1')
        context['company']=company
        return context

class CandDetails(TemplateView):
    template_name = 'admin/cand-details.html'

    def dispatch(self, request, *args, **kwargs):
        cid = request.GET['id']

        cand = CanReg.objects.filter(user_id=cid)

        return render(request,'admin/cand-details.html',{'cand':cand})

class CompDetails(TemplateView):
    template_name = 'admin/comp-details.html'

    def dispatch(self, request, *args, **kwargs):
        cid = request.GET['id']

        comp = CompReg.objects.filter(user_id=cid)

        return render(request,'admin/comp-details.html',{'comp':comp})

class Jobslist(TemplateView):
    template_name = 'admin/comp-jpost.html'

    def get_context_data(self, **kwargs):

        context = super(Jobslist, self).get_context_data(**kwargs)

        jobs = JobDetails.objects.filter(hide=0)
        context['jobs']=jobs
        return context

class DetailsJob(TemplateView):
    template_name = 'admin/job-details.html'

    def dispatch(self, request, *args, **kwargs):
        jid = request.GET['id']
        job = JobDetails.objects.filter(id=jid)

        return render(request,'admin/job-details.html',{'details':job})

class SelectedCan(TemplateView):
    template_name = 'admin/cand-sel.html'

    def get_context_data(self, **kwargs):
        context = super(SelectedCan, self).get_context_data(*kwargs)
        candidate = JobsApplied.objects.all()
        context['sel'] = candidate
        return context

class FeeDBack(TemplateView):
    template_name = 'admin/feedback-view.html'
    def get_context_data(self, **kwargs):
        context = super(FeeDBack, self).get_context_data(*kwargs)
        feedback = FeedBack.objects.filter()
        context['feedback'] = feedback
        return context

    def post(self,request,*args,**kwargs):
        reply = request.POST['reply']
        hidden = request.POST['hidden']
        repl = FeedBack.objects.get(id=hidden)
        repl.reply = reply
        repl.save()
        return redirect(request.META['HTTP_REFERER'])








