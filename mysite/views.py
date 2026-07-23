# i  have create this file
from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import default


def index(request):
    return render(request,'index.html')
    # return HttpResponse("Home")


def analyze(request):
    #get text
    djtext =request.POST.get('text','default')


    #for checkfox valuue
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newline=request.POST.get('newlineremover','off')
    spaceremove=request.POST.get('extraspaceremever','off')
    charcount=request.POST.get('charcouter','off')

    #analyzed text and check which checkbox is on
    if removepunc == "on" :
        # analyzed=djtext      for   as it is texr without removing punc..
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'remove Punctuation', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to upperCase', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if newline=="on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed=analyzed+char
        params = {'purpose': 'Romove new Lines', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if spaceremove=="on":
        analyzed=""
        for index , char in enumerate(djtext):

    # Why use enumerate?  It automatically keeps count of the position of each element
            if not (djtext[index] == " " and djtext[index+1]==" "):
                analyzed=analyzed+char
        params = {'purpose': 'Romove new Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char
            charlen=len(analyzed)

        params = {'purpose': 'Charector and length', 'analyzed_text': analyzed,'char_count': charlen}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (removepunc != "on" and fullcaps != "on" and newline != "on" and spaceremove != "on" and charcount != "on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)

