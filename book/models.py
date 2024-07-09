from django.db import models
from django.contrib.auth.models import  User
from .helpers import  SaveMedia

class Author(models.Model):
    first_name = models.CharField(verbose_name="Имя", max_length=100)
    last_name = models.CharField(verbose_name="Фамилия", max_length=100)
    birth_date = models.DateField(verbose_name="Дата рождения")
    biography = models.TextField()
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateField()
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  
    cout = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


    
