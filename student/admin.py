from django.contrib import admin
from .models import Student,Subject,Marks,Group,Exam
from import_export.admin import ExportActionMixin,ImportExportMixin

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','roll','name',]
    list_filter=[  'name','roll',]
    list_display_links = ['serial','name','roll']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display=[  'serial','title_en',]
    list_filter=[  'title_en',]
    list_display_links = ['serial','title_en',]

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','title_en',]
    list_filter=[  'title_en',]
    list_display_links = ['serial','title_en',]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=[  'id','serial','name','code',]
    list_filter=[  'name','code',]
    list_display_links = ['id','serial','name','code']

@admin.register(Marks)
class MarksAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[  'id','roll','subject_name','MCQ','CQ','grade','exam']
    search_fields=['roll']
    list_display_links = ['id','roll']
