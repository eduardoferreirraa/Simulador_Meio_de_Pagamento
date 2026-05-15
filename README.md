# 💳 Simulador de Meio de Pagamento (SMM)

> Projeto desenvolvido para a disciplina de **Programação de Computadores** — UNICSUL 2026

---

## 📋 Sobre o projeto

O **SMM (Simulador de Meio de Pagamento)** é um programa de linha de comando desenvolvido em Python que simula o processamento de transações financeiras com diferentes meios de pagamento.

O sistema calcula automaticamente:
- A **taxa MDR** (Merchant Discount Rate) de cada transação
- O **valor líquido** que o lojista recebe
- A **data de crédito** com ajuste automático para dias úteis

---

## 🚀 Funcionalidades

| Opção | Meio de Pagamento | Taxa MDR | Prazo de Crédito |
|:---:|---|:---:|:---:|
| `0` | Cartão de Débito | 1% | D+1 |
| `1` | Cartão de Crédito à Vista | 5% | D+30 |
| `2` | Cartão de Crédito Parcelado (2x ou 3x) | 5% | D+30 / D+60 / D+90 |
| `9` | Sair | — | — |

### Regras de negócio implementadas

- ✅ Cálculo automático de MDR por tipo de pagamento
- ✅ Ajuste de data de crédito para o próximo dia útil (pula sábado e domingo)
- ✅ Parcelamento em 2 ou 3 vezes com distribuição correta de centavos
- ✅ Validação de entradas — rejeita valores inválidos e opções inexistentes
- ✅ Formatação de valores no padrão brasileiro (R$ 0,00)
- ✅ Exibição de data e hora da transação em tempo real

---

## 🖥️ Como executar

### Opção 1 — Compilador online (sem instalação)
Acesse [programiz.com/python-programming/online-compiler](https://www.programiz.com/python-programming/online-compiler/), cole o código e clique em **Run**.

### Opção 2 — Localmente
Certifique-se de ter o Python instalado:
```bash
python --version
```
Clone o repositório e execute:
```bash
git clone https://github.com/eduardoferreirraa/Simulador_de_Meio_de_Pagamento.git
cd Simulador_de_Meio_de_Pagamento
python smm.py
```

---

## 📺 Exemplo de uso

```
======================================================================
UNICSUL - Simulador de Meio de Pagamento – versão 2026  15/05/2026
Meio de pagamento disponível:
  0 – Cartão de Débito
  1 – Cartão de Crédito à Vista
  2 – Cartão de Crédito Parcelado
  9 – Sair

Escolha o meio de pagamento: 2
Valor da compra: R$ 300,00
Quantidade de parcelas (2 ou 3): 3

======================================================================
Data da compra         : 15/05/2026
Hora da compra         : 14:35
Meio de pagamento      : 2 – Cartão de Crédito Parcelado
Valor da compra        : R$ 300,00
Valor do MDR (taxa)    : R$ 15,00
Valor líquido total    : R$ 285,00

  Parcela              : 1/3
  Valor líquido        : R$ 95,00
  Data de crédito      : 15/06/2026

  Parcela              : 2/3
  Valor líquido        : R$ 95,00
  Data de crédito      : 14/07/2026

  Parcela              : 3/3
  Valor líquido        : R$ 95,00
  Data de crédito      : 13/08/2026
======================================================================
```

---

## 🧠 Conceitos aplicados

- **Pensamento computacional** — decomposição do problema em funções independentes
- **Lógica de negócios** — regras reais do mercado financeiro (MDR, prazos de crédito)
- **Manipulação de data e hora** — biblioteca `datetime` e `timedelta`
- **Validação de dados** — tratamento de entradas inválidas com `try/except`
- **Operações financeiras** — arredondamento correto de parcelas em centavos
- **Boas práticas** — código organizado, legível e comentado

---

## 📁 Arquivos do repositório

| Arquivo | Descrição |
|---|---|
| `smm.py` | Código principal do simulador |
| `smm_comentado.py` | Mesma versão com comentários explicativos em cada linha |

---

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Bibliotecas:**
- `datetime` — data e hora da transação
- `timedelta` — cálculo de prazos de crédito

---

## 👨‍💻 Autor

**Eduardo Ferreira**  
Estudante de Ciência da Computação — UNICSUL, São Paulo

[![GitHub](https://img.shields.io/badge/GitHub-eduardoferreirraa-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/eduardoferreirraa)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Eduardo%20Ferreira-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eduardoferreira)

---

## 📄 Contexto acadêmico

Projeto desenvolvido como **Entrega 1** da disciplina de Programação de Computadores (2026/1), com objetivo de aplicar conhecimentos de:
- Algoritmos matemáticos
- Pensamento computacional
- Uso de bibliotecas Python
- Projeto e validação de algoritmos
