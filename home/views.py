from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import BlogPost, Category
from .forms import BlogForm, CategoryForm
from .models import Users
from .UsersForm import UsersForm
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import *

@login_required
@admin_or_editor
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_blogposts')
    else:
        form = BlogForm()

    return render(request, 'create_blogpost.html', {'form': form})


def list_blogposts(request):
    blogposts = BlogPost.objects.all()
    return render(request, 'list_blogposts.html', {'blogposts': blogposts})


@login_required
@admin_or_editor
def update_blogpost(request, id):
    blogpost = BlogPost.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            return redirect('list_blogposts')
    else:
        form = BlogForm(instance=blogpost)

    return render(request, 'update_blogpost.html', {'form': form})


@login_required
@admin_required
def delete_blogpost(request, id):
    blogpost = BlogPost.objects.get(id=id)
    blogpost.delete()
    return redirect('list_blogposts')


def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)

        form.save()
        return redirect('/')
    else:
        form = UsersForm()

    return render(request, 'create_user.html', {'form': form})


def update_user(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect('/')
    else:
        form = UsersForm(instance=user)

    return render(request, 'update_user.html', {'form': form})

def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/')


def list_user(request):
    users = Users.objects.all()
    return render(request,'dashboard1.html',{'users':users})


from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .models import BlogPost, Category
from .forms import BlogForm, CategoryForm
from .models import Users
from .UsersForm import UsersForm
from .models import Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import *

@login_required
@admin_or_editor
def create_blogpost(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_blogposts')
    else:
        form = BlogForm()

    return render(request, 'create_blogpost.html', {'form': form})


def list_blogposts(request):
    user_profile = UserProfile.objects.get(user=request.user)
    allowed_categories = user_profile.category.all()
    blogposts = BlogPost.objects.filter(category__in=allowed_categories)
    return render(request, 'list_blogposts.html', {'blogposts': blogposts})


@login_required
@admin_or_editor
def update_blogpost(request, id):
    blogpost = get_object_or_404(BlogPost, id=id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the blog post belongs to a category associated with the current user
    if blogpost.category in user_profile.category.all():
        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blogpost)
            if form.is_valid():
                form.save()
                return redirect('list_blogposts')
        else:
            form = BlogForm(instance=blogpost)

        return render(request, 'update_blogpost.html', {'form': form})
    else:
        # Handle unauthorized access (e.g., return a 404 error)
        return HttpResponseNotFound("You are not authorized to access this blog post.")


@login_required
@admin_required
def delete_blogpost(request, id):
    blogpost = BlogPost.objects.get(id=id)
    blogpost.delete()
    return redirect('list_blogposts')


def create_user(request):
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES)

        form.save()
        return redirect('/')
    else:
        form = UsersForm()

    return render(request, 'create_user.html', {'form': form})


def update_user(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        form = UsersForm(request.POST, request.FILES, instance=user)
        form.save()
        return redirect('/')
    else:
        form = UsersForm(instance=user)

    return render(request, 'update_user.html', {'form': form})

def delete_user(request, id):
    user = Users.objects.get(id=id)
    user.delete()
    return redirect('/')


def list_user(request):
    users = Users.objects.all()
    return render(request,'dashboard1.html',{'users':users})



def category_detail(request):
    category = Category.objects.all()
    # blogposts = category.posts.all()
    context = {'category':category}
    return render(request, 'category_list.html',context)


@login_required
@admin_or_editor
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_detail')
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})

@login_required
@admin_required
def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_detail')

@login_required
@admin_or_editor
def update_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'update_category.html', {'form': form})


@login_required
@category_access_required
def blogposts_by_category(request, category_id):

    category = Category.objects.get(id=category_id)
    blogposts = category.blogposts.all()
    return render(request, 'blogposts_by_category.html', {'category': category, 'blogposts': blogposts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect('/')

from .decorators import category_access_required

@category_access_required
def show_specific_categories(request, category_id):
    user_profile = request.user.userprofile
    allowed_categories = user_profile.categories.all()
    return render(request, 'specific_categories.html', {'categories': allowed_categories})



def category_detail(request):
    user_profile = UserProfile.objects.get(user=request.user)
    category = user_profile.category.all()

    context = {'category':category}
    return render(request, 'category_list.html',context)


@login_required
@admin_or_editor
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_detail')
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})

@login_required
@admin_required
def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('category_detail')

@login_required
@admin_or_editor
def update_category(request,id):
    category = Category.objects.get(id=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'update_category.html', {'form': form})


@login_required
@category_access_required
def blogposts_by_category(request, category_id):

    category = Category.objects.get(id=category_id)
    blogposts = category.blogposts.all()
    return render(request, 'blogposts_by_category.html', {'category': category, 'blogposts': blogposts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def logout_view(request):
    logout(request)

    return redirect('/')

from .decorators import category_access_required

@category_access_required
def show_specific_categories(request, category_id):
    user_profile = request.user.userprofile
    allowed_categories = user_profile.categories.all()
    return render(request, 'specific_categories.html', {'categories': allowed_categories})


from django.shortcuts import render
from .models import Category, UserProfile


