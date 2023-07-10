from multiprocessing import context,get_context
from urllib import request
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import EditForm, Post_form,UpdateProfileForm
from django.contrib.auth.models import User
from .models import Post,FollowersCount, Profile
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView,DeleteView,View
from django.urls import reverse_lazy,reverse
from django.core.mail import send_mail




# Create your views here.
class indexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all().order_by('-id')
        return context
    


def profile( request):
    users = User.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    current_user =request.user
    for user in users:
        user=User.objects.get(username=request.user.username)
        logged_in_user=user
    user_followers=len(FollowersCount.objects.filter(user=current_user))
    user_following=len(FollowersCount.objects.filter(follower=current_user))
    user_followers0=FollowersCount.objects.filter(user=current_user)
    user_followers1=[]
    for i in user_followers0:
        user_followers0=i.follower
        user_followers1.append(user_followers0)
    if logged_in_user in user_followers1:
        follow_button_value='unfollow'
    else:
        follow_button_value='follow'

    context1= {'follow_button_value': follow_button_value,'current_user':current_user,'user_following':user_following,'user_followers':user_followers,'posts':posts,'users':users}
    context = context1
        
    return  render(request,'profile.html', context)   





def signup_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user = authenticate( username=username, password=password)
            user.save()
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'an error occurred while creating')

    return render(request,'signup.html',{'form':form})


def story(request):
    return render(request, 'story.html')

def login_user(request):
    return render(request, 'login_user.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditForm(request.POST, instance=request.user)
        form1 = UpdateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid() and form1.is_valid():
            form.save()
        
            form1.save()
            messages.success(request, 'you have successfully edited your profile')
            return redirect('profile')
    else:
        form = EditForm(instance=request.user)
        form1 = UpdateProfileForm(request.POST, instance=request.user.profile)
        context = {'form': form,'form1': form1}

    return render(request, 'edit_profile.html',context) 
def post_list(self):
    
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('-id')
    return posts
    

class post_detail(CreateView):
    template_name = 'post_details.html'
    model =Post
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    fields= ('title','text','created_date')

    
class update_view(UpdateView):
    template_name = 'update_post.html'
    model =Post
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    fields= ('title','text','created_date')

class article_view(DetailView):
    template_name = 'article_view.html'
    model=Post
    
def follwers_count(request):
    if request.method == 'POST':
        value= request.POST['value']
        user= request.POST['user']
        follower= request.POST['follower']
        if value =='follow':
            followers_cnt = FollowersCount.objects.create(follower = follower,user = user)
            followers_cnt.save()
        else:
            followers_cnt = FollowersCount.objects.get(follower = follower,user = user)
            followers_cnt.delete()
            
        return redirect('/?user='+user)
class delete_view(DeleteView):
    template_name = 'delete_view.html'
    model=Post  
    success_url= reverse_lazy('profile')
# # def logout(request):
#     logout(request)
#     return redirect('index')