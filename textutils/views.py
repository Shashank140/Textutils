# I created this file - Shashank
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse('''Harry  Django CodeWithHarry''')
    return render(request, 'index.html')

#def about(request):
#   return HttpResponse("About Harry Bhai")
#def removepunc(request):
    #Get the text
 #   djtext = request.GET.get('text', 'default')
  #  print(djtext)
    #Analyze the text
   # return HttpResponse("remove punc")
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')




    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text

        return render(request, 'analyze.html', params)

    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if (djtext[index] == " " and djtext[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        # Analyze the text
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')

def capfirst(request):
    return HttpResponse("capitalize first")