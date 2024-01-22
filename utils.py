import os
import tempfile
import pickle
import battleship

def get_option_from_list(options: dict):
    """Repeatedly gets standard input until the input is a valid option in the dict keys, then returns it."""
    while True:
        for i,v in options.items():
            print(f'{i}. {v[0]}')
        eleccion = input()
        if eleccion in options.keys():
            return eleccion
        print('Opción inválida. Por favor elige una opción de la lista.')

def cls():
    """Clears the terminal screen."""
    os.system('cls' if os.name=='nt' else 'clear')

def get_savefile_path():
    """Returns the savefile path, which is located in the temp folder of the system."""
    return tempfile.gettempdir() + '/battleship.pickle'

def guardar_partida(partida: battleship.Game):
    """Saves a battleship game to a file in the savefile path."""
    with open(get_savefile_path(), 'wb') as f:
        pickle.dump(partida, f)

def cargar_partida() -> battleship.Game | None:
    """Tries to load a battleship game from a file in the savefile path and returns it, or None if it fails to load it."""
    try:
        with open(get_savefile_path(), 'rb') as f:
            return pickle.load(f)
    except:
        return None