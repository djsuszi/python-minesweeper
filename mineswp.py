"""
    Saper - moduł głównego interfejsu graficznego Tkinter.
"""

# import biblioteki graficznej do obsługi okienek GUI
import tkinter as tk
from tkinter import ttk, N, S, W, E
from game_lib import (
    LMOUSE_CLICK_EVENT,
    RMOUSE_CLICK_EVENT,
    DEFAULT_MINE_COUNT,
    odkryj_pole,
    oznacz_pole,
    nowa_gra
)


def create_minesweeper_window():
    """
        Funkcja inicjuje komponenty graficzne Tk.
        Zwraca obiekt okna gotowy do uruchomienia (wyświetlenia).
    """

    # Poniżej znajdują się instrukcje inicjalizujące komponenty graficzne okna Tk
    # (deklaracje widgetów, umiejscowienie ich w oknie, przypisanie funkcji do zdarzeń)

    # okno główne
    root_window = tk.Tk()
    root_window.title("Wężowy saper")

    # ramka główna- podstawowy kontener na pozostałe widgety
    mainframe = ttk.Frame(root_window, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root_window.columnconfigure(0, weight=1)
    root_window.rowconfigure(0, weight=1)

    # dodawanie przycisków reprezentujących pole minowe w rozmiarze 10x10
    fields_grid = {}
    for row_num in range(10):
        for col_num in range(10):
            field_button = ttk.Button(
                mainframe,
                text=" ",
                width=2,
                state=tk.DISABLED,
            )
            field_button.grid(column=row_num, row=col_num, sticky=W)
            field_button.bind(LMOUSE_CLICK_EVENT, odkryj_pole)
            field_button.bind(RMOUSE_CLICK_EVENT, oznacz_pole)
            # zapamiętanie przycisku na liście pod indeksem
            fields_grid[(row_num, col_num)] = field_button

    # liczniki gry
    var_total_mines = tk.IntVar(value=DEFAULT_MINE_COUNT)
    var_games_played = tk.IntVar(value=0)
    var_hidden_mines = tk.IntVar(value=DEFAULT_MINE_COUNT)

    # dodanie statycznych etykietek informacyjnych
    ttk.Label(mainframe, text="Gra:").grid(column=0, row=11, columnspan=5, sticky=W)
    ttk.Label(mainframe, text="Pozostało min:").grid(column=0, row=12, columnspan=5, sticky=W)
    # wartości dla etykiet
    ttk.Label(mainframe, textvariable=var_games_played).grid(column=7, row=11, columnspan=5, sticky=E)
    ttk.Label(mainframe, textvariable=var_hidden_mines).grid(column=7, row=12, columnspan=5, sticky=E)

    # polte tekstowe na wpisanie liczby min do rozmieszczenia
    mine_count_input = ttk.Entry(mainframe, width=7, textvariable=var_total_mines)
    mine_count_input.grid(column=0, row=13, columnspan=5, sticky=W)

    # definicja przycisku nowej gry
    new_game_button = ttk.Button(mainframe, text="Nowa gra")
    new_game_button.grid(column=7, row=13, columnspan=5, sticky=W)
    new_game_button.bind(LMOUSE_CLICK_EVENT, nowa_gra)

    # zapamiętanie pod jednym obiektem "konfiguracji" okna
    # przycisków oraz liczników gry
    mainframe.game_settings = {
        # liczniki gry
        'rozegrane_gry': var_games_played,  # licznik sesji
        'liczba_ukrytych_min': var_hidden_mines,  # aktualna liczba nierozbrojonych min
        'liczba_wszystkich_min': var_total_mines,  # całkowita liczba min na polu
        # ustawienia min
        'siatka': fields_grid,  # pola (wraz z indeksami)
        'wszystkie_pola': list(fields_grid.values()),  # wszystkie pola
        'pola_z_minami': [],  # pola zazbrojone miną
        'pola_oznaczone': [],  # pole oznaczone przez gracza
        'liczniki_pol': {}  # informacje o licznikach w polach
    }

    # zwrócenie gotowego obiektu, który należy aktywować przez wywołanie:
    # root_window.mainloop()
    # uruchomienie rysuje okienka graficzne i uruchamia nasłuch na zdarzenia
    # (np. klikanie przez użytkownika)

    return root_window
