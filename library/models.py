from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class user_table(models.Model):
    username=models.CharField(max_length=100)
    housename=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post= models.CharField(max_length=100)
    pin=models.IntegerField()
    phone=models.BigIntegerField()
    email=models.CharField(max_length=50)
    lid=models.ForeignKey(login_table,on_delete=models.CASCADE)

class library_table(models.Model):
    libraryname = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.IntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)
    lid = models.ForeignKey(login_table, on_delete=models.CASCADE)

class book_table(models.Model):
    bookname = models.CharField(max_length=100)
    authorname = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    libid = models.ForeignKey(library_table,on_delete=models.CASCADE)


class complaint_table(models.Model):
    uid = models.ForeignKey(user_table,on_delete=models.CASCADE)
    libid = models.ForeignKey(library_table,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)

class rating_table(models.Model):
    libid = models.ForeignKey(library_table,on_delete=models.CASCADE)
    uid = models.ForeignKey(user_table,on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)


