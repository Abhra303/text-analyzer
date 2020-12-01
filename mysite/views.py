#i have created this file -- abhra
from django.http import HttpResponse
from django.shortcuts import render
# file = open("mysite/about.txt","rt")
# heading = file.readline()
# content = file.read()
# file.close()
heading = "hello world via variable"

def index(request):
    param = {'name':'harry','geta':'gusar','mob':45864}
    return render(request,"index2.html",param)
    # return render(request,"index.html")
    # return HttpResponse("hello world")

# def about(request):
#     return HttpResponse(f"<h2>{heading}</h2><pre><!--content--></pre>")


# def charcount(request):
#     return HttpResponse('''charcount <a href="about">home</a>''') #we can also write '/' in href to back example--> <a href ='/'>

def removepunc(request):
    text = request.POST.get('text','default') # second parameter is default if first parameter has nothing 
    removepuncelem = request.POST.get('removepunc','off')
    punctuations = '''"':;!(){}[]-*/+\,<>?~`@#$%^&_.'''
    analyzed = ""
    if removepuncelem == 'on':
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'punctuation':text,'analyzed':analyzed}
        return render(request,"analyzer.html",param)
    else:
        return HttpResponse("error has occured!!")




