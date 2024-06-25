from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'games/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('game_list')


@login_required
def game_list(request):
    games = Game.objects.all()
    return render(request, 'games/game_list.html', {'games': games})

@login_required
def inicial(request):
    games = Game.objects.all()
    return render(request, 'games/inicial.html', {'games': games})

@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', {'form': form})

@login_required
def game_update(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'games/game_form.html', {'form': form})

@login_required
def game_delete(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'games/game_confirm_delete.html', {'game': game})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})