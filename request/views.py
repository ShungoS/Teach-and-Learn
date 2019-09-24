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
from .models import ReqPost

def home2(request):
    return render(request, 'tl_app/home2.html', context)


class ReqListView(ListView):
    model = ReqPost
    template_name='tl_app/home2.html'
    context_object_name = 'reqposts'
    ordering = ['-date_posted']
    paginator_by = 10

class ReqPostListView(ListView):
    model = ReqPost
    template_name='request/user_reqposts.html'
    context_object_name = 'reqposts'
    paginator_by = 10
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
class ReqDetailView(DetailView):
    model = ReqPost

class ReqCreateView(LoginRequiredMixin,CreateView):
    model = ReqPost
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ReqUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ReqPost
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ReqDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ReqPost
    success_url = '/'
    
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

