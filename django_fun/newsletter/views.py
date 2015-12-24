from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = 'My Title %s' % (request.user)
    context = {
        'title': title,
        'name': 'The Moose',
    }
    return render(request, "home.html", context)
