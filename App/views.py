from django.shortcuts import render

# Create your views here.
def iplteams(request):
    return render(request,'IPL_TEAMS.html')
