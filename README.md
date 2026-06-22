Abaixo você pode visualizar o conteúdo completo em formato de texto para copiar e colar diretamente no seu repositório se preferir:

```markdown
# 🛒 Terminal Shopping List CRUD

Este projeto é uma aplicação de linha de comando (CLI) desenvolvida em **Python** que funciona como um sistema completo de **CRUD** (Create, Read, Update, Delete) para gerenciamento de uma lista de compras. 

O foco principal deste script é puramente **educacional**, demonstrando conceitos lógicos de validação de dados, tratamento de exceções em tempo de execução e manipulação de fluxos de repetição e condicionais.

---

## 💡 Características do Projeto

* **CRUD Completo via Terminal:** Permite adicionar, visualizar, editar e remover itens interativamente.
* **Armazenamento Dinâmico em Memória:** Utiliza o conceito de **listas paralelas** (`ls_lista_compras`, `ls_quantidades`, `lf_lista_valores`) sincronizadas através de índices correspondentes.
* **Sem Persistência de Dados:** Por se tratar de um exercício de lógica pura, o projeto **não** salva os dados em bancos de dados (SQL/NoSQL) ou arquivos locais (como `.txt` ou `.json`). Todas as informações são limpas ao encerrar a aplicação.
* **Validação de Entradas Robusta:**
  * Proteção contra quebras por tipos de dados inválidos (ex: digitar letras em campos de números) usando blocos `try/except ValueError`.
  * Validação de regras de negócio básicas (impedindo a adição ou atualização com quantidades e valores menores ou iguais a zero).
  * Tratamento de strings com `.lower().strip()` para mitigar erros induzidos por espaços em branco ou letras maiúsculas na busca de itens.
  * Proteção do estado dos dados no fluxo de edição (as listas só são alteradas se todas as entradas do usuário passarem com sucesso na validação).

---

## 🛠️ Funcionalidades

1. **Adicionar Item (Create):** Recebe o nome do produto, quantidade de unidades e o valor unitário.
2. **Editar Item (Update):** Permite alterar o nome, quantidade e preço de um item existente de maneira segura.
3. **Remover Item (Delete):** Remove o produto selecionado e reajusta as estruturas de memória.
4. **Visualizar Lista (Read):** Exibe de forma formatada todos os itens cadastrados, suas respectivas quantidades e o subtotal por produto.
5. **Calcular Valor Total (Read/Aggregate):** Percorre toda a estrutura para retornar o valor acumulado final da lista formatado em moeda (R$).
6. **Fechar a Lista:** Encerra a execução do loop principal da aplicação.

---

## 🔧 Como Executar

### Pré-requisitos
* Ter o **Python 3.10+** instalado em sua máquina.

### Passo a Passo
1. Clone este repositório ou baixe o arquivo `ShoppingList.py`.
2. Abra o terminal na pasta onde o arquivo está localizado.
3. Execute o script com o seguinte comando:
```bash
python ShoppingList.py