from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name="homepage"),
    path('play/', views.play, name="gamepage"),
    path('level/<int:level>/question/<int:question>/', views.question_page, name="question"),
    path('level/<int:level>/', views.open_level1, name="open_level"),
    path("track-tab-switch/", views.track_tab_switch, name="track_tab_switch"),
    path("morse-code/<int:level>/", views.open_morse, name="decrypt")
]