import psutil as ps
import socket


def usuario_conectado():
    """Retorna o nome do usuário conectado.
    Retorna: str - nome do usuário ou 'Desconhecido' se falhar.
    """
    try:
        usuarios = ps.users()
        if usuarios:
            return usuarios[0].name
        return "Desconhecido"
    except Exception:
        return "Desconhecido"


def mostrar_ip():
    """Retorna o IP local da máquina.
    Retorna: str - endereço IP ou 'Desconhecido' se falhar.
    """
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        return ip
    except Exception:
        return "Desconhecido"


