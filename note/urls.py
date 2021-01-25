from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home-view'),
    path('<slug:foo>/<slug:goo>/', home, name='home'),
    path('<slug:foo>/<slug:goo>/create/', note_create, name='create-view'),
    path('<slug:foo>/<slug:goo>/<int:id>/', note_detail, name='detail-view'),
    path('<slug:foo>/<slug:goo>/<int:id>/update', note_update, name='update-view'),
    path('<slug:foo>/<slug:goo>/<int:id>/delete', note_delete, name='delete-view'),
    path('<slug:foo>/<slug:goo>/logout/', logout, name='logout'),
    path('<slug:foo>/<slug:goo>/user_id/', user_id, name='user_id'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),

]
