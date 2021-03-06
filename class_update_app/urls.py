from django.urls import path
from .views import ClassList,ClassCreate,ClassDetail,resultfunc,ClassDelete,comparefunc

urlpatterns=[
    path("list/",ClassList.as_view(),name="list"),
    path("create/",ClassCreate.as_view(),name="create"),
    path("detail/<int:pk>",ClassDetail.as_view(),name="detail"),
    path("result/<int:pk>",resultfunc,name="result"),
    path("delete/<int:pk>",ClassDelete.as_view(),name="delete"),
    path("compare/<int:pk>",comparefunc,name="compare"),
]