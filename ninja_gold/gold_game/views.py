from django.shortcuts import render, redirect
import random


# Create your views here.
    
def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
        request.session['activity'] = []
        request.session['end'] = False

    context = {
        'places': {
            'farm': "(earns 10-20 gold)",
            'cave': "(earns 5-10 gold)",
            'house': "(earns 2-5 gold)",
            'casino': "(earns/loses 0-50 gold)"

        }
    }
    return render(request, 'index.html', context)

def process_money(request, place):
    if place == 'farm':
        print("farm time baby!")
        gold_create = round(random.random()*10+10)
        request.session['gold'] += gold_create
        request.session['activity'].append(f" You visited the farm and gained {gold_create} gold.")
    elif place == 'cave':
        print("going down into the cave")
        gold_create = round(random.random()*5+5)
        request.session['gold'] += gold_create
        request.session['activity'].append(f" You visited the cave and gained {gold_create} gold.")
    elif place == 'house':
        print("going back to the house")
        gold_create = round(random.random()*2+3)
        request.session['gold'] += gold_create
        request.session['activity'].append(f" You visited the house and gained {gold_create} gold.")
    else:
        print("going to the casino!")
        gold_create = round(random.random()*100-50)
        request.session['gold'] += gold_create
        if gold_create > 0:
            request.session['activity'].append(f" You visited the casino and gained {gold_create} gold.")
        else:
            request.session['activity'].append(f" You visited the casino and lost {gold_create} gold.")
    if request.session['gold'] >= request.session['win']:
        request.session['end'] = True

    return redirect('/')

def win_condition(request):
    if request.method == 'POST':
        request.session['win'] = int(request.POST['win'])
        return redirect('/')
    else:
        return redirect('/')
        
    
def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    request.session.flush()
    return redirect('/')

