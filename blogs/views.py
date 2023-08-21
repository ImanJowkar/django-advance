from django.shortcuts import render

from django.views import View
from django.views.generic import CreateView
from django.urls import reverse
from blogs.models import Post


# Create your views here.


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'blogs/index.html')


class BlogCreate(CreateView):
    model = Post
    fields = "__all__"
    template_name = 'blogs/create-blog.html'
    success_url = '/blogs/'
