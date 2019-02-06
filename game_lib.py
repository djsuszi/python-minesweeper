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
            'rozegrane_gry'  # licznik sesji
            'liczba_ukrytych_min'  # aktualna liczba nierozbrojonych min
            'liczba_wszystkich_min'  # całkowita liczba min na polu

            # ustawienia min
            siatka': fields_grid,  # pola (wraz z indeksami)
            wszystkie_pola': list(fields_grid.values()),  # wszystkie pola
            pola_z_minami': [],  # pola zazbrojone miną
            pola_oznaczone': [],  # pole oznaczone przez gracza
            liczniki_pol': {}  # informacje o licznikach w polach
    """
    settings = event.widget.master.game_settings
    if name:
        return settings[name]
    return settings


def nowa_gra(event):
    """
        Przygotowuje pole minowe.
        Rozmieszcza w wylosowanych miejscach miny.
        Pozostałe pola wypełniane są licznikami informującymi o
        liczbie bezpośrednio sąsiadujących min.
    """
    pass


def losuj_miny(all_fields, select_count):
    """
        Wybiera ze zbioru zadaną liczbę pól,
        które mają zawierać miny.
    """
    pass


def notify_neightbours(settings):
    """
        Ustawia liczniki min w sąsiedztwie pola.
    """
    pass


def oznacz_pole(event):
    """
        Oznacza dane pole jako zawierające minę.
    """
    pass


def odkryj_pole(event):
    """
        Podejmuje próbę rozbrojenia pola.
        Jeśli w polu jest mina, gra kończy się.
        W przeciwnym wypadku w polu pojawi się informacja
        o liczbie min w bezpośrednim sąsiedztwie.
    """
    pass
