def handle_command(command, args):
    if command == "theme":
        return set_theme(args[0] if args else "")
    elif command == "font":
        return set_font_size(args[0] if args else "")
    elif command == "color":
        return set_text_color(args[0] if args else "")
    return None

def get_help():
    return (
        "  theme <dark/light> - Смена темы интерфейса\n"
        "  font <размер> - Изменение размера шрифта\n"
        "  color <цвет> - Изменение цвета текста"
    )

def set_theme(theme):
    return f"Тема '{theme}' будет применена после выполнения команды"

def set_font_size(size):
    return f"Размер шрифта '{size}' будет применен после выполнения команды"

def set_text_color(color):
    return f"Цвет текста '{color}' будет применен после выполнения команды"