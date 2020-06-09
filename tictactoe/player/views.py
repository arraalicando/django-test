from django.shortcuts import render
from gameplay.models import Game


# Create your views here.


def home(request):
    current_user_games = Game.objects.filter(
        firstPlayer=request.user,
        status='F'
    ) | Game.objects.filter(
        secondPlayer=request.user,
        status='S'
    )

    return render(request, "player/home.html",
                  {'gameCount': current_user_games.count(),
                   'games': list(current_user_games),
                   'user': request.user})
