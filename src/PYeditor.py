import curses
import sys


def main(stdscr, filename):
    curses.curs_set(1)  # Show cursor

    text = ""
    y, x = 0, 0  # Cursor position

    if filename:
        try:
            with open(filename, "r") as file:
                text = file.read()
        except FileNotFoundError:
            pass  # File not found, start with an empty text

    while True:
        stdscr.clear()
        stdscr.addstr(text)

        # Move the cursor to the current position (y, x)
        stdscr.move(y, x)

        key = stdscr.getch()

        if key == 27:  # Escape key to exit
            save_and_exit(text, filename)
            break
        elif key == 10:  # Enter key
            text = insert_newline(text, y, x)
            y += 1
            x = 0
        elif key == curses.KEY_BACKSPACE:  # Backspace
            text, y, x = handle_backspace(text, y, x)
        elif key == curses.KEY_LEFT:  # Left arrow
            x = max(0, x - 1)
        elif key == curses.KEY_RIGHT:  # Right arrow
            x = min(len(text.split("\n")[y]), x + 1)
        elif key == curses.KEY_UP:  # Up arrow
            y = max(0, y - 1)
            x = min(x, len(text.split("\n")[y]))
        elif key == curses.KEY_DOWN:  # Down arrow
            lines = text.split("\n")
            y = min(len(lines) - 1, y + 1)
            x = min(x, len(lines[y]))
        elif key == 9:  # Tab key
            text, x = insert_tab(text, y, x)
        else:
            text = insert_char(text, y, x, chr(key))
            x += 1


def save_and_exit(text, filename):
    if filename:
        with open(filename, "w") as file:
            file.write(text)


def insert_newline(text, y, x):
    lines = text.split("\n")
    lines.insert(y + 1, lines[y][x:])
    lines[y] = lines[y][:x]
    return "\n".join(lines)


def handle_backspace(text, y, x):
    lines = text.split("\n")
    if x > 0:
        lines[y] = lines[y][: x - 1] + lines[y][x:]
        x -= 1
    elif y > 0:
        if lines[y] == "":
            del lines[y]
            y -= 1
            x = len(lines[y])
        else:
            lines[y - 1] += lines[y]
            del lines[y]
            y -= 1
            x = len(lines[y])
    return "\n".join(lines), y, x


def insert_char(text, y, x, char):
    lines = text.split("\n")
    lines[y] = lines[y][:x] + char + lines[y][x:]
    return "\n".join(lines)


def insert_tab(text, y, x):
    lines = text.split("\n")
    current_line = lines[y]
    before_cursor = current_line[:x]
    after_cursor = current_line[x:]
    spaces_to_insert = 7 - (len(before_cursor) % 7)
    tabs = " " * spaces_to_insert
    new_line = before_cursor + tabs + after_cursor
    lines[y] = new_line
    return "\n".join(lines), x + spaces_to_insert


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 editor.py <filename>")
    else:
        filename = sys.argv[1]
        curses.wrapper(main, filename)
