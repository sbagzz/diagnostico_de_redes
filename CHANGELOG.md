# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/).

---

## [Unreleased]

### A Adicionar
- [ ] Exportar diagnóstico para JSON/CSV
- [ ] Interface gráfica com tkinter
- [ ] Teste de velocidade de download/upload
- [ ] Verificação de portas abertas
- [ ] Histórico de diagnósticos
- [ ] Alertas para falhas recorrentes

### Mudanças Planejadas
- Melhorar documentação
- Adicionar testes unitários com pytest
- Otimizar performance de testes

---

## [2.0] - 2026-02-28

### Adicionado
- ✨ Interface colorida com Rich
- ✨ Suporte cross-platform (Windows/Linux/macOS)
- ✨ Limpeza de tela automática
- ✨ Tratamento robusto de exceções
- ✨ Sistema de logs persistente
- ✨ Docstrings em todas as funções
- ✨ Type hints para melhor clareza
- 📝 README.md completo com exemplos
- 📝 CONTRIBUTING.md para contribuições
- 🔄 GitHub Actions workflow para CI/CD

### Corrigido
- 🐛 Retornos inconsistentes em `teste_conexao()` e `teste_dns()`
- 🐛 Indentação irregular em `sistema.py`
- 🐛 Captura de `KeyboardInterrupt` (Ctrl+C)
- 🐛 Timeout configurável em testes de ping

### Melhorado
- 📊 Tabela de diagnóstico com formatação Rich
- 🎨 Menu principal mais intuitivo
- ⚙️ Configuração de timeout em testes
- 📝 Mensagens de erro mais descritivas

---

## [1.0] - 2026-01-15

### Adicionado
- 🎯 Versão inicial funcional
- 🌐 Teste de conexão com ping
- 🔍 Teste de DNS
- 👤 Exibição do IP local
- 👤 Exibição do usuário conectado
- 💾 Sistema básico de logging

### Features
- Menu interativo no terminal
- Diagnóstico completo em tabela
- Registro de eventos em arquivo de log

---

## Guia de Versionamento

Usamos [Semantic Versioning](https://semver.org/lang/pt-BR/):
- **MAJOR** (1.0.0) - Mudanças incompatíveis
- **MINOR** (1.1.0) - Novas features compatíveis
- **PATCH** (1.0.1) - Correções de bugs

---

**[Unreleased]:** Mudanças que ainda não foram lançadas  
**[2.0]:** Versão atual  
**[1.0]:** Primeira versão estável
