from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Todolist , todoItem
from django.views.generic import (ListView,CreateView,UpdateView,DeleteView)
# Create your views here.
class ListlistView(ListView):
    model=Todolist
    template_name = 'todo_app/index.html'

class itemListView(ListView):
    model = todoItem
    template_name = 'todo_app/todo_list.html'

    def get_queryset(self):
        return todoItem.objects.filter(todo_list_id=self.kwargs['list_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['todo_list']=Todolist.objects.get(id=self.kwargs['list_id'])
        return context
    """
    get_queryset : phuong thuc dung de truy van co so du lieu , 
    """
class ListDelete(DeleteView):
    model = Todolist
    template_name = 'todo_app/todolist_delete.html'
    success_url = reverse_lazy('index')


class ItemDelete(DeleteView):
    model = todoItem
    template_name = 'todo_app/todoitem_delete.html'
    def get_success_url(self):
        return reverse_lazy('list',args=[self.kwargs['list_id']])

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['todo_list']=self.object.todo_list
        return context
class ListCreate(CreateView):
    model = Todolist
    fields = ['title']
    template_name = 'todo_app/todo_listform.html'

    def get_context_data(self, **kwargs):
        context=super(ListCreate,self).get_context_data(**kwargs)
        context['title']="add a new List"
        return context



class ItemCreate(CreateView):
    model= todoItem
    fields = [
        'todo_list',
        'title',
        'description',
        'due_date',
    ]

    def get_initial(self):
        initial_data=super(ItemCreate,self).get_initial()
        todo_list=Todolist.objects.get(id=self.kwargs['list_id'])
        initial_data['todo_list']=todo_list
        return initial_data
    def get_context_data(self, **kwargs):
        context=super(ItemCreate,self).get_context_data()
        todo_list=Todolist.objects.get(id=self.kwargs['list_id'])
        context['todo_list']=todo_list
        context['title']='create a new item '
        return context

    def get_success_url(self):
        return reverse('list',args=[self.object.todo_list_id])


class ItemUpdate(UpdateView):
    model = todoItem
    fields = ['todo_list',
        'title',
        'description',
      'due_date',
    ]

    def get_context_data(self):
            context = super(ItemUpdate, self).get_context_data()
            context["todo_list"] = self.object.todo_list
            context["title"] = "Edit item"
            return context

    def get_success_url(self):
            return reverse("list", args=[self.object.todo_list_id])

class ListUpdate(UpdateView):
    model = Todolist
    fields = ['title']
    template_name = 'todo_app/List-Edit.html'
    def get_context_data(self, **kwargs):
        context=super(ListUpdate,self).get_context_data(**kwargs)
        context['todo_list']=self.object.todo_list
        context['title']='Edit Name List'
        return context

    def get_object(self, queryset=None):
        list_id = self.kwargs.get('list_id')
        return get_object_or_404(self.model, id=list_id)

    def get_success_url(self):
        return reverse('list-edit',args=[self.object.todo_list])