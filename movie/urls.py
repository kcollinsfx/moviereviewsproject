from django.urls import path
from . import views

urlpatterns = [
    path('<int:movie_id>', views.detail, name='detail'),
    # I wonder why we are putting this set of code in movies/urls
    path('<int:movie_id>/create', views.createreview, name='createreview'),
    path('review/<int:review_id>', views.updatereview, name='updatereview'),
    path('review/<int:review_id/delete', views.deletereview, name='deletereview'),

]