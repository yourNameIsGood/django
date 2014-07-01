from django.template import loader,Context
from django.http import HttpResponse
from app1.models import BlogPost

def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('foo.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def show_404(request):
    view = loader.get_template('404.html')
    data = Context({'title':'this is how things are done here'})
    return HttpResponse(view.render(data))