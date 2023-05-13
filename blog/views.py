from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from datetime import date

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


######################## DUMMY DATA #######################
#  all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Zaryab Ahmed",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothin like the views you get when hiking in the mountains! And I was't even prepared for what happened whilst I was enjoying the view!",
#         "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

#         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

#         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo."""
#     },

#     {
#         "slug": "nature-is-the-best",
#         "image": "mountains.jpg",
#         "author": "Zaryab Ahmed",
#         "date": date(2021, 7, 21),
#         "title": "Nature At Its Best",
#         "excerpt": "There's nothin like the views you get when hiking in the mountains! And I was't even prepared for what happened whilst I was enjoying the view!",
#         "content": """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

#         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo.

#         Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut volutpat velit. Morbi luctus ultrices sodales. Integer pulvinar ligula et erat ultrices, non placerat eros condimentum. Proin sagittis interdum justo, sit amet lacinia odio consequat sed. Aenean malesuada libero vitae efficitur tristique. Etiam dictum laoreet lorem, id faucibus felis bibendum id. Aenean tincidunt eros sem, nec vulputate eros porttitor fringilla. Phasellus justo mauris, porttitor in metus eget, hendrerit aliquam justo."""
#     }
# ]
