from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

user = get_user_model()
# Create your models here.


class PostView(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    """Model definition for Author."""

    user = models.OneToOneField(user, on_delete=models.CASCADE)
    profile_picture = models.URLField(max_length=200, null=True)

    class Meta:
        """Meta definition for Author."""

    def __str__(self):
        """Unicode representation of Author."""
        return self.user.username


class Category(models.Model):
    """Model definition for Category."""

    title = models.CharField(max_length=100)

    class Meta:
        """Meta definition for Category."""

    def __str__(self):
        """Unicode representation of Category."""
        return self.title

    def get_absolute_url(self):
        return reverse('category-list', kwargs={'id': self.id})


class Post(models.Model):
    """Model definition for Post."""

    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField()
    timestamp = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.URLField(max_length=300, null=True)
    category = models.ManyToManyField(Category)
    featured = models.BooleanField(default=True)
    previous_post = models.ForeignKey(
        'self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey(
        'self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        """Meta definition for Post."""

    def __str__(self):
        """Unicode representation of Post."""
        return self.title

    def get_absolute_url(self):

        return reverse('post-details', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'id': self.id
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'id': self.id
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()


class Comment(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=300)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comment."""

    def __str__(self):
        """Unicode representation of Comment."""
        return self.user.username
