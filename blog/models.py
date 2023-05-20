from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=20, default="new", null=False)

    def __str__(self):
        return f"{self.name}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(blank=True, null=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Blog(models.Model):
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(max_length=5000, validators=[
                               MinLengthValidator(100)])
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, unique=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL,)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)

        # Doing this so that our built in django save method is called with any other arguments passed in the overwriting of save method
        super().save(*args, **kwargs)


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Blog,
                             on_delete=models.CASCADE, related_name="comments")
