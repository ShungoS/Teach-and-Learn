from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
from request.models import ReqPost


def home(request):
    Post = Post.objects.all()
    ReqPost = ReqPost.objects.all()
    return render(request, 'tl_app/home.html', {'Post':Post,'ReqPost':RepPost})   

class PostListView(ListView):
    model = Post
    template_name='tl_app/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'Reqpost_list': ReqPost.objects.order_by('name'),
            'more_context': ReqPost.objects.all(),
        })
        post_list = Post.objects.all().order_by('-date_posted')[:5]
        return context
    def get_queryset(self):
        return Post.objects.order_by('date_posted')
    
    

class UserPostListView(ListView):
    model = Post
    template_name='tl_app/user_posts.html'
    context_object_name = 'posts'
    paginator_by = 10
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content','file','thumbnail']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

   

    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'tl_app/login.html', {'title' : 'Login' })

def contact(request):
    return render(request, 'tl_app/contact.html', {'title' : 'Contact Us' })

def otherteacher(request):
    return render(request, 'tl_app/otherteacher.html', {'title' : 'OtherTeacher' })
                     
def paymentinput(request):
    return render(request, 'tl_app/paymentinput.html', {'title' : 'paymentinput' })

def profileedit(request):
    return render(request, 'tl_app/profileedit.html', {'title' : 'profileedit' })

def request(request):
    return render(request, 'tl_app/request.html', {'title' : 'request' })

def searchclass(request):
    return render(request, 'tl_app/searchclass.html', {'title' : 'searchclass' })

def searchresult(request):
    return render(request, 'tl_app/searchresult.html', {'title' : 'searchresult' })

def signup(request):
    return render(request, 'tl_app/signup.html', {'title' : 'signup' })

def takeclass(request):
    return render(request, 'tl_app/takeclass.html', {'title' : 'takeclass' })

def teacherregister(request):
    return render(request, 'tl_app/teacherregister.html', {'title' : 'teacherregister' })

def teacherregisterconfirm(request):
    return render(request, 'tl_app/teacherregisterconfirm.html', {'title' : 'teacherregisterconfirm' })

def yourpage(request):
    return render(request, 'tl_app/yourpage.html', {'title' : 'yourpage' })