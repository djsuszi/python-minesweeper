"""
    Gra "Saper" - wersja napisana w Python przy użyciu modułu Tkinter.
    Moduł główny.
"""
from mineswp import create_minesweeper_window

# import obiektu gry
root_window = create_minesweeper_window()
# uruchomienie gry (wywołanie interfejsu graficznego)
root_window.mainloop()
