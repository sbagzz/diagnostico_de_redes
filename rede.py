"""Módulo de testes de rede.

Contém funções para verificar conexão com internet e resolução de DNS.
"""

from ping3 import ping
from dns.resolver import resolve


def teste_conexao():
    """Testa conexão com 8.8.8.8 (Google DNS) e mede latência.
    
    Returns:
        tuple: (bool, str) - (status, latência_ou_erro)
    """
    try:
        resposta = ping("8.8.8.8", timeout=4)
        if resposta:
            ms = round(resposta * 1000, 2)
            return True, f"{ms} ms"
        return False, "Sem resposta"
    except Exception as e:
        return False, f"Erro: {str(e)}"


def teste_dns():
    """Testa resolução DNS com google.com.
    
    Returns:
        bool: True se DNS funciona, False caso contrário.
    """
    try:
        resolve("google.com", "A")
        return True
    except Exception:
        return False
    


        