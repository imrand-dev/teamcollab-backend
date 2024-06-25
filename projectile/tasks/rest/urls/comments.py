from django.urls import path

from tasks.rest.views.tasks import CommentDetail

urlpatterns = [
    path("/<uuid:comment_uid>", CommentDetail.as_view(), name="comment-detail"),
]
