from django.http import HttpResponse
from django.shortcuts import render
from .models import Marks,Student,Exam,Result
from .forms import SeachResultForm
# Create your views here.

def searchResult(request):
    context={}
    flag1=0
    flag2=0
    
    if request.method=='POST':
        totalgpa=0
        result=Marks.objects.filter(class_roll=request.POST.get('roll').strip())
        student=Student.objects.filter(class_roll=request.POST.get('roll').strip()).first()
        exam=Exam.objects.filter(id=request.POST.get('exam')).first()
        context['result']=result
        context['student']=student
        context['exam']=exam
        
        for reslt in result:
            if reslt.grade=="Absent":
                grade="Absent"
                cgpa=None
                context['grade']=grade
                context['cgpa']=cgpa
                flag1=1
                return render(request, 'result/show_result.html', context=context)

            elif reslt.grade=="F":
                grade="F"
                cgpa=0
                context['grade']=grade
                context['cgpa']=cgpa
                flag2=1
                
            else:
                #print(student.fourth_subject,reslt.subject)
                if student:
                    if reslt.subject == student.fourth_subject:
                        cg=float(reslt.cgpa)
                        if cg>2:
                            gpa=cg-2
                            totalgpa=totalgpa+gpa

                    else:
                        totalgpa=totalgpa+float(reslt.cgpa)
        if flag2==1:
            return render(request, 'result/show_result.html', context=context)
        
        else:
            #print(grade)
            cgpa=totalgpa/6
            context['cgpa']=round(cgpa,2)
            if cgpa<1:
                grade="F"
            elif cgpa>=1 and cgpa<2:
                grade="D"
            elif cgpa>=2 and cgpa<3:
                grade="C"
            elif cgpa>=3 and cgpa<3.5:
                grade="B"
            elif cgpa>=3.5 and cgpa<4:
                grade="A-"
            elif cgpa>=4 and cgpa<5:
                grade="A"
            elif cgpa>=5:
                grade="A+"
            else:
                grade="Absent"
            context['grade']=grade

        
        
   
        return render(request, 'result/show_result.html', context=context)
    form=SeachResultForm()
    context['form']=form
    return render(request, 'result/search_result.html', context=context)

def createResult(request):
        rolls=list(Marks.objects.filter(exam=1).values('class_roll').order_by('class_roll').distinct())
        exam=Exam.objects.filter(id=1).first()
        count=0
        for roll in rolls:
            print(roll['class_roll'])
            result=Marks.objects.filter(class_roll=roll['class_roll'])
            student=Student.objects.filter(class_roll=roll['class_roll']).first()
            totalgpa=0
            total=0
            flag1=0
            flag2=0
            for reslt in result:
                if reslt.grade=="Absent":
                    grade="Absent"
                    cgpa=None
                    flag1=1

                elif reslt.grade=="F":
                    grade="F"
                    cgpa=0
                    flag2=1
                    total=total+reslt.total

                    
                else:
                    #print(student.fourth_subject,reslt.subject)
                    if student:
                        if reslt.subject == student.fourth_subject:
                            cg=float(reslt.cgpa)
                            total=total+reslt.total

                            if cg>2:
                                gpa=cg-2
                                totalgpa=totalgpa+gpa

                        else:
                            total=total+reslt.total
                            totalgpa=totalgpa+float(reslt.cgpa)
            if flag1==1 and flag2==1 :
                if student:
                    result_individual=Result.objects.create(class_roll=roll['class_roll'],name=student.name,position=count,group=student.group,section=student.section,exam=exam,total=1,cgpa=cgpa,grade=grade)
            else:
                #print(grade)
                cgpa=round(totalgpa/6,2)

                if cgpa<1:
                    grade="F"
                elif cgpa>=1 and cgpa<2:
                    grade="D"
                elif cgpa>=2 and cgpa<3:
                    grade="C"
                elif cgpa>=3 and cgpa<3.5:
                    grade="B"
                elif cgpa>=3.5 and cgpa<4:
                    grade="A-"
                elif cgpa>=4 and cgpa<5:
                    grade="A"
                elif cgpa>=5:
                    grade="A+"
                else:
                    grade="Absent"
                if student:
                    print(student.name)
                    result_individual=Result.objects.create(class_roll=roll['class_roll'],name=student.name,position=count,group=student.group,section=student.section,exam=exam,total=total,cgpa=cgpa,grade=grade)
            count=count+1

            
        
        print(count,result)

        return HttpResponse('ok')

