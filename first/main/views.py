import email
from imaplib import _Authenticator
from telnetlib import AUTHENTICATION, LOGOUT
from django.contrib.auth.mixins import UserPassesTestMixin

from email import headerregistry
from multiprocessing import AuthenticationError
from re import template
from django.shortcuts import get_object_or_404, render,redirect
from django.views import View
from . models import  City, Registration
from . models import Clothers
from .models import Food
from .models import Singers
from .models import Actors
from .models import Films
from .models import Posts
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import AddPostForm, SingersForm
from django.core.mail import EmailMessage
# from . models import Home
# from . models import Text
# def send_message(request):
#     send_mail("Welcome to testing page","My content","200103227@stu.sdu.edu.kz",["200103200@stu.sdu.edu.kz","200103200@stu.sdu.edu.kz"],
#               fail_silently=False,html_message="<b>Bold text </b> <i>Italic text </i>" )
 
    
#     return render (request,'main/successfull.html')
def send_message(request):
    email  = EmailMessage('welcome to testing page ' , 'Hello','200103227@stu.sdu.edu.kz',['200103288@stu.sdu.edu.kz','200103200@stu.sdu.edu.kz'],
    headers={'Message-ID':'main'},
    )
    email.attach_file('C:/Users/Acer/Pictures/photo.png')
    email.send(fail_silently=False)
    return render(request,'main/successfull.html')




def show_id(request, post_id):
    post=get_object_or_404(Posts, pk = post_id)
    context={'post':post}
    return render(request, 'main/post.html', context=context)

def show_post(request, post_slug):
    post = get_object_or_404(Posts, slug = post_slug)
    context = {'post':post}
    return render(request, 'main/post.html', context=context)

def index(request):
 tasks = City.objects.order_by('-id')[:1]
 return render(request, 'main/index.html',{"aktau": tasks})
# Create your views here.



def home(request):
#  task = New.objects.order_by('-id')[:1]
 return render(request, 'main/home.html')



def about(request):
 temp = Food.objects.order_by('-id')[:1]
 return render(request, 'main/about.html',{"balkaymak": temp})



def menu(request):
 task = Clothers.objects.order_by('-id')[:1]
 return render(request, 'main/menu.html', {"saykele": task})


def actors(request):
    actor = Actors.objects.order_by('-id')[:1]
    return render(request,'main/actors.html', {"actor": actor})


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            try:
                form.save()
                return redirect('login')
            except:
                form.add_error(None, 'Ошибка при выходе ')
    else:
        form = AddPostForm()
    return render (request,'main/login.html',{'form':form ,'username':'Welcome.Its your first time?' , 'password':'password'})


def films(request):
    movie = Films.objects.order_by('-id')[:1]
    return render(request, 'main/films.html', {"movie": movie})


def aboutus(request):
    return render(request, 'main/aboutus.html', {"aboutus": aboutus})


class NewsDeleteView(DeleteView):
    model = Singers
    success_url = '/singers/'
    template_name = 'main/delete.html'

class NewsUpdateView(UpdateView):
    model = Singers
    template_name = 'main/update.html'
    form_class = SingersForm
    
class NewsDetailView(DetailView):
    model = Singers
    template_name = 'main/details_view.html'
    context_object_name = 'singer'
def insert(request):
    error = ''
    if request.method == 'POST':
        form = SingersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/singers')
        else:
            error = 'Форма была неверной'
    form = SingersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/insert.html', data)

def singers(request):
    singer = Singers.objects.all()
    return render(request,'main/singers.html', {"singer": singer})

# class CustomerRegistrationView(CreateView):
#       template_name = 'login.html'
#       form_class = CustomerRegistrationForm
#       success_url = reverse_lazy('main')

#       def form_valid(self, form):
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password')
#            email = form.cleaned_data.get('email')
#            user = Registration.objects.create_user(username, email, password)
#            form.instance.user=user
#            login(self.request, user)
#            return super().form_valid(form)

# class CustomerRegistrationView(CreateView):
#       template_name = 'login.html'
#       form_class = CustomerRegistrationForm
#       success_url = reverse_lazy('main')

#       def form_valid(self, form):
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password')
#            email = form.cleaned_data.get('email')
#            user = Registration.objects.create_user(username, email, password)
#            form.instance.user=user
#            login(self.request, user)
#            return super().form_valid(form)
      
# class CustomerLogoutView(View):
#         def get(self, request):
#             LOGOUT(request)
#             return redirect('main')

# class CustomerLoginView(FormView):
#       template_name = 'login.html'
#       form_class = CustomerLoginForm
#       success_url = reverse_lazy('main')
#       def form_valid(self, form):
#             uname = form.cleaned_data.get('username')
#             pword = form.cleaned_data['password']
#             usr = _Authenticator(username=uname, password=pword)
#             if usr is not None and usr.customer:
#                 login(self.request, usr)
#             else:
#                  return render (self.request, 'login.html', {'form': CustomerLoginForm})
#             return super().form_valid(form)

