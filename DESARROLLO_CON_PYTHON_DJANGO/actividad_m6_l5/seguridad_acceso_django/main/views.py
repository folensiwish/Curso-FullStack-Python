from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
@permission_required('main.can_edit', raise_exception=True)
def home(request):
    return render(request, 'home.html',context={})