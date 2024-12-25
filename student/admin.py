from django.contrib import admin
from .models import Student,Subject,Marks,Group,Exam,Result,Choice
from import_export.admin import ExportActionMixin,ImportExportMixin
from .models import Student,StudentAdmission,StudentCategory,Class,Session,Group,Division,District,Upazilla,Union,GuardianInfo,Transaction,Adress,SubjectChoice,SscEquvalent
from import_export.admin import ExportActionMixin,ImportExportMixin
from import_export.widgets import ManyToManyWidget
from import_export.resources import ModelResource
from django.forms import Field

# Register your models here.
class StudentResource(ModelResource):
    
    student_category = Field(
        widget=ManyToManyWidget(StudentCategory, field='title',
                                        separator='|')
    )
    class Meta:
        model = Student
        fields = ('email', 'student_category')


@admin.register(Student)
class StudentAdmin(ImportExportMixin,admin.ModelAdmin):
    search_fields=['email','phone','class_roll']
    list_display=[ 'class_roll','name','email','phone','student_category','department','session','user_link']
    list_display_links = ['name','email']
    list_filter=['department','student_category','session','group','class_year','is_active']

@admin.register(Session)
class StudentSessionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'id','serial','title','title_en']
    list_display_links = ['serial','title']

@admin.register(GuardianInfo)
class GuardianInfoAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display= ['father_name', 'mother_name','guardian_phone']
    list_display_links = ['father_name', 'mother_name','guardian_phone']
    list_filter=['guardian_phone',]
@admin.register(SscEquvalent)
class SscEquvalentAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display= ['id', 'ssc_or_equvalent','ssc_board']
    list_display_links = ['id', 'ssc_or_equvalent','ssc_board']
    list_filter=['id', 'ssc_or_equvalent','ssc_board']
@admin.register(SubjectChoice)
class SubjectChoiceAdmin(ExportActionMixin,admin.ModelAdmin):
        list_display=['id',]
        filter_horizontal = ['compulsory_subject','optional_subject']

@admin.register(Adress)
class AdressAdmin(ExportActionMixin,admin.ModelAdmin):
    pass
@admin.register(Transaction)
class TransactionAdmin(ExportActionMixin,admin.ModelAdmin):
    pass


@admin.register(StudentCategory)
class StudentCategoryAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display=[ 'serial','title','title_en']
    list_display_links = ['serial','title']
    save_as = True
    resource_class = StudentResource
    

@admin.register(Division)
class DivisionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','link']
    list_display_links = ['name','name_en']
@admin.register(District)
class DistrictAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','division','link']
    list_display_links = ['name','name_en']
    list_filter=['division']

@admin.register(Upazilla)
class UpazillaAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','district','link']
    list_display_links = ['name','name_en']
    list_filter=['district']

@admin.register(Union)
class UnionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'name','name_en','upazilla','link']
    list_display_links = ['name','name_en']
    
@admin.register(StudentAdmission)
class StudentAdmissionAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[ 'id','name','student_details','ssc_roll','board','passing_year','quota','group','status']
    list_display_links = ['ssc_roll','name',]
    list_filter=['board','passing_year','quota','group',]
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
class SubjectAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display=[  'id','serial','name','code',]
    list_filter=[  'name','code',]
    list_display_links = ['id','serial','name','code']

@admin.register(Marks)
class MarksAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[  'id','class_roll','name','subject_name','MCQ','CQ','total','grade','cgpa','exam']
    search_fields=['class_roll']
    list_display_links = ['id','class_roll']
    list_filter=[  'grade','cgpa','exam','subject']
    def get_import_data_kwargs(self, **kwargs):
        return super().get_import_data_kwargs(**kwargs)
@admin.register(Result)
class ResultAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[  'id','class_roll','name','group','section','exam','total','cgpa','grade']
    search_fields=['class_roll']
    list_display_links = ['id','class_roll']
    list_filter=[  'group','cgpa','exam','grade','section']

@admin.register(Choice)
class ChoiceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display=[  'id','class_roll','subject1','subject2','subject3','subject4','subject5','subject6','fourth_subject']
    search_fields=['class_roll']
    list_display_links = ['id','class_roll']
    list_filter=[ 'subject1','subject2','subject3','subject4','subject5','subject6','fourth_subject']

   
