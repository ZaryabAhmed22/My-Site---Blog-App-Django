from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotAllowed
from django.urls import reverse
from django.shortcuts import render
from datetime import date
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views import View
from .forms import CommentForm


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


class PostDetailDetailView(DetailView):
    model = Blog
    template_name = "blog/post-detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        comment_form = CommentForm()
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        context["comment_form"] = comment_form

        return context


class PostDetailView(View):
    # Function for checking whether the post is stored in the session as read-later or not
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is not None:
            # Will return a Boolean
            is_saved_for_later = int(post_id) in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Blog.objects.get(slug=slug)

        # Creating the context
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        rendered_post = Blog.objects.get(slug=slug)

        if comment_form.is_valid():
            # >> IMPORTANT: Since now we are not using DetailVIew and saving the data manually, we are unable to fill the foriegn key post. To solve this problem we will pass "commit=False" in .save method, this will only create a model instance and not touch the data base yet and then set the post field manunally as the rendered post because the comments belong to that post which has been rendered

            # Only creates a model instace
            comment = comment_form.save(commit=False)

            # Setting the foriegn key "post"
            comment.post = rendered_post

            # Calling the .save() method because we are using a model form
            comment.save()

            # we can use the slug as args because we have access to the slug since the request is made from the same post detail page
            return HttpResponseRedirect(reverse("post-detail", args=[slug]))

        # post = Blog.objects.get(slug=slug)
        context = {
            "post": rendered_post,
            "post_tags": rendered_post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        # Getting the sessions
        stored_posts = request.session.get("stored_posts")

        # Creating an empty dictionary for the context that will be passed to the template
        context = {}

        # Checking if there are any posts ids stored as session, if not then context will have no posts. If there are some post ids in the session, then we will retrieve those Blog objects whom ids are in the session dictionary "stored_posts". The id__in means that we have attaches an "__in" modifier with the id which checks in the partical dictionary
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            context["posts"] = Blog.objects.filter(id__in=stored_posts)
            context["has_posts"] = True

        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        # Getting the sessions
        stored_posts = request.session.get("stored_posts")

        # Creating an empty list if there are no sessions
        if stored_posts is None:
            stored_posts = []

        # Getting the data from the hidden input field
        post_id = int(request.POST["post_id"])

        # Appending the post_id in stored posts if it's not in stored_posts list and if it's already stored in the list we remove it, and then saving the stored_posts list ot the sessions
        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts

        # Redirecting to home page
        return HttpResponseRedirect("/")
