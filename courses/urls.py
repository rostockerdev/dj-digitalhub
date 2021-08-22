from django.urls import include, path

from courses import views as course_view

from .models import Course

app_name = "courses"

urlpatterns = [
    path("", course_view.course_list_view, name="courselist"),
    path(
        "<course_slug>/", course_view.CourseDetailView.as_view(), name="course-detail"
    ),
    path(
        "<course_slug>/like/", course_view.course_like_toggle_view, name="course-like"
    ),
    path("<course_slug>/add-review/", course_view.add_review_view, name="add-review"),
    path(
        "<str:course_slug>/<str:lesson_slug>/",
        course_view.lesson_detail_view,
        name="lesson-detail",
    ),
    path(
        "<str:course_slug>/<str:lesson_slug>/add-comment/",
        course_view.add_comment_view,
        name="add-comment",
    ),
]
