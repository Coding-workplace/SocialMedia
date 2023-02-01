from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name='home_page'),
	path('<int:pk>',views.delete_post,name="delete_post"),
	path('<str:username>',views.profile_view,name="profile_view")
]
