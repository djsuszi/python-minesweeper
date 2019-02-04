"""
    Biblioteka funkcji wykonujących akcje interfejsu graficznego.
"""

import random
import tkinter as tk
from tkinter import messagebox

LMOUSE_CLICK_EVENT = '<1>'
RMOUSE_CLICK_EVENT = '<3>'
DEFAULT_MINE_COUNT = 10
FIELD_EMPTY = ' '
FIELD_MARKED = '?'
FIELD_MINE = 'X'
FIELD_CLEAN = '.'


def get_settings(event, name=None):
    """
        Funkcja pomocnicza do pobierania obiektów konfiguracji okna.
        Jeśli nie podano nazwy parametru, zwracany jest cały słownik ustawień.

        Ustawienia gry:
            # liczniki gry
            'var_games_played': var_games_played,  # licznik sesji
            'var_hidden_mines': var_hidden_mines,  # aktualna liczba nierozbrojonych min
            'var_total_mines': var_total_mines,  # całkowita liczba min na polu

            # ustawienia min
            fields_grid': fields_grid,  # pola (wraz z indeksami)
            all_fields': list(fields_grid.values()),  # wszystkie pola
            fields_with_mines': [],  # pola zazbrojone miną
            fields_marked': [],  # pole oznaczone przez gracza
            fields_counters': {}  # informacje o licznikach w polach
    """
    settings = event.widget.master.game_settings
    if name:
        return settings[name]
    return settings


def start_new_game(event):
    """
        Przygotowuje pole minowe.
        Rozmieszcza w wylosowanych miejscach miny.
        Pozostałe pola wypełniane są licznikami informującymi o
        liczbie bezpośrednio sąsiadujących min.
    """
    pass


def setup_mines(all_fields, select_count):
    """
        Wybiera ze zbioru zadaną liczbę pól.
    """
    pass


def notify_neightbours(settings):
    """
        Ustawia liczniki min w sąsiedztwie pola.
    """
    pass


def mark_field_with_mine(event):
    """
        Oznacza dane pole jako zawierające minę.
    """
    pass


def defuse_mine(event):
    """
        Podejmuje próbę rozbrojenia pola.
        Jeśli w polu jest mina, gra kończy się.
        W przeciwnym wypadku w polu pojawi się informacja
        o liczbie min w bezpośrednim sąsiedztwie.
    """
    pass
