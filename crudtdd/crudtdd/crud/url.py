from django.urls import path
app_name = 'crud'
from crud.views import List,Get,Create,Update,Delete
urlpatterns = [
    path('', List.as_view() ,name='main'),
    path('get/<int:id>/', Get.as_view() ,name='Get'),
    path('create', Create.as_view() ,name='create'),
    path('update/<int:id>/', Update.as_view() ,name='update'),
    path('delete/<int:id>/', Delete.as_view() ,name='delete'),
]