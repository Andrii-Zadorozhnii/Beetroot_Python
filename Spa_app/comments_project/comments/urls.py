from .views import AttachmentUploadView, CaptchaView, CommentCreateView, CommentListView
from django.urls import path


urlpatterns = [
    path('attachments/', AttachmentUploadView.as_view(), name='attachment-upload'),
    path('captcha/', CaptchaView.as_view(), name='captcha'),
    path('comments/', CommentListView.as_view(), name='comment-list'),
    path('comments/create/', CommentCreateView.as_view(), name='comment-create'),
]