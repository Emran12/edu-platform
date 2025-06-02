from django.contrib import admin
from .models import Course, Lesson, Enrollment

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'teacher', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('teacher', 'created_at')

class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('title', 'content')

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'progress')
    list_filter = ('course', 'user')
    search_fields = ('user__username', 'course__title')

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)

# ✅ Custom Admin Site Branding
admin.site.site_header = "EduPlatform Admin"
admin.site.site_title = "EduPlatform Admin Portal"
admin.site.index_title = "Welcome to the EduPlatform Dashboard"
