from django.shortcuts import render, redirect
from .models import Game


def home(request):
    if request.method == 'POST':
        words = request.POST['word']
        game = Game.objects.create(words=words)

        return redirect('hangman:play', game.id)

    return render(request, 'hangman/index.html')


def play(request, game_id):
    game = Game.objects.get(id=game_id)
    feedback = ""

    if request.method == 'POST':
        letter = request.POST['letter']
        game.guessed_word += letter
        if letter.lower() not in game.words:
            game.attempts_left -= 1
            if game.attempts_left == 0:
                feedback = "You have failed, the correct word should be {}".format(game.words)
        elif all(char.lower() in game.guessed_word.lower() for char in game.words):
            feedback = "Congratulations, you guessed the word correctly"

    game.save()
    return render(request, 'hangman/play.html', {'game':game, 'feedback':feedback})

