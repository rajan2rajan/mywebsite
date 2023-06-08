from .views import *
from django.urls import path

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('editabout/<int:pk>',editabout,name='editabout'),
    path('video/',project_video,name='video'),
    path('submitvideo/',submit_video,name='submit_video'),
    path('submitvideo/<int:pk>',edit_video,name='edit_video'),
    path('deletevideo/<int:pk>',delete_video,name='delete_video'),
    path('cv/',cv,name='cv'),
    path('generatepdf/',generatepdf,name='generatepdf'),
    path('pdf/',pdf,name='pdf'),
    # path('siteundercons/',siteundercons,name='siteundercons'),



]
