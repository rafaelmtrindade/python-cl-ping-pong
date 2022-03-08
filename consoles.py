import os
import sys
from time import sleep
try:
    from ctypes import Structure, windll, c_short, c_ushort, c_byte, c_int, byref
except ImportError:
    windll = None
try:
    import tty
    import termios
    import re
except ImportError:
    tty = termios = None


class ConsoleNavigator:
    def __init__(self, clean_start: bool = False):
        self.NAVIGATOR = _NavigatorDOS() if windll else _NavigatorANSI()
        if clean_start:
            self.clear_console()
        # self.is_nav_dos = isinstance(self.NAVIGATOR, _NavigatorDOS)

        self.init_pos = self.NAVIGATOR.get_cursor_pos()
        self.init_row = self.init_pos.get('row')
        self.init_col = self.init_pos.get('col')
        self.init_size = self.get_window_size()

    def clear_console(self):
        self.NAVIGATOR.clear_console()

    def get_window_size(self):
        size = os.get_terminal_size()
        return (size.lines, size.columns)

    def reset_window_size(self):
        self.NAVIGATOR.resize_window(*self.init_size)

    def resize_window(self, lines: int = 0, cols: int = 0):
        if not (lines and cols):
            size = self.get_window_size()
            if not lines:
                lines = size[0]
            if not cols:
                cols = size[1]
        self.NAVIGATOR.resize_window(lines, cols)

    def show_cursor(self):
        self.NAVIGATOR.toggle_cursor(True)

    def hide_cursor(self):
        self.NAVIGATOR.toggle_cursor(False)

    def get_cursor_pos(self):
        return self.NAVIGATOR.get_cursor_pos()

    def move_cursor_to_init_pos(self):
        '''
        Move o cursor para a posição em que estava quando foi
        instanciado o Navigator.
        '''
        self.NAVIGATOR.move_cursor_to(self.init_row, self.init_col)

    def move_cursor_by(self, row: int, col: int = 0):
        '''
        Posiciona o cursor relativamente a sua posição atual,
        de acordo com a quantia de linhas e colunas especificadas.

        row - quantidade de linhas a mover para cima (negativo) ou para baixo (positivo)
        '''
        self.NAVIGATOR.move_cursor_by(row, col)

    def move_cursor_to(self, row: int, col: int = 0):
        self.NAVIGATOR.move_cursor_to(row, col)


class _NavigatorANSI():
    def clear_console(self):
        os.system('clear')

    def resize_window(self, lines: int, cols: int):
        sys.stdout.write(f'\033[8;{lines};{cols}t')

    def toggle_cursor(self, on: bool):
        sys.stdout.write(f'\033[?25{"h" if on else "l"}')

    def get_cursor_pos(self) -> dict:
        stdin = sys.stdin.fileno()
        tattr = termios.tcgetattr(stdin)
        try:
            tty.setcbreak(stdin, termios.TCSANOW)

            sys.stdout.write('\x1b[6n\r')
            buffer = ''
            while True:
                buffer += sys.stdin.read(1)
                if buffer[-1] in ('R', '\n') or not buffer:
                    break
            pos_data = re.search(r'\x1b\[(\d*);(\d*)R', buffer)
            return {
                'row': int(pos_data.group(1)),
                'col': int(pos_data.group(2))
            }
        except KeyboardInterrupt:
            pass
        except:
            raise ValueError('Não foi possível ler a posição do cursor.')
        finally:
            termios.tcsetattr(stdin, termios.TCSANOW, tattr)

    def move_cursor_to(self, row: int, col: int = 0):
        print(f'\x1b[{row};{col}H', end='')

    def move_cursor_by(self, row: int, col: int):
        curr_pos = self.get_cursor_pos()
        curr_row = curr_pos.get('row')
        curr_col = curr_pos.get('col')
        self.move_cursor_to(curr_row+row, curr_col+col)


class _NavigatorDOS():
    _STDOUT_HANDLE = -11  # windows stdout handler

    def clear_console(self):
        os.system('cls')

    def resize_window(self, lines: int, cols: int):
        os.system(f'mode {cols},{lines}')

    def toggle_cursor(self, on: bool):
        ci = _CURSOR_INFO()
        # handle = windll.kernel32.GetStdHandle(self._STDOUT_HANDLE)
        successful = windll.kernel32.GetConsoleCursorInfo(
            self._STDOUT_HANDLE, byref(ci))
        if not successful:
            raise RuntimeError('Não foi possível obter dados do cursor.')
        ci.visible = on
        successful = windll.kernel32.SetConsoleCursorInfo(
            self._STDOUT_HANDLE, byref(ci))
        if not successful:
            raise RuntimeError('Não foi possível modificar o cursor.')

    def _get_cursor_coord(self) -> "_COORD":
        csbi = _CONSOLE_SCREEN_BUFFER_INFO()
        # handle = windll.kernel32.GetStdHandle(self._STDOUT_HANDLE)
        successful = windll.kernel32.GetConsoleScreenBufferInfo(
            self._STDOUT_HANDLE, byref(csbi))
        if not successful:
            raise ValueError('Não foi possível ler a posição do cursor.')
        return csbi.dwCursorPosition

    def get_cursor_pos(self):
        coord = self._get_cursor_coord()
        return {
            'col': coord.X,
            'row': coord.Y
        }

    def move_cursor_to(self, row: int, col: int):
        # handle = windll.kernel32.GetStdHandle(self._STDOUT_HANDLE)
        windll.kernel32.SetConsoleCursorPosition(
            self._STDOUT_HANDLE, _COORD(col, row))

    def move_cursor_by(self, row: int, col: int):
        curr_coord = self._get_cursor_coord()
        curr_col = curr_coord.X
        curr_row = curr_coord.Y
        self.move_cursor_to(curr_row+row, curr_col+col)


if windll:
    class _COORD (Structure):
        _fields_ = [
            ('X', c_short),
            ('Y', c_short)
        ]

    class _SMALL_RECT(Structure):
        _fields_ = [
            ('Left', c_short),
            ('Top', c_short),
            ('Right', c_short),
            ('Bottom', c_short)
        ]

    class _CONSOLE_SCREEN_BUFFER_INFO(Structure):
        _fields_ = [
            ('dwSize', _COORD),
            ('dwCursorPosition', _COORD),
            ('wAttributes', c_ushort),
            ('srWindow', _SMALL_RECT),
            ('dwMaximumWindowSize', _COORD)
        ]

    class _CURSOR_INFO(Structure):
        _fields_ = [
            ('size', c_int),
            ('visible', c_byte)
        ]


if __name__ == '__main__':
    NAVIGATOR = ConsoleNavigator()
    # pos = NAVIGATOR.get_cursor_pos_after_init()

    # for k, v in pos.items():
    #     print(f'{k}: {v}')
    # pass

    # try:
    #     NAVIGATOR.hide_cursor()
    #     NAVIGATOR.resize_window(30)
    #     print('I\'m here...')
    #     sleep(5)
    # finally:
    #     NAVIGATOR.show_cursor()

    print(os.name)
