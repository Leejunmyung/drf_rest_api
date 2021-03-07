from django.db import models

class Todo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    todo_id = models.ForeignKey(Todo, on_delete=models.CASCADE)
    contents = models.TextField()
    created_at = models.DateField()
    updated_at = models.DateField()
