from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView, DetailView
from django.views.generic.base import View, TemplateView


# Importing data from models
from .models import Blog


# Helper function and global variables
all_blogs = Blog.objects.all()

# >> not using this helper function


def get_date(post):
    return post["date"]

# Create your views here.


def index(request):
    # >> This whole query orders the data in decending order and slices the first 3 posts, this whole query will be changed into an SQL query in BTS, so there are no performance issues >> Important, this syntax doesn't used negative indexing
    latest_posts = all_blogs.order_by("-date")[:3]

    # >> Ordering and slicing the data without models
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):

    return render(request, "blog/all-posts.html", {
        "all_posts": all_blogs.order_by("-date")
    })


def post(request, slug):
    # >> before models
    # using the next function >> finds the next element that matches the condition
    # identified_post = next(post for post in all_blogs if post['slug'] == slug)

    # >> Getting the desired object based on slug field using the slug in request
    identified_post = get_object_or_404(Blog, slug=slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "tags": identified_post.tags.all()
    })


############# SWTICHING TO CLASS BASED VIEWS ###############
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Blog
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostView(ListView):
    # model = Blog
    # >> We can also use if we use model = Blog
    # ordering = ["-date"]
    queryset = Blog.objects.order_by("-date")
    template_name = "blog/all-posts.html"
    context_object_name = "all_posts"


class PostDetailView(DetailView):
    model = Blog
    template_name = "blog/post-detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
