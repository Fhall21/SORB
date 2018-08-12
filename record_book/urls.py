from django.urls import path, re_path
from login import views
from record_book.views import Pioneer



app_name="login"

urlpatterns = [
	path('pioneer', Pioneer.as_view(), name='Pioneer_intro'),
	] 