from functools import wraps

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from .models import Category

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def is_editor(user):
    return user.groups.filter(name='Editor').exists()



def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You must be an admin to access this page.")
            return redirect('login')
    return _wrapped_view

def editor_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if is_editor(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You must be an editor to access this page.")
            return redirect('login')
    return _wrapped_view

def admin_or_editor(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if is_admin(request.user) or is_editor(request.user):
            return view_func(request, *args, **kwargs)
        else:
            messages.error(request, "You must be an admin or editor to access this page.")
            return redirect('login')
    return _wrapped_view



from .models import UserProfile, Category, Permission


def has_access_to_category(user, category_id):
    try:
        user_profile = UserProfile.objects.get(user=user)
        user_roles = user_profile.roles.all()
        allowed_categories = Category.objects.filter(userprofile=user_profile)

        if allowed_categories.filter(id=category_id).exists():
            return True
        else:
            for role in user_roles:
                if role.permissions.filter(category_id=category_id).exists():  # Modify this line
                    return True
            return False
    except UserProfile.DoesNotExist:
        return False


from functools import wraps
from django.shortcuts import redirect

def category_access_required(view_func):
    @wraps(view_func)
    def decorator(request, category_id, *args, **kwargs):
        if not has_access_to_category(request.user, category_id):
            return redirect('/')  # Redirect to unauthorized access page
        return view_func(request, category_id, *args, **kwargs)
    return decorator


