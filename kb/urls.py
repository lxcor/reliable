from django.urls import path

from kb import views

urlpatterns = [
    path('article/', views.ListArticles.as_view(), name='list-articles'),
    path('article/create/', views.CreateArticle.as_view(), name='create-article'),
    path('article/edit/<int:pk>/', views.EditArticle.as_view(), name='edit-article'),
    path('article/delete/<int:pk>/', views.DeleteArticle.as_view(), name='delete-article'),
    path('article/read/<int:pk>/', views.ReadArticle.as_view(), name='read-article'),

    path('article/image/<int:pk>/', views.upload_image, name='upload-image'),
    path('article/file/<int:pk>/', views.upload_file, name='upload-file'),

]
