from django.shortcuts import HttpResponse, render

# Create your views here.
def IndexView(request):
    return render(request, 'dex/index.html')
def LeftSidebarView(request):
    return render(request, 'dex/left-sidebar.html')
def RightSidebarView(request):
    return render(request, 'dex/right-sidebar.html')
def NoSidebarView(request):
    return render(request, 'dex/no-sidebar.html')
