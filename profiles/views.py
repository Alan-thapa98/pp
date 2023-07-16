from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile, Relationship
from .forms import ProfileModelForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


@login_required
def my_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    print(profile)
    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
    }

    return render(request, 'profiles/myprofile.html', context)



class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profiles/detail.html'

    # def get_object(self):
    #     slug = self.kwargs.get('slug')
    #     profile = Profile.objects.get(slug=slug)
    #     return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['posts'] = self.get_object().get_all_authors_posts()
        context['len_posts'] = True if len(
            self.get_object().get_all_authors_posts()) > 0 else False
        return context



# custom
@login_required
def my_profile_view_edit(request):
    profile = Profile.objects.get(user=request.user)
    # THESE IS FOR THE CHANGE PROFILE
    form = ProfileModelForm(request.POST or None,
                            request.FILES or None, instance=profile)
    # TO  CONFIRM
    confirm = False
    #  TO CHECK WEATHER THE PSOTS IS UPLADED FOR NOT
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True
            context = {
                'profile': profile,
                'form': form,
                'confirm': confirm,
            }
            return render(request, 'profiles/myprofile.html', context)
    else:
        context = {
            'profile': profile,
            'form': form,
            'confirm': confirm,
        }
        return render(request, 'profiles/pro_edite.html', context)




# def handelLogout(request):
#     logout(request)
#     messages.success(request, "Successfully logged out")
#     return redirect('http://127.0.0.1:8000/')


