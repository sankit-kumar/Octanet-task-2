from django.contrib import admin
from django.urls import path
from tudoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('tudo/', views.tudos),
     path('show/', views.show),
      path('delete/<slug:pk>/', views.delete),
     path('update/<slug:pk>/',views.update),

]