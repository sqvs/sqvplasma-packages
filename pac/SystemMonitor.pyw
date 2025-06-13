import psutil

def handle_command(command, args):
    if command == "cpu":
        return get_cpu_info()
    elif command == "memory":
        return get_memory_info()
    elif command == "processes":
        return get_processes()
    return None

def get_help():
    return (
        "  cpu - Информация о процессоре\n"
        "  memory - Информация о памяти\n"
        "  processes - Список процессов"
    )

def get_cpu_info():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=False)
        cpu_logical = psutil.cpu_count(logical=True)
        return (
            f"Физические ядра: {cpu_count}\n"
            f"Логические ядра: {cpu_logical}\n"
            f"Загрузка CPU: {cpu_percent}%"
        )
    except Exception as e:
        return f"Ошибка получения информации о CPU: {e}"

def get_memory_info():
    try:
        mem = psutil.virtual_memory()
        return (
            f"Всего памяти: {mem.total // (1024**2)} MB\n"
            f"Доступно: {mem.available // (1024**2)} MB\n"
            f"Использовано: {mem.used // (1024**2)} MB\n"
            f"Процент использования: {mem.percent}%"
        )
    except Exception as e:
        return f"Ошибка получения информации о памяти: {e}"

def get_processes():
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            processes.append(f"{proc.info['pid']}: {proc.info['name']}")
            
        return "\n".join(processes[:20]) + "\n... (полный список в файле processes.txt)"
    except Exception as e:
        return f"Ошибка получения списка процессов: {e}"