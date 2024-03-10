from django.shortcuts import render, redirect
from .models import ReportReview
from campaign.models import Review
from .forms import ReportCommentForm
from django.contrib import messages

# Create your views here.

def report_comment(request, id):
    review = Review.objects.get(id=id)

    if request.method == 'POST':
        print('post request')
        report_form = ReportCommentForm(request.POST)
        print('where data',report_form)
        if report_form.is_valid():
            print('vaild form')
        
            report_form = report_form.save(commit=False)
            # report_form.reason = request.POST['reason']
            report_form.review = review
            report_form.reporter = request.user
            report_form.save()
            messages.success(request, 'Thank you for reporting this comment.')


    else:
        print('not vaild')
        report_form = ReportCommentForm()

    context = {
        'form' : report_form
    }
    return render(request, 'reports/report_comment.html', context)