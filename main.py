import game
import pickle
import os
import re

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def get_option_from_list(options: dict):
    while True:
        for i,v in options.items():
            print(f'{i}. {v[0]}')
        eleccion = input()
        if eleccion in options.keys():
            return eleccion
        print('Opción inválida. Por favor elige una opción de la lista.')

def guardar():
    pass

def turno(jugada):
    if jugada == 'G':
        guardar()
        return 'Partida guardada.'
    elif jugada_regex := re.fullmatch(r'([A-J])([0-9]+)',jugada):
        row, col = jugada_regex.group(1,2)
        return f'Elegida casilla {row}{col}'

def ejecutar_partida(current_game: game.BattleshipGame):
    resultado_turno = ''
    while True:
        cls()
        print(current_game.get_board())
        print(f'Turno {current_game.current_turn} de {current_game.max_turns}')
        print(resultado_turno)
        print('Introduce una coordenada para intentar destruir un barco (por ejemplo: B3)')
        print('O introduce \'G\' para guardar la partida.')
        jugada = input()
        resultado_turno = turno(jugada)



def nueva_partida():
    difficulties = {
        '1': ('Fácil', 60),
        '2': ('Difícil', 35)
    }
    print('Elige una dificultad:')
    choice = get_option_from_list(difficulties)
    chosen_difficulty = difficulties[choice][1]
    new_game = game.BattleshipGame(chosen_difficulty)
    ejecutar_partida(new_game)


def cargar_partida():
    try:
        with open('battleship.pickle','rb') as f:
            loaded_game = pickle.load(f)
    except:
        print('No se ha podido cargar la partida.')
        return
    ejecutar_partida(loaded_game)

opciones = {
    '1':('Nueva partida',nueva_partida),
    '0':('Salir',exit)
}

def hay_partida_anterior():
    try:
        with open('battleship.pickle','rb') as f:
            return pickle.load(f)
    except:
        return False

def menu():
    while True:
        if hay_partida_anterior():
            opciones['2'] = ('Cargar partida',cargar_partida)
        elif opciones.get('2'):
            opciones.pop('2')
        for i,v in opciones.items():
            print(f'{i}. {v[0]}')
        eleccion = input()
        if eleccion in opciones.keys():
            return eleccion
        print('Opción inválida. Por favor elige una opción de la lista.')

def main():
    while True:
        eleccion = menu()
        opciones[eleccion][1]()

if __name__ == '__main__':
    main()