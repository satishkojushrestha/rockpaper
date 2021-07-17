from django.shortcuts import render
import random

def index(request):
    return render(request, 'index.html')

a = ''
score = 0

def welcome(request,id):
    global a
    if request.method == 'POST':
        name = request.POST["name"]
        a = name
        return render(request,'welcome.html',{
            "names":name,
        })
    
    message, score, user, computer = game(id)
    if computer=='r':
        computer = 'rock'

    if computer=='s':
        computer = 'scissor'
    
    if computer=='p':
        computer = 'paper'

    if user=='r':
        user = 'rock'

    if user=='s':
        user = 'scissor'
    
    if user=='p':
        user = 'paper'

    return render(request,'welcome.html',{
            "names":a,
            "message":message,
            "score":score,
            "user":user,
            "computer":computer
        })
    


def game(id,computer=''):
    user = ''
    game_list = ['r','p','s']
    cont = 0
    global score

    if id == 1:
        user = 'r'
    elif id == 2:
        user = 'p'
    elif id == 3:
        user = 's'
    elif id == 100:
        score = 0
    else:
        cont = 1

    if cont != 1 and id != 100:
        computer = random.choice(game_list)
        score = score
        if computer == user:
            return "Its a tie", score, user, computer

        if is_won(user, computer):
            score += 1
            return "You won!", score, user, computer
    
    return "You loose", score, user, computer


def is_won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
        
