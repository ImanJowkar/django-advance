from django.shortcuts import render

from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blogs.models import Post


# Create your views here.


class IndexView(ListView):
    model = Post
    template_name = 'blogs/index.html'
    context_object_name = 'posts'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    # fields = "__all__"
    fields = ['title', 'image', 'content', 'status', 'category', 'published_at']
    template_name = 'blogs/post-create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blogs:home')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogs/post-detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    success_url = '/blogs/'
    fields = ['title', 'image', 'content', 'status', 'category', 'published_at']
    template_name = 'blogs/post-create.html'

    def get_success_url(self):
        return reverse_lazy('blogs:detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post

    def get_success_url(self):
        return reverse_lazy('blogs:home')

