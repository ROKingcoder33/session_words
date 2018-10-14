from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(req):
    if 'word_list' not in req.session:
        req.session['word_list'] = []
    context = {
        'title': 'Session Words',
    }
    return render(req, 'main/index.html', context)

def add_word(req):
    if req.method != 'POST':
        return redirect('/')

    if 'size' not in req.POST:
        size = 'small'
    else:
        size = 'big'

    word = {
        'word': req.POST['word'],
        'color': req.POST['color'],
        'size': size
    }
    req.session['word_list'].append(word)
    req.session.modified = True
    return redirect('/')

def clear(req):
    req.session.clear()
    return redirect('/')
