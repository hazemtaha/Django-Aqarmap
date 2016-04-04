from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserSettingForm
from accounts.models import UserProfile
# Create your views here.


@login_required
def user_setting(request):
    if request.method == 'GET':
        form = UserSettingForm(instance=request.user)
        saved = 'hide'
    else:
        form = UserSettingForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            saved = 'show'
    context = {'form': form, 'saved': saved}
    return render(request, 'user_settings/settings.html', context)
