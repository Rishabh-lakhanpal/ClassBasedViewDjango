from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import StudentRegistration
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here. 

# This Class will Add new Item and Show all items
class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StudentRegistration()
        stud = User.objects.all()
        context = {
            'stu' : stud,
            'form' : form
        }
        return context

    def post(self, request):
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
    



class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args , **kwargs)
   

class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
        return render(request, 'enroll/updatestudent.html', {'form':form})
   
    def post(self,request, id):
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

