from django.urls import path
import news.views as views

urlpatterns = [
    path('', views.main_page),
    path('<int:id>/', views.news_detail_view),
    path('add/', views.news_add_view),
    path('<int:id>/update/', views.news_update_view),
    path('<int:id>/delete/', views.news_delete_view),
]