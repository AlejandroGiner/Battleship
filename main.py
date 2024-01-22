import battleship, utils
import pickle
import re

def turno(jugada, game: battleship.Game):
    if jugada == 'G':
        utils.guardar_partida(game)
        return 'Partida guardada.'
    elif jugada_regex := re.fullmatch(r'([A-J])([0-9]+)',jugada):
        row, col = jugada_regex.group(1,2)
        try:
            result = game.hit(row, col)
        except battleship.AlreadyDiscoveredError:
            return 'Ya has elegido esta casilla anteriormente.'
        except battleship.GameOverError:
            return 'La partida ha terminado.'
        except IndexError:
            return 'Esa casilla no existe.'


        ret = f'Elegida casilla {row}{col}. '
        if result > 0:
            ret += '¡Tocado!'
        elif result == 0:
            ret += '¡Tocado y hundido!'
        else:
            ret += 'No has tocado...'

        return ret


def ejecutar_partida(current_game: battleship.Game):
    resultado_turno = ''
    while True:
        utils.cls()
        print(current_game.get_board())
        print(f'Turno {current_game.current_turn} de {current_game.max_turns}')
        print(f'Barcos hundidos: {current_game.sunk_boats()}')
        print(resultado_turno)

        if current_game.won():
            print('¡Has ganado!')
            break
        elif current_game.current_turn <= current_game.max_turns:
            print('Introduce una coordenada para intentar destruir un barco (por ejemplo: B3)')
            print('O introduce \'G\' para guardar la partida.')
            jugada = input()
            resultado_turno = turno(jugada, current_game)
        else:
            print('Número máximo de turnos alcanzado. Has perdido.')
            break

def nueva_partida():
    difficulties = {
        '1': ('Fácil', 60),
        '2': ('Difícil', 35)
    }
    print('Elige una dificultad:')
    choice = utils.get_option_from_list(difficulties)
    chosen_difficulty = difficulties[choice][1]
    new_game = battleship.Game(chosen_difficulty)
    ejecutar_partida(new_game)

def continuar_partida():
    loaded_game = utils.cargar_partida()
    if loaded_game:
        ejecutar_partida(loaded_game)
    else:
        print('Error al cargar la partida.')

opciones = {
    '1':('Nueva partida',nueva_partida),
    '0':('Salir',exit)
}

def hay_partida_anterior():
    return utils.cargar_partida() is not None

def menu():
    while True:
        # If a saved game is detected, show the menu option to load it
        if hay_partida_anterior():
            opciones['2'] = ('Cargar partida',continuar_partida)
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