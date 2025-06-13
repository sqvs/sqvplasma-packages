import base64
import json
import os

def handle_command(command, args):
    if command == "pyexec":
        return exec_python_code(' '.join(args))
    elif command == "base64":
        return base64_encode(' '.join(args))
    elif command == "json":
        return format_json(args[0] if args else "")
    return None

def get_help():
    return (
        "  pyexec <код> - Выполнить Python код\n"
        "  base64 <текст> - Кодирование/декодирование Base64\n"
        "  json <файл> - Форматирование JSON"
    )

def exec_python_code(code):
    try:
        if not code:
            return "Укажите код: pyexec <код>"
            
        # Создаем локальный контекст для выполнения кода
        local_vars = {}
        
        # Выполняем код
        exec(code, globals(), local_vars)
        
        # Возвращаем результат, если он есть
        if '_' in local_vars:
            return str(local_vars['_'])
        return "Код выполнен"
    except Exception as e:
        return f"Ошибка выполнения кода: {e}"

def base64_encode(text):
    try:
        if not text:
            return "Укажите текст: base64 <текст>"
            
        # Если текст похож на base64, декодируем
        if text.endswith('=') and len(text) % 4 == 0:
            try:
                decoded = base64.b64decode(text).decode('utf-8')
                return f"Декодировано: {decoded}"
            except:
                pass
                
        # Иначе кодируем
        encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return f"Закодировано: {encoded}"
    except Exception as e:
        return f"Ошибка обработки: {e}"

def format_json(filename):
    try:
        if not filename:
            return "Укажите файл: json <имя_файла>"
            
        if not os.path.exists(filename):
            return f"Файл не существует: {filename}"
            
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return json.dumps(data, indent=2, ensure_ascii=False)
    except Exception as e:
        return f"Ошибка обработки JSON: {e}"