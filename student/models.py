from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import Field
from django.urls import reverse
from django.utils.html import format_html
from django.template.defaultfilters import escape
from import_export.resources import ModelResource

UserModel=get_user_model()

# Create your models here.
class Group(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

class Exam(models.Model):
    serial=models.IntegerField(default=0)
    title=models.CharField(max_length=150,blank=True,null=True)
    title_en=models.CharField(max_length=150,blank=True,null=True)
    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

class StudentCategory(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    
class Department(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True,verbose_name="Name(In English)")
    code=models.CharField(max_length=20, null=True,blank=True)
    about=RichTextUploadingField(blank=True,null=True)
    about_en=RichTextUploadingField(blank=True,null=True,verbose_name="About(In English)")
    professor=models.IntegerField(default=0)
    associate_professor=models.IntegerField(default=0)
    assistant_professor=models.IntegerField(default=0)
    lecturer=models.IntegerField(default=0)
    demonstrator=models.IntegerField(default=0)
    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.name


class Branch(models.Model):
    serial=models.IntegerField(default=10)
    code=models.CharField(max_length=20, null=True,blank=True)
    name=models.CharField(max_length=100,unique=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        ordering = ['serial']
    
    def __str__(self):
        return self.name

class Session(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en
    
    
class Class(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title
    
class Group(models.Model):
    serial=models.IntegerField(default=10)
    title=models.CharField(max_length=100,unique=True)
    title_en=models.CharField(max_length=100,unique=True,blank=True,null=True)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        return self.title_en

  
class Subject(models.Model):
    serial=models.IntegerField(default=10)
    name=models.CharField(max_length=100,null=True,blank=True)
    name_en=models.CharField(max_length=100,null=True,blank=True)
    code=models.CharField(max_length=20, null=True,blank=True)
    group=models.ManyToManyField(Group, blank=True,null=True)
    department=models.ManyToManyField(Department, blank=True,null=True)
    type=models.CharField(max_length=25,blank=True,null=True)
    is_available=models.BooleanField(default=True)



    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.name_en:
            return self.name_en
        else:
            return '1'

    
class Division(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=15,unique=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name_en

class District(models.Model):
    name=models.CharField(max_length=25,unique=True)
    name_en=models.CharField(max_length=25,unique=True)
    lattitude=models.CharField(max_length=15,blank=True,null=True)
    longitude=models.CharField(max_length=15, blank=True,null=True)
    division=models.ForeignKey(Division, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class Upazilla(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    district=models.ForeignKey(District, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)
    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class Union(models.Model):
    name=models.CharField(max_length=25)
    name_en=models.CharField(max_length=25)
    upazilla=models.ForeignKey(Upazilla, on_delete=models.CASCADE,blank=True,null=True)
    link=models.CharField(max_length=15,null=True,blank=True)

    class Meta:
        ordering = ['name_en']
    def __str__(self):
        return self.name_en

class GuardianInfo(models.Model):
    serial=models.IntegerField(default=10)
    father_name=models.CharField(max_length=100,blank=True,null=True)
    father_name_en=models.CharField(max_length=100,blank=True,null=True)
    profession_of_father=models.CharField(max_length=25,blank=True,null=True)
    father_nid=models.CharField(max_length=25,blank=True,null=True)
    mother_name=models.CharField(max_length=100,blank=True,null=True)
    mother_name_en=models.CharField(max_length=100,blank=True,null=True)
    profession_of_mother=models.CharField(max_length=25,blank=True,null=True)
    mother_nid=models.CharField(max_length=100,blank=True,null=True)
    guardian_phone=models.CharField(max_length=11,blank=True,null=True)
    anual_income=models.CharField(max_length=11,blank=True,null=True)
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.father_name:
            return self.father_name
        else:
            return '1'
    
class Adress(models.Model):
    serial=models.IntegerField(default=10)
    village_or_house=models.CharField(max_length=50,blank=True,null=True)
    house_or_street_no=models.CharField(max_length=25,blank=True,null=True)
    post_office=models.CharField(max_length=25,blank=True,null=True)
    division=models.ForeignKey(Division,blank=True,null=True,on_delete=models.SET_NULL)
    district=models.ForeignKey(District,blank=True,null=True,on_delete=models.SET_NULL)
    upazilla=models.ForeignKey(Upazilla,blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.village_or_house:
            return self.village_or_house
        else:
            return '1'
            
class Student(models.Model):
    std_id=models.IntegerField(default=10)
    name=models.CharField(max_length=100,blank=True, null=True)
    name_bangla=models.CharField(max_length=100,blank=True, null=True)
    email=models.EmailField(max_length=50,blank=True, null=True)
    phone=models.CharField(max_length=11,blank=True, null=True)
    class_roll=models.CharField(max_length=11,null=True, blank=True,)
    session=models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    student_category=models.ForeignKey(StudentCategory,blank=True,null=True,on_delete=models.SET_NULL)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    section=models.CharField(max_length=25,null=True, blank=True,)
    department=models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    exam_roll=models.CharField(max_length=25,null=True, blank=True,)
    registration=models.CharField(max_length=25,null=True, blank=True,)
    class_year=models.ForeignKey(Class,blank=True,null=True,on_delete=models.SET_NULL)
    cgpa=models.CharField(max_length=15,null=True, blank=True,)
    date_of_birth=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=15,null=True, blank=True,)
    passing_year=models.CharField( max_length=25, blank=True,null=True)
    nationality=models.CharField(max_length=15,null=True, blank=True,)
    birth_registration=models.CharField(max_length=25,null=True, blank=True,)
    religion=models.CharField(max_length=15,null=True, blank=True,)
    blood_group=models.CharField(max_length=10,null=True, blank=True,)
    marital_status=models.CharField(max_length=25,null=True, blank=True,)
    guardian_info=models.ForeignKey(GuardianInfo,on_delete=models.SET_NULL,null=True, blank=True,)
    present_adress=models.ForeignKey(Adress,null=True, blank=True,related_name="present_adress",on_delete=models.SET_NULL)
    permanent_adress=models.ForeignKey(Adress,null=True, blank=True,related_name="permanent_adress",on_delete=models.SET_NULL)
    image=models.ImageField(upload_to='media/',blank=True,null=True) 
    signature=models.ImageField(upload_to='media/',blank=True,null=True)
    user=models.OneToOneField(UserModel,blank=True,null=True,on_delete=models.CASCADE)
    is_active=models.BooleanField(default=False)
    fourth_subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)


    def user_link(self):
        if self.user is not None:
            return format_html('<a href="%s">%s</a>' % (reverse("admin:auth_user_change", args=(self.user.id,)) , escape(self.user.username)))
        else:
            return None
    user_link.allow_tags = True
    user_link.short_description = "User"
    
    def __str__(self):
        return self.name +':'+ self.phone
    
    def __unicode__(self):
        return self.name_bangla
    
    
    
    
class SscEquvalent(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    ssc_or_equvalent=models.CharField(max_length=25,blank=True,null=True)
    ssc_board=models.CharField(max_length=25,blank=True,null=True)
    ssc_group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    ssc_session=models.ForeignKey(Session,blank=True,null=True,on_delete=models.SET_NULL)
    ssc_exam_roll=models.CharField(max_length=25,blank=True,null=True)
    ssc_regitration_no=models.CharField(max_length=25,blank=True,null=True)
    ssc_cgpa_with_4th=models.CharField(max_length=25,blank=True,null=True)
    ssc_cgpa_without_4th=models.CharField(max_length=25,blank=True,null=True)
    ssc_passing_year=models.CharField( max_length=25, blank=True,null=True)
    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.student:
            return self.student.name+': '+self.student.phone
        return '1'
    
class SubjectChoice(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    compulsory_subject=models.ManyToManyField(Subject,related_name='compulsory_subject',blank=True,null=True)
    optional_subject=models.ManyToManyField(Subject,related_name='optional_subject',blank=True,null=True)
    fourth_subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)

    
    class Meta:
        ordering = ['serial']
    def __str__(self):
        if self.student is not None:
            return self.student.name+': '+self.student.phone
        return '1'
    


class Transaction(models.Model):
    serial=models.IntegerField(default=10)
    student=models.ForeignKey(Student,blank=True,null=True,on_delete=models.CASCADE)
    phone=phone=models.CharField(max_length=11,unique=True,blank=True,null=True,)
    email=models.EmailField(max_length=50,blank=True,null=True)
    transactionID=models.CharField(max_length=25,blank=True,null=True)
    purpose=models.CharField(max_length=25,blank=True,null=True)
    method=models.CharField(max_length=100,blank=True,null=True)
    amount=models.CharField(max_length=25,blank=True,null=True)
    date=models.DateField(blank=True, null=True)
    refunded=models.BooleanField(default=False)
    
    class Meta:
        ordering = ['serial']
        unique_together = (('student', 'transactionID'),)
    def __str__(self):
        if self.student:
            return self.student
        else:
            return '1'


class StudentAdmission(models.Model):
    serial=models.IntegerField(default=10)
    student=models.OneToOneField(Student,blank=True,null=True,on_delete=models.SET_NULL)
    ssc_roll=models.CharField(max_length=25,blank=True,null=True)
    name=models.CharField(max_length=125,blank=True,null=True)
    passing_year=models.CharField( max_length=25, blank=True,null=True)
    board=models.CharField(max_length=25,blank=True,null=True)
    group=models.CharField(max_length=25,blank=True,null=True)
    quota=models.CharField(max_length=25,blank=True,null=True)
    status=models.CharField(max_length=100,default="Not Admitted")

    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.ssc_roll
    def student_details(self):
        stud=self.student
        if stud:
            return format_html('<a href="%s" target="_blank">%s</a>' % (reverse("admin:student_student_change", args=(stud.id,)) , escape(self.name+",\nRoll:"+stud.class_roll+', Phone:'+stud.phone)))
    student_details.allow_tags = True
    def save(self, *args, **kwargs):
           super().save(*args, **kwargs)
           if self.serial == None:
                self.serial = self.id
                super().save()
    

  

class Marks(models.Model):
    serial=models.IntegerField(default=0)
    class_roll=models.CharField(max_length=10,)
    name=models.CharField(max_length=100,blank=True, null=True)
    subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)    
    exam=models.ForeignKey(Exam,blank=True,null=True,on_delete=models.SET_NULL)
    MCQ=models.IntegerField(blank=True,null=True)
    CQ=models.IntegerField(blank=True,null=True)
    practical=models.IntegerField(blank=True,null=True)
    total=models.IntegerField(blank=True,null=True)
    grade=models.CharField(max_length=150,blank=True,null=True)
    cgpa=models.CharField(max_length=150,blank=True,null=True)
     
    class Meta:
        ordering = ['serial']
        unique_together=('class_roll','subject','exam')
    def __str__(self):
        if self.subject is not None:
            return self.class_roll+': '+self.subject.name_en
        return self.class_roll
    def subject_name(self):
        if self.subject is not None:
            return self.subject.name_en
    def before_save_instance(self, instance, using_transactions, dry_run):
        print(instance)
    def save(self, *args, **kwargs):
        total=0
        if self.subject:
            group=Group.objects.filter(id=3).first()
            subj=Subject.objects.filter(name_en=self.subject.name_en).first()

            if group in subj.group.all():
                if self.CQ:
                    total=total+self.CQ
                    if self.CQ<17:
                        self.grade="F"
                        self.cgpa=0
                else:
                    self.grade="Absent"
                    self.cgpa=None
                    
                if self.MCQ:
                    total=total+self.MCQ
                    if self.MCQ<8:
                        self.cgpa=0
                        self.grade="F"
                else:
                    self.grade="Absent"
                    self.cgpa=None
                
                if self.practical:
                    print("practical")
                    total=total+self.practical
                    if self.practical<8:
                        self.cgpa=0
                        self.grade="F"
                else:
                    total=round(total*(100/75), 2)
            else:
                if self.subject.id==2:
                    if self.CQ:
                        total=total+self.CQ
                        if self.CQ<33:
                            self.grade="F"
                            self.cgpa=0
                    else:
                        self.grade="Absent"
                        self.cgpa=None
                else:
                    if self.CQ:
                        total=total+self.CQ
                        if self.CQ<23:
                            self.grade="F"
                            self.cgpa=0
                    else:
                        self.grade="Absent"
                        self.cgpa=None
                    

                    if self.MCQ:
                        total=total+self.MCQ
                        if self.MCQ<10:
                            self.cgpa=0
                            self.grade="F"
                    else:
                        self.grade="Absent"
                        self.cgpa=None
                    
                        


            self.total=total

            if self.grade == 'F':
                self.cgpa=0
            elif self.grade == 'Absent':
                self.cgpa=None
            else: 
                if total<33:
                    self.cgpa=0
                    self.grade="F"

                elif total>=33 and total<40:
                    self.cgpa=1
                    self.grade="D"

                elif total>=40 and total<50:
                    self.cgpa=2
                    self.grade="C"
                elif total>=50 and total<60:
                    self.cgpa=3
                    self.grade="B"
                elif total>=60 and total<70:
                    self.cgpa=3.5
                    self.grade="A-"
                elif total>=70 and total<80:
                    self.cgpa=4
                    self.grade="A"
                else:
                    self.cgpa=5
                    self.grade="A+"



        super(Marks, self).save(*args, **kwargs)

class Result(models.Model):
    class_roll=models.CharField(max_length=255,)
    name=models.CharField(max_length=255,blank=True, null=True)
    position=models.IntegerField(blank=True,null=True)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    section=models.CharField(max_length=255,blank=True, null=True)
    exam=models.ForeignKey(Exam,blank=True,null=True,on_delete=models.SET_NULL)
    total=models.IntegerField(blank=True,null=True)
    grade=models.CharField(max_length=255,blank=True,null=True)
    cgpa=models.CharField(max_length=255,blank=True,null=True)
    number_of_subject=models.IntegerField(blank=True,null=True)
    present_at=models.IntegerField(blank=True,null=True)
    absent_at=models.IntegerField(blank=True,null=True)
    fail_at=models.IntegerField(blank=True,null=True)
    pass_at=models.IntegerField(blank=True,null=True)
    absent_or_fail_at=models.IntegerField(blank=True,null=True)
    minimum_pass=models.IntegerField(blank=True,null=True)
    remarks=models.CharField(max_length=255,blank=True,null=True)
    class Meta:
        ordering = ['-group','-position']
    def __str__(self):
        if self.class_roll is not None:
            return self.class_roll+': '+self.name
        return self.class_roll
    def save(self, *args, **kwargs):
        if self.absent_at != None and self.fail_at != None:
            self.absent_or_fail_at=self.absent_at +self.fail_at
        else:
            self.absent_or_fail_at=self.absent_at
        super(Result, self).save(*args, **kwargs)


    
class FinalResult(models.Model):
    class_roll=models.CharField(max_length=255)
    name=models.CharField(max_length=255,blank=True, null=True)
    position=models.IntegerField(blank=True,null=True)
    group=models.ForeignKey(Group,blank=True,null=True,on_delete=models.SET_NULL)
    section=models.CharField(max_length=255,blank=True, null=True)
    exam=models.ForeignKey(Exam,blank=True,null=True,on_delete=models.SET_NULL)
    total=models.IntegerField(blank=True,null=True)
    grade=models.CharField(max_length=255,blank=True,null=True)
    cgpa=models.CharField(max_length=255,blank=True,null=True)
     
    class Meta:
        ordering = ['group','position']
    def __str__(self):
        if self.class_roll is not None:
            return self.class_roll+': '+self.name
        return self.class_roll

class Choice(models.Model):
    class_roll=models.CharField(max_length=255)
    name=models.CharField(max_length=255,blank=True, null=True)
    subject1=models.ForeignKey(Subject,related_name='subject1',blank=True,null=True,on_delete=models.SET_NULL)
    subject2=models.ForeignKey(Subject,related_name='subject2',blank=True,null=True,on_delete=models.SET_NULL)
    subject3=models.ForeignKey(Subject,related_name='subject3',blank=True,null=True,on_delete=models.SET_NULL)
    subject4=models.ForeignKey(Subject,related_name='subject4',blank=True,null=True,on_delete=models.SET_NULL)
    subject5=models.ForeignKey(Subject,related_name='subject5',blank=True,null=True,on_delete=models.SET_NULL)
    subject6=models.ForeignKey(Subject,related_name='subject6',blank=True,null=True,on_delete=models.SET_NULL)

    fourth_subject=models.ForeignKey(Subject,blank=True,null=True,on_delete=models.SET_NULL)
    class Meta:
        ordering = ['class_roll']
    def __str__(self):
        if self.class_roll is not None:
            return self.class_roll+': '+self.name
        return self.class_roll
