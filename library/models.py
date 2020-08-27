from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=False, blank=False)
    date_of_death = models.DateField(null=True,blank=True)

    def __str__(self):

     result = ''
     if self.date_of_death is None:
        result = '%s , %s (%s - )' % (self.last_name, self.first_name, self.date_of_birth)
     else:
        result = '%s , %s  (%s - %s) ' % (self.last_name, self.first_name, self.date_of_birth, self.date_of_death)
     return result

    def get_absolute_url(self):
        return reverse('library_author_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_author_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_author_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name','first_name']
        unique_together = (('last_name', 'first_name'),)


class Publisher(models.Model):
    publisher_id = models.AutoField(primary_key=True)
    publisher_name = models.CharField(max_length = 200, unique=True)

    def __str__(self):
        return '%s' % self.publisher_name

    def get_absolute_url(self):
        return reverse('library_publisher_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_publisher_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_publisher_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['publisher_name']


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - ( %s , %s)' %(self.book_name, self.author.last_name, self.author.first_name)

    def get_absolute_url(self):
        return reverse('library_book_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_book_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_book_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['book_name','author__last_name']
        unique_together = (('book_name','author'),)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=50, unique = True)

    def __str__(self):
        return '%s' % self.genre_name

    def get_absolute_url(self):
        return reverse('library_genre_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_genre_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_genre_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['genre_name']


class Section(models.Model):
    section_id = models.AutoField(primary_key=True)
    genre = models.ForeignKey(Genre, related_name='sections', on_delete=models.PROTECT)
    book = models.ForeignKey(Book, related_name='sections', on_delete=models.PROTECT)

    def __str__(self):
        return '%s - %s' % (self.book.book_name, self.genre.genre_name)

    def get_absolute_url(self):
        return reverse('library_section_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_section_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_section_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['genre__genre_name', 'book__book_name']
        unique_together = (('genre', 'book'),)


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)

    def get_absolute_url(self):
        return reverse('library_member_detail_urlpattern',
                       kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('library_member_update_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    def get_delete_url(self):
        return reverse('library_member_delete_urlpattern',
                       kwargs={'pk': self.pk}
                       )

    class Meta:
        ordering = ['last_name', 'first_name']