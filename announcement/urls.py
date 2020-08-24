from django.urls import path

from announcement.views import AnnouncementView, UpdateDeleteAnnouncement, UploadFile, UploadAnnounce

urlpatterns = [
    path('info/', AnnouncementView.as_view()),
    path('updel/<int:pk>/', UpdateDeleteAnnouncement.as_view()),
    path('generic/', UploadFile.as_view()),
    path('file/', UploadAnnounce.as_view()),
]
