from django.urls import path

from . import views

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
#클래스 형 뷰를 사용할 때는 꼭 as.view() 를 붙여야 한다.
app_name = 'polls'