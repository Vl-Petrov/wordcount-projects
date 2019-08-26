from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')


def wordcount(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    worddic = {}
    for word in words:
        if word in worddic:
            worddic[word] +=1
        else:
            worddic[word] = 1
    sortwords = sorted(worddic.items(), key = operator.itemgetter(1), reverse = True)
    return render(request, 'wordcount.html', {'fulltext':fulltext, 'words':len(words), 'worddic': sortwords})


def about(request):
    return render(request, 'about.html')
