from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)
""" thoi diem sau 7 ngay """
class Todolist(models.Model):
    title=models.CharField(max_length=100 , unique=True)

    def get_absolute_url(self):
        return reverse('list', args=[str(self.id)])

    def __str__(self):
        return self.title
    """Ví dụ: Nếu bạn có một model tên là "Product" và muốn tạo URL cho mỗi sản phẩm dựa trên id của nó, 
    hàm get_absolute_url sẽ được gọi trên một thể hiện của "Product,"
     và nó sẽ tạo một URL như "/products/1/", 
    với "1" là giá trị id của sản phẩm."""

class todoItem(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(default=one_week_hence)
    todo_list=models.ForeignKey(Todolist,on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('item-update', kwargs=[str(self.todo_list.id),str(self.id)])

    def __str__(self):
        return f'{self.title}: due{self.due_date}'

    class Meta:
        ordering = ["due_date"]