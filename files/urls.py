from django.urls import path
from .views import upload_file_view, upload_file_lancamento_view, upload_file_date_view

app_name = "file"

urlpatterns = [
    path('', upload_file_view, name = 'upload_view'),
    path('lancamento', upload_file_lancamento_view, name = 'upload_lancamento_view'),
    path('date', upload_file_date_view, name = 'upload_date_view'),

]