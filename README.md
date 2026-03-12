# 🌐 Diagnóstico de Rede

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status: Ativo](https://img.shields.io/badge/status-ativo-brightgreen.svg)](#)
[![Tests](https://github.com/sbagzz/diagnostico_de_redes/workflows/Python%20Tests/badge.svg)](https://github.com/sbagzz/diagnostico_de_redes/actions)

Ferramenta interativa e robusta para diagnóstico completo de conectividade de rede, desenvolvida em Python com interface colorida via terminal.

---

## 📋 Sumário

- [✨ Funcionalidades](#-funcionalidades)
- [🚀 Quick Start](#-quick-start)
- [📦 Requisitos](#-requisitos)
- [📁 Estrutura](#-estrutura-do-projeto)
- [💻 Módulos](#-módulos)
- [📊 Exemplo de Saída](#-exemplo-de-saída)
- [🔧 Troubleshooting](#-troubleshooting)
- [🎯 Conceitos Praticados](#-conceitos-praticados)
- [💡 Melhorias Futuras](#-melhorias-futuras)


---
# ✨ Funcionalidades

✅ **Teste de Conexão** - Verifica conectividade com 8.8.8.8 (Google DNS) e mede latência

✅ **IP Local** - Exibe o endereço IP da máquina  

✅ **Teste de DNS** - Valida resolução de nomes (domínio google.com)  

✅ **Usuário do Sistema** - Mostra o nome do usuário conectado

✅ **OS**-  Mostra informações do sistema operacional    

✅ **Diagnóstico Completo** - Executa todos os testes simultaneamente  

✅ **Interface Colorida** - Menu formatado com Rich para melhor visualização  

✅ **Log Automático** - Registra todas as operações em `diagnostico.log`  

✅ **Cross-platform** - Funciona em Windows, Linux e macOS

---

## 🚀 Quick Start

### 1️⃣ Clonar o Repositório

**HTTPS:**
```bash
git clone https://github.com/sbagzz/diagnostico_de_redes.git
cd diagnostico-de-redes
```

**SSH:**
```bash
git clone git@github.com:sbagzz/diagnostico_de_redes.git
cd diagnostico_de_redes
```

### 2️⃣ Pré-requisitos
```bash
# Verifique se Python 3.10+ está instalado
python --version
```

### 3️⃣ Ativar Ambiente Virtual

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 4️⃣ Instalar Dependências
```bash
 pip install -e .
```

### 5️⃣ Executar
```bash
python main.py
```

---

## 📦 Requisitos

| Pacote | Versão | Descrição |
|--------|--------|-----------|
| `ping3` | 5.1.5 | Teste de ping (ICMP) |
| `dnspython` | 2.6.1 | Resolução de DNS |
| `psutil` | 7.2.2 | Informações do sistema |
| `rich` | 14.3.3 | Formatação de saída |
| `Pygments` | 2.19.2 | Realce de sintaxe |

**Compatibilidade:** Python 3.10+  
**Acesso de Rede:** Requerido para testes de conectividade

---

## 📁 Estrutura do Projeto

```
diagnóstico de redes/
│
├── main.py              # Aplicação principal (menu, interface)
├── rede.py              # Funções de teste de rede
├── sistema.py           # Coleta de informações do sistema
├── logger.py            # Sistema de logging
├── pyproject.toml       # Dependências Python
├── diagnostico.log      # Arquivo de log (gerado automaticamente)
└── README.md            # Esta documentação
```

---

## 💻 Módulos

### `main.py`
**Responsabilidades:**
- 🎯 Exibir menu principal
- 📥 Receber entrada do usuário
- 🔄 Coordenar fluxo de execução
- 📊 Formatar e exibir resultados
- 💾 Registrar eventos em log

**Funções principais:**
- `menu()` - Exibe opções disponíveis
- `limpar_tela()` - Limpeza cross-platform
- `status_color()` - Formatação de status
- `diagnostico_completo()` - Executa todos os testes
- `main()` - Loop principal

### `rede.py`
**Responsabilidades:**
- 🌐 Testes de conectividade
- 🔍 Verificação de DNS
- ⏱️ Medição de latência

**Funções:**
- `teste_conexao()` → `(bool, str)` - Status e latência
- `teste_dns()` → `bool` - Resultado do teste de DNS

### `sistema.py`
**Responsabilidades:**
- 👤 Informações do usuário
- 🖥️ Endereço IP da máquina
- 🖥️ Sistema operacional da máquina

**Funções:**
- `usuario_conectado()` → `str` - Nome do usuário
- `mostrar_ip()` → `str` - IP local
- `OS()` → `str` - OS da máquina


### `logger.py`
**Responsabilidades:**
- 📝 Registro de eventos
- 💾 Persistência em arquivo

**Funções:**
- `salvar_log(mensagem)` - Registra evento em `diagnostico.log`

---

## 📊 Exemplo de Saída

### Menu Principal
```
===================================
     Diagnóstico de Rede
===================================
1 - Testar conexão
2 - Identificar IP local
3 - Testar DNS
4 - Usuário conectado
5 - OS 
6 - Diagnóstico Completo
0 - Sair
===================================

► Escolha uma opção:
```

### Diagnóstico Completo (Opção 6)
```
╭─────────────────────────────────────────────────╮
│ Diagnóstico de Rede                              │
├──────────────┬────────────────┬──────────────────┤
│ Item         │ Status         │ Detalhe          │
├──────────────┼────────────────┼──────────────────┤
│ Internet     │ ✓ OK           │ 15.23 ms         │
│ IP Local     │ INFO           │ 192.168.1.100    │
│ DNS          │ ✓ OK           │ Resolução OK     │
│ Sistema      │ INFO           │ Linux            │
╰──────────────┴────────────────┴──────────────────╯
```

### Arquivo de Log
```
2026-02-28 20:01:56,231 - Aplicação iniciada
2026-02-28 20:01:56,588 - Diagnóstico completo iniciado
2026-02-28 20:01:57,123 - Teste de conexão iniciado
2026-02-28 20:01:57,456 - Teste de DNS iniciado
2026-02-28 20:01:57,456 - Detecção de SO iniciada
2026-02-28 20:01:57,698 - Diagnóstico completo finalizado
2026-02-28 20:01:57,739 - Aplicação encerrada normalmente
```

---

## 🔧 Troubleshooting

### ❌ Erro: `ModuleNotFoundError: No module named 'ping3'`
```bash
# Reinstale as dependências
pip install --upgrade -e .
```

### ❌ Erro: "Permission denied" ao testar ping
**Windows:**
- Abra o PowerShell como **Administrador**

**Linux/macOS:**
- Execute com privilégios: `sudo python main.py`
- Ou configure permissões ICMP

### ❌ Erro: "Arquivo de log inacessível"
```bash
# Verifique permissões de escrita
ls -l diagnostico.log  # Linux/macOS
dir /AD diagnostico.log  # Windows
```

### ❌ Erro: Limpeza de tela não funciona
- A aplicação detecta automaticamente o SO
- Se falhar, usa fallback ANSI

### ⚠️ Teste de DNS sempre falha
- Verifique sua conexão com a internet
- Teste manualmente: `nslookup google.com`

---

## 🎯 Conceitos Praticados

✔️ **Modularização** - Código organizado em módulos especializados  
✔️ **Tratamento de Erros** - Try/except robustos em funções críticas  
✔️ **Type Hints** - Anotações de tipo em funções  
✔️ **Logging** - Registro persistente de eventos  
✔️ **APIs de Sistema** - Socket, psutil, subprocess  
✔️ **Programação Cross-platform** - Compatibilidade Windows/Unix  
✔️ **Interfaces CLI** - Menu interativo com Rich  
✔️ **Boas Práticas** - Docstrings, guardião `if __name__`, conventions PEP 8  

---

## 💡 Melhorias Futuras

- [ ] Exportar diagnóstico para JSON/CSV
- [ ] Interface gráfica com tkinter
- [ ] Teste de velocidade de download/upload
- [ ] Verificação de portas abertas
- [ ] Histórico de diagnósticos
- [ ] Alertas para falhas recorrentes
- [ ] Sincronização com servidor remoto
- [ ] Comparação com execuções anteriores


## 🤝 Contribuições

Sugestões e pull requests são bem-vindos!  
Para contribuir, leia [CONTRIBUTING.md](CONTRIBUTING.md) e abra uma issue descrevendo sua melhoria.

---

## 👨‍💻 Autor

**Gabriel Noronha**  
- 📧 Email: gnoronha409@gmail.com
- 🔗 GitHub: [@sbagzz](https://github.com/sbagzz)

Estudante de desenvolvimento Python e segurança.

---

**Versão:** 2.1 
**Última atualização:** 12 de março de 2026  
**Desenvolvido em:** Python 3.10+
