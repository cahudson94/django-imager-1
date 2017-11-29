"""Views for Django Imager."""

from django.shortcuts import render
from registration.backends.hmac.views import RegistrationView


def home_view(request, number=None):
    """View for the home page."""
    login_context = {}
    if request.user.username:
        login_context = {"username": request.user.username}
    return render(request, 'imagersite/home.html', context=login_context)


def login_view(request):
    """View for login."""
    return render(request, 'imagersite/login.html', context={})


def logout_view(request):
    """View for logout."""
    return render(request, 'imagersite/logout.html', context={})


def register_view(request):
    """View for registration."""
    return render(request, 'imagersite/register.html', context={})


def profile_view(request):
    """View for profile."""
    import pdb; pdb.set_trace()
    if not request.user.username:
        return render(request, 'imagersite/profile.html', context={"logged_out_alert": "You are not logged in. Log in to view your profile!", "logged_in": False})
    import pdb; pdb.set_trace()
