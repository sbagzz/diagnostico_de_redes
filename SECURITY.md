# Política de Segurança

## Versões Suportadas

As seguintes versões do Python são suportadas:

| Versão | Suportado          |
| ------ | ------------------ |
| 3.11   | ✅ Sim             |
| 3.10   | ✅ Sim             |
| 3.9    | ✅ Sim             |
| 3.8    | ✅ Sim             |
| 3.7    | ✅ Sim             |
| 3.6    | ✅ Sim             |
| < 3.6  | ❌ Não             |

## Reportando Vulnerabilidades de Segurança

**Não** abra issues públicas para vulnerabilidades de segurança.

Se você descobrir uma vulnerabilidade de segurança, por favor envie um email para `seu-email@exemplo.com` com:

1. **Descrição da vulnerabilidade**
2. **Versões afetadas**
3. **Como reproduzir** (se possível)
4. **Impacto potencial**
5. **Sugestões de correção** (se houver)

Tentaremos responder em até 48 horas e trabalharemos com você para resolver o problema de forma responsável.

## Dependências Seguras

Este projeto usa as seguintes dependências:

- `ping3` - Teste de ping
- `dnspython` - Resolução de DNS
- `psutil` - Informações do sistema
- `rich` - Formatação de terminal
- `Pygments` - Realce de sintaxe

Todas as dependências são verificadas regularmente para atualizações de segurança.

## Boas Práticas de Segurança

Ao usar esta ferramenta:

- ✅ Mantenha Python atualizado
- ✅ Atualize regularmente as dependências: `pip install --upgrade -r requirements.txt`
- ✅ Não use credenciais em logs ou variáveis de ambiente
- ✅ Revise os logs em `diagnostico.log` regularmente
- ✅ Use em redes confiáveis

## Conformidade

Este projeto adere às seguintes práticas de segurança:

- 🔒 Type hints para melhor análise de código
- 🔒 Tratamento robusto de exceções
- 🔒 Validação de entrada
- 🔒 Princípio do menor privilégio
- 🔒 Sem armazenamento de dados sensíveis

---

**Obrigado por manter nosso projeto seguro!**
