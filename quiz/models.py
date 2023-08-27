from django.db import models
from uuid import uuid4

# Create your models here.
class Basemodel(models.Model):
    uid =models.UUIDField(primary_key=True,default=uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    class Meta:
        abstract=True

class Category(Basemodel):
    category_name=models.CharField(max_length=100)

    def __str__(self):
         return self.category_name

class Question(Basemodel):
    category=models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    question =models.CharField(max_length=100)
    marks=models.IntegerField(default=5)

    def __str__(self):
        return self.question

class Answer(Basemodel):
    question=models.ForeignKey(Question,related_name='question_answer',on_delete=models.CASCADE)
    answer =models.CharField(max_length=100)
    is_correct =models.BooleanField(default=False)

    def __str__(self):
        return self.answer


