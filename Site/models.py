from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField(max_length= 100)
    #body = RichTextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='', blank= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default='None' )

    class Meta:
        ordering = [ '-date']

    def __str__(self):
        return self.title

    def snippet(self):
         return self.body[:300]+'...'

    def Short_snippet(self):
        return self.body[:20]+'...'


    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/media/default.jpg"

'''class Feedback(models.Model):
    subject = models.CharField(max_length = 100)
    email: models.EmailField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)'''

#adding comments model
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete =models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('self', on_delete=models.CASCADE, null= True, blank=True, default = '')
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
         return self.text

class Reply(models.Model):
    replies = models.ForeignKey('Comment', on_delete = models.CASCADE, related_name = 'replies')
    name = models.CharField( max_length = 100)
    texts = models.TextField()
    author = models.ForeignKey('self', on_delete=models.CASCADE, null= True, blank=True, default = '')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.texts
