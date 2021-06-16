from django.conf.urls import url, include
from django.contrib import admin
from JenjieBook import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^attendance_page/$', article_views.attendance_page, name="attendance_page"),
    url(r'^student_page/$', article_views.student_page, name="student_page"),
    url(r'^quiz_page/$', article_views.quiz_page, name="quiz_page"),
    url(r'^list/$', article_views.task_list, name="list"),
    



    url(r'^$', article_views.HomePage, name="home"),
    url(r'^student/$', article_views.StudentViews, name="student"),
    url(r'^teacher/$', article_views.TeacherViews
        , name="teacher"),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
