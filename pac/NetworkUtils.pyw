import platform
import subprocess
import psutil
import requests

def handle_command(command, args):
    if command == "ping":
        return ping_host(args[0] if args else "google.com")
    elif command == "ipinfo":
        return get_ip_info()
    elif command == "download":
        return download_file(args[0] if args else "")
    return None

def get_help():
    return (
        "  ping <хост> - Проверка доступности хоста\n"
        "  ipinfo - Сетевые интерфейсы\n"
        "  download <url> - Скачивание файла"
    )

def ping_host(host):
    try:
        param = '-n' if platform.system().lower() == 'windows' else '-c'
        command = ['ping', param, '4', host]
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        return f"Ошибка ping: {e}"

def get_ip_info():
    try:
        interfaces = psutil.net_if_addrs()
        result = []
        for name, addrs in interfaces.items():
            result.append(f"Интерфейс: {name}")
            for addr in addrs:
                result.append(f"  {addr.family.name}: {addr.address}")
        return "\n".join(result)
    except Exception as e:
        return f"Ошибка получения информации: {e}"

def download_file(url):
    try:
        if not url:
            return "Укажите URL: download <url>"
            
        filename = url.split('/')[-1]
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        return f"Файл скачан: {filename}"
    except Exception as e:
        return f"Ошибка скачивания: {e}"