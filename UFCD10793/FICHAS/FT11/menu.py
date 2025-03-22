import curses
import time

def main(stdscr):
    # Configuração inicial
    curses.curs_set(0)  # Esconde o cursor
    stdscr.clear()

    # Cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    # Opções do menu
    menu = ["1. Novo Jogo", "2. Carregar Jogo", "3. Opções", "4. Pontuações", "5. Sair"]
    current_row = 0

    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        # Desenha o título
        title = "MENU PRINCIPAL"
        stdscr.addstr(h//2 - len(menu)//2 - 2, w//2 - len(title)//2, title, curses.color_pair(1))

        # Desenha as opções do menu
        for idx, item in enumerate(menu):
            x = w//2 - len(item)//2
            y = h//2 - len(menu)//2 + idx

            if idx == current_row:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, item)
                stdscr.attroff(curses.color_pair(2))
            else:
                stdscr.addstr(y, x, item, curses.color_pair(1))

        # Atualiza a tela
        stdscr.refresh()

        # Captura tecla
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # Mostra a opção selecionada
            stdscr.clear()
            stdscr.addstr(h//2, w//2 - 10, f"Selecionado: {menu[current_row]}")
            stdscr.refresh()
            time.sleep(1)

            if current_row == len(menu)-1:  # Se selecionou "Sair"
                break

if __name__ == '__main__':
    curses.wrapper(main)