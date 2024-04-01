from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .decorations import profile_ownership_required
from .forms import ProfileCreationForm
from .models import Profile


# Create your views here.

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_user'
    template_name = 'profileapp/create.html'
    success_url = reverse_lazy('accountapp:hello_world')

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_user'
    template_name = 'profileapp/update.html'
    success_url = reverse_lazy('accountapp:hello_world')
