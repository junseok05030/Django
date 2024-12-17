from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text = 'Enter a book genre(e.g. Science Fiction)')


    def __str__(self):
        return self.name
##장르모델
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=200) # 책 제목
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    
    summary = models.TextField(max_length=1000,help_text="Enter a brief description of the book");

    isbn = models.CharField('ISBN', max_length=13, help_text = '13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
import uuid

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique whole library')
    book = models.models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    
    LOAN_STATUS = (
        ('m', 'maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank_True,
        default='m',
        help_text='Book availablity',
    )
    
    
    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'

class Author(models.Model):
    first_name = models.Char_field(max_length=100)
    last_name = models.Char_field(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank = True)
    

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    def __str__(self):
        return f'{self.last_name},{self.first_name}'
    








