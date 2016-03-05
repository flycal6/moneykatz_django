from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.views < 0:
            self.views = 1

        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class File(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    document = models.FileField(upload_to='media')
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    spirit_animal_picture = models.ImageField(upload_to='spirit_images', blank=True)

    def __unicode__(self):
        return self.user.username


# class Contact(models.Model):
#     from_email = models.EmailField()
#     subject = models.CharField(max_length=128)
#     message = models.CharField(max_length=4096)
#
#     def __unicode__(self):
#         return self.subject
