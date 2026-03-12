# 🤝 Guia de Contribuição

Obrigado pelo interesse em contribuir para o **Diagnóstico de Rede**! Aqui estão as diretrizes para contribuir.

---

## 📋 Como Contribuir

### 1. Fork o Repositório
Clique no botão **"Fork"** no topo da página.

### 2. Clone seu Fork
```bash
git clone https://github.com/sbagzz/diagnostico_de_redes.git
cd diagnóstico-de-redes
```

### 3. Crie uma Branch
```bash
git checkout -b feature/sua-funcionalidade
# ou para correções:
git checkout -b fix/sua-correcao
```

### 4. Faça suas Mudanças
- Edite os arquivos necessários
- Mantenha o código limpo e bem documentado
- Siga a convenção PEP 8

### 5. Commit
```bash
git add .
git commit -m "Descrição clara da mudança"
```

### 6. Push
```bash
git push origin feature/sua-funcionalidade
```

### 7. Crie um Pull Request
1. Vá em **Pull Requests** → **New Pull Request**
2. Selecione sua branch
3. Descreva suas mudanças
4. Clique em **Create Pull Request**

---

## 🎯 Tipos de Contribuição Bem-Vindos

- **Correções de bugs** - Encontrou um problema? Corrija-o!
- **Novas funcionalidades** - Ideias para melhorias? Implemente!
- **Documentação** - Melhorias no README ou comentários no código
- **Testes** - Adicione testes unitários para as funções
- **Otimizações** - Melhore a eficiência do código

---

## 📝 Padrões de Código

### Python (PEP 8)
```python
def funcao_exemplo(parametro: str) -> str:
    """Descrição breve da função.
    
    Args:
        parametro: Descrição do parâmetro
        
    Returns:
        str: Descrição do retorno
    """
    return f"Resultado: {parametro}"
```

### Commits
- Use mensagens descritivas em português ou inglês
- Exemplo: `feat: adiciona teste de velocidade`
- Ou: `fix: corrige erro no teste de DNS`
- Ou: `docs: melhora README`

---

## 🧪 Testando Antes de Fazer Push

```bash
# Ative o ambiente virtual
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate.bat  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python main.py

# Verifique se não há erros de sintaxe
python -m py_compile *.py
```

---

## 🐛 Reportando Bugs

Se encontrar um bug, abra uma **Issue** com:
1. **Título descritivo**
2. **Descrição detalhada** do problema
3. **Passos para reproduzir**
4. **Comportamento esperado** vs **comportamento atual**
5. **Seu ambiente** (SO, versão Python, etc)

---

## 💡 Sugestões de Funcionalidades

Quer sugerir uma nova funcionalidade? Abra uma **Issue** com:
1. **Título claro**
2. **Descrição detalhada**
3. **Casos de uso**
4. **Exemplo de como seria utilizado**

---

## 📌 Regras Importantes

✅ **Faça:**
- Manter código limpo e bem formatado
- Adicionar docstrings em funções novas
- Testar antes de fazer push
- Descrever bem seus commits

❌ **Evite:**
- Commits com muitos arquivos não relacionados
- Alterar `main` diretamente
- Remover funcionalidades existentes sem discussão
- Adicionar dependências sem justificativa

---

## 📞 Precisa de Ajuda?

- 📖 Abra uma **Discussion**
- 🐛 Reporte um **Issue**
- 💬 Entre em contato na descrição do repositório

---

**Obrigado por contribuir! 🙏**
