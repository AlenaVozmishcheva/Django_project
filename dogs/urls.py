from django.urls import path
from dogs.apps import DogsConfig

from dogs.views import index_view, breeds_list_view, breed_dogs_list_view, DogListView, DogCreateView, \
    DogDetailView, DogUpdateView, DogDeleteView

app_name = DogsConfig.name

urlpatterns = [
    # breeds
    path('', index_view, name='index'),
    path('breeds/', breeds_list_view, name='breeds'),

    # dogs
    path('breeds/<int:pk>/dogs', breed_dogs_list_view, name='breed_dogs'),
    path('dogs/', DogListView.as_view(), name='dogs_list'),
    path('dogs/create/', DogCreateView.as_view() , name='dog_create'),
    path('dogs/detail/<int:pk>/', DogDetailView.as_view(), name='dog_detail'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),

]



