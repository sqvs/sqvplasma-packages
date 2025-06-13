import os
import glob

def handle_command(command, args):
    if command == "ls":
        return list_files(args[0] if args else "")
    elif command == "cat":
        return cat_file(args[0] if args else "")
    elif command == "find":
        return find_files(args[0] if args else "*")
    elif command == "mkdir":
        return make_dir(args[0] if args else "")
    return None

def get_help():
    return (
        "  ls [путь] - Список файлов\n"
        "  cat <файл> - Вывод содержимого файла\n"
        "  find <шаблон> - Поиск файлов\n"
        "  mkdir <директория> - Создание директории"
    )

def list_files(path):
    try:
        target_path = path if path else os.getcwd()
        if not os.path.exists(target_path):
            return f"Директория не существует: {target_path}"
            
        items = os.listdir(target_path)
        result = []
        for item in items:
            full_path = os.path.join(target_path, item)
            if os.path.isdir(full_path):
                result.append(f"[DIR]  {item}")
            else:
                size = os.path.getsize(full_path)
                result.append(f"[FILE] {item} ({size} bytes)")
                
        return "\n".join(result)
    except Exception as e:
        return f"Ошибка: {e}"

def cat_file(filename):
    try:
        if not filename:
            return "Укажите имя файла: cat <имя_файла>"
            
        if not os.path.exists(filename):
            return f"Файл не существует: {filename}"
            
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Ошибка чтения файла: {e}"

def find_files(pattern):
    try:
        files = glob.glob(pattern)
        if not files:
            return "Файлы не найдены"
        return "\n".join(files)
    except Exception as e:
        return f"Ошибка поиска: {e}"

def make_dir(dirname):
    try:
        if not dirname:
            return "Укажите имя директории: mkdir <имя>"
            
        os.makedirs(dirname, exist_ok=True)
        return f"Директория создана: {dirname}"
    except Exception as e:
        return f"Ошибка создания директории: {e}"