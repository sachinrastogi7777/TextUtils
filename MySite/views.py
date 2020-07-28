# This file is created by :- Sachin

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    removenewline = request.POST.get('removenewline','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    # check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punchuations', 'analyzed_text':analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text':analyzed}
        djtext = analyzed
    if extraspaceremover == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed += char
        params = {'purpose': 'Text after removal of Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed
    if removenewline == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'Text after removal of Newline', 'analyzed_text': analyzed}
    if removenewline!='on' and removepunc!='on' and extraspaceremover!='on' and fullcaps!='on':
        return HttpResponse('Error')
    return render(request,'analyze.html',params)


