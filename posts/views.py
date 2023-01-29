from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from django.views import generic
from django.urls import reverse_lazy


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    extra_context = {"title": "Главная страница"}
    template_name = "index.html"

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "post_detail.html"

class PostCreateView(generic.CreateView):
    model= Post
    template_name = "post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("main-page")

class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("main-page")

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("main-page")

# Create your views here.
def hello (request):
    return HttpResponse('GeekTech')

def index (request):
    posts = Post.objects.all()
    context = {
        "title": "Главна страница",
        "posts": posts
      
    }
    return render(request, "index.html",context)


def about(request):
    context = {
        "title": "О нас",
    }
    return render(request, "about.html", context)


def contacts(request):
    context = {
        "title": " контакты",
    }   
    return render (request, "contacts.html" , context)