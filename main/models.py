from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

class Skill(models.Model):

    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    name = models.CharField(max_length=30, blank=True, null=True)
    description = RichTextField()
    image = models.FileField(blank=True, null=True, upload_to='skills')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Certificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank=True, null=True)
    provider = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    image_file = models.FileField(blank=True, null=True, upload_to='certificates')
    image_url = models.URLField(blank=True, null=True)
    is_cloud = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.provider}: {self.title}'

class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'
        verbose_name = 'User Profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatar')
    title = models.CharField(max_length=200, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    certifications = models.ManyToManyField(Certificate, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    email = models.EmailField(verbose_name='Email')
    message = models.TextField(verbose_name='Message')

    def __str__(self):
        return f'{self.name}'

# Makes it easy to access static files in a template
class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = 'Media'
        ordering = ['name']

    image = models.ImageField(blank=True, null=True, upload_to='media')
    url = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    is_image = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Portfolio'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/portfolio/{self.slug}'

class Blog(models.Model):

    class Meta:
        verbose_name_plural = 'Blog Profiles'
        verbose_name = 'Blog'
        ordering = ['name']

    date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog')
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/blog/{self.slug}'