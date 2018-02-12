from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    text = models.TextField()
    slug = models.SlugField(max_length=40)
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField( blank=True, null=True,verbose_name='Imagen')
    title = models.CharField(max_length=200)

    def get_object(self):
        object = get_object_or_404(Post,title=self.kwargs['title'])
        return object
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        view_name = "post"
        return reverse(view_name, kwargs={"slug": self.slug})