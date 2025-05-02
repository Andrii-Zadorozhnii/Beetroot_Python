from .views import AttachmentUploadView, CaptchaView, CommentListCreateView, CommentListView
from django.urls import path


urlpatterns = [
    path('attachments/', AttachmentUploadView.as_view(), name='attachment-upload'),
    path('captcha/', CaptchaView.as_view(), name='captcha'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]