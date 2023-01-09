from django.urls import path
from . import views

urlpatterns = [
    path("",views.addandshow,name="show"),
    path("update/<int:id>",views.updatedata,name="updatedata"),
    path("delete/<int:id>",views.delete_data,name="deletedata"),
    path("studentsinfo/all/",views.studentapi),
]