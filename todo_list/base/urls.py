from django.urls import path
from .views import Tasklist, TaskDetail, TaskCreate, TaskEdit, DeleteView, MyLoginView, RegistrationForm
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', Tasklist.as_view(), name="tasks"),
    path('task/<int:pk>/',TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name = "task-create"),
    path('task-edit/<int:pk>/',TaskEdit.as_view(), name='task-edit'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(next_page='login'),name="logout"),
    path('register/', RegistrationForm.as_view(), name="register")]
