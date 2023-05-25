from django.shortcuts import render,redirect
from StudyApp.models import Notes,Attendance_Report,Student,Subject,Student_Notification,Student_Feedback,Student_leave,StudentResult,Lesson,Submission
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='login/')
def HOME(request):
    return render(request,'Student/home.html')


@login_required(login_url='login/')
def STUDENT_NOTIFICATION(request):

    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification':notification,
        }

    return render(request,'Student/notification.html',context)


@login_required(login_url='login/')
def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):

    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')

@login_required(login_url='login/')
def STUDENT_FEEDBACK(request):

    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_Feedback.objects.filter(student_id = student_id)

    context = {
        'feedback_history':feedback_history
    }

    return render(request,'Student/feedback.html',context)

@login_required(login_url='login/')
def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)
        feedbacks = Student_Feedback(
            student_id = student,
            feedback = feedback,
            feedback_reply = "",

        )

        feedbacks.save()
        return redirect('student_feedback')


@login_required(login_url='login/')
def STUDENT_LEAVE(request):

    student = Student.objects.get(admin = request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id = student)

    context = {
        'student_leave_history':student_leave_history
    }

    return render(request,'Student/apply_leave.html',context)


@login_required(login_url='login/')
def STUDENT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')

        leave_message = request.POST.get('leave_message')
        student_id = Student.objects.get(admin = request.user.id)

        student_leave = Student_leave(
            student_id = student_id,
            data = leave_date,
            message = leave_message
        )

        student_leave.save()
        messages.success(request,'Leave Are Successfully Sent!')
        return redirect('student_leave')


@login_required(login_url='login/')
def STUDENT_VIEW_ATTENDANCE(request):

    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')

    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

            
            attendance_report = Attendance_Report.objects.filter(student_id = student, attendance_id__subject_id = subject_id)
            

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
        
    }

    return render(request,'Student/view_attendance.html',context)


@login_required(login_url='login/')
def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin = request.user.id)

    result = StudentResult.objects.filter(student_id = student)
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark


    context = {
        'result':result,
        'mark':mark
    }

    return render(request,'Student/view_result.html',context)

@login_required(login_url='login/')
def STUDENT_VIEW_LESSON(request):

    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)
    submissions = Submission.objects.filter(student_id = student)
    action = request.GET.get('action')
    get_subject = None
    lessons = None

    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        get_subject = Subject.objects.get(id = subject_id)
        lessons = Lesson.objects.filter(subject_id = subject_id)
        

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'lessons':lessons,
        'submissions':submissions,
    }

    return render(request,'Student/view_lesson.html',context=context)

@login_required(login_url='login/')
def STUDENT_EDIT_ASSIGNMENT(request,sub_id,les_id):

    student_id = Student.objects.get(admin = request.user.id)
    lesson_id = Lesson.objects.get(id = les_id)

    context = {
        'student':student_id,
        'lesson':lesson_id,
    }

    return render(request,'Student/send_assignment.html',context=context)

@login_required(login_url='login/')
def STUDENT_SEND_ASSINGMENT(request):
    
    if request.method == "POST":
        lesson_id = request.POST.get('lesson_id')
        student_id = request.POST.get('student_id')
        submission_file = request.FILES.get('submission_file')

        lesson = Lesson.objects.get(id = lesson_id)
        student = Student.objects.get(id = student_id)

        # Check if the student has already submitted for the lesson
        existing_submission = Submission.objects.filter(lesson_id = lesson, student_id = student).exists()
        if existing_submission:
            messages.error(request,'You have already submitted an assignment for this lesson.')
            return redirect('student_view_lesson')
        else:
            submission = Submission(lesson_id = lesson ,student_id=student,submission_file=submission_file,submission_status = 1)
            submission.save()
            messages.success(request,'Assignment has been submitted!')
        return redirect('student_view_lesson')

    return render(request,'Student/view_lesson.html')


@login_required(login_url='login/')
def VIEW_ALL_NOTES(request):

    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)

    context = {
        'subjects':subjects
    }

    return render(request,'Student/my_notes.html',context=context)


@login_required(login_url='login/')
def VIEW_NOTES(request,sub_id):

    student = Student.objects.get(admin = request.user.id)
    subject = Subject.objects.filter(id = sub_id)
    notes = Notes.objects.filter(student_id = student, subject_id = sub_id)

    context = {
        'subject':subject,
        'student':student,
        'notes':notes,
    }

    return render(request,'Student/note.html',context=context)


@login_required(login_url='login/')
def ADD_NOTES(request,sub_id):

    student = Student.objects.get(admin = request.user.id)
    subject = Subject.objects.get(id = sub_id)

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        subject_id = request.POST.get('subject_id')
        topic = request.POST.get('topic')
        content = request.POST.get('content')

        student = Student.objects.get(id = student_id)
        subject = Subject.objects.get(id = subject_id)

        note = Notes(
            student_id = student,
            subject_id = subject,
            topic = topic, 
            content = content,
        )

        note.save()
        messages.success(request,'Notes Are Successfully Added')
        return redirect('view_notes',sub_id)

    context = {
        'subject':subject,
        'student':student,     
    }

    return render(request,'Student/Add_Notes.html',context=context)