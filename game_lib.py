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
    print('rozpoczynam nową grę')
    ustawienia=  get_settings(event)

    # losujemy pola, które mają zostać zaminowane
    wszystkie_pola = ustawienia['wszystkie_pola']
    ile = ustawienia['liczba_wszystkich_min'].get()
    ustawienia['pola_z_minami'] = losuj_miny(wszystkie_pola, ile)

    # aktualizujemy liczniki
    ustawienia['rozegrane_gry'].set(ustawienia['rozegrane_gry'].get() + 1)
    ustawienia['liczba_ukrytych_min'].set(ile)

    # czyszczenie pola
    for pole in wszystkie_pola:
        pole.configure(text=FIELD_EMPTY, state=tk.NORMAL)

    # aktualizuję liczniki na polach
    notify_neightbours(ustawienia)

def losuj_miny(wszystkie_pola, ile):
    """
        Wybiera ze zbioru zadaną liczbę pól,
        które mają zawierać miny.
    """
    wylosowane = []
    while len(wylosowane) < ile:
        pole = random.choice(wszystkie_pola)
        if pole not in wylosowane:
            wylosowane.append(pole)
            lokalizacja = pole.grid_info()
            print('Wylosowałem {0}x{1}'.format(
                lokalizacja['row'], lokalizacja['column']
            ))
    return wylosowane


def notify_neightbours(ustawienia):
    """
        Ustawia liczniki min w sąsiedztwie pola.
    """
    zakres = (-1, 0, 1)
    dlugosc_pola = range(10)
    pola_z_minami = ustawienia['pola_z_minami']
    liczniki_pol = {}
    for mina in pola_z_minami:
        mina_loc = mina.grid_info()
        mina_x = mina_loc['column']
        mina_y = mina_loc['row']
        for x in zakres:
            for y in zakres:
                somsiad_x = mina_x + x
                somsiad_y = mina_y + y
                if somsiad_x in dlugosc_pola and somsiad_y in dlugosc_pola:
                    somsiad = ustawienia['siatka'][(somsiad_x, somsiad_y)]
                    if somsiad not in pola_z_minami:
                        if somsiad in liczniki_pol:
                            liczniki_pol[somsiad] += 1
                        else:
                            liczniki_pol[somsiad] = 1
    ustawienia['liczniki_pol'] = liczniki_pol


def oznacz_pole(event):
    """
        Oznacza dane pole jako zawierające minę.
    """
    print('oznaczam pole')
    pole = event.widget
    ustawienia = get_settings(event)
    licznik_min = ustawienia['liczba_ukrytych_min']
    if pole in ustawienia['pola_oznaczone']:
        pole.configure(text=FIELD_CLEAN)
        ustawienia['pola_oznaczone'].remove(pole)
        licznik_min.set(licznik_min.get() + 1)
    else:
        pole.configure(text=FIELD_MARKED)
        ustawienia['pola_oznaczone'].append(pole)
        licznik_min.set(licznik_min.get() - 1)

    if licznik_min.get() == 0:
        for pole in ustawienia['pola_oznaczone']:
            if pole not in ustawienia['pola_z_minami']:
                return
        messagebox.showinfo('Koniec gry!', 'Wąż może pić')

def odkryj_pole(event):
    """
        Odkrywa pole minowe
    """
    pole = event.widget
    lokalizacja = pole.grid_info()
    print('Odkrywam {0}x{1}'.format(
        lokalizacja['row'],
        lokalizacja['column']
    ))
    ustawienia = get_settings(event)
    if pole in ustawienia['pola_z_minami']:
        pole.configure(text=FIELD_MINE)
        messagebox.showwarning('Koniec Gry!', 'Wąż zdetonował minę')
    else:
        pole.configure(text=ustawienia['liczniki_pol'].get(pole, FIELD_EMPTY))
