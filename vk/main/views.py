import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from .models import User, Post, Comment, UserProfile, Friend
from .forms import RegisterForm, LoginForm, PostForm, CommentForm

@login_required
def index(request):
    return render(request, 'index.html', {'user': request.user, 'friends': Friend.objects.filter(to_user_id=request.user.id)})

def userprofile(request, index):
    return render(request, 'profilePage.html', {'user': UserProfile.objects.get(user_id=index), 'posts': Post.objects.filter(user=UserProfile.objects.get(user_id=index)), 'currentUser': request.user})

def add_post(request, index):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = UserProfile(id=index)
            post.publication_date = str(datetime.time)
            post.save()

            return redirect('userprofile', index)
            #return render(request, 'profilePage.html', {'user': UserProfile.objects.get(user_id=index), 'posts': Post.objects.filter(user=UserProfile.objects.get(user_id=index))})
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})

def delete_post(request, index):
    post = get_object_or_404(Post, id=index)
    user_id = post.user.id
    post.delete()

    return redirect('userprofile', user_id)

def add_friend(request, index):
    friend = Friend(from_user=UserProfile.objects.get(user=request.user), to_user=UserProfile.objects.get(id=index))
    friend.save()
    return redirect('userprofile', index)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()

            userProfile = UserProfile(user=user)
            userProfile.save()
            login(request, user)  # Log in the new user
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})