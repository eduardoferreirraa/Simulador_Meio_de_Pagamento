from datetime import datetime, timedelta

# ─────────────────────────────────────────────
# TAXAS
# ─────────────────────────────────────────────
MDR_DEBITO  = 0.01   # 1%
MDR_CREDITO = 0.05   # 5%

# ─────────────────────────────────────────────
# UTILITÁRIOS
# ─────────────────────────────────────────────

def proximo_dia_util(data: datetime) -> datetime:
    """Avança a data enquanto for sábado (5) ou domingo (6)."""
    while data.weekday() in (5, 6):
        data += timedelta(days=1)
    return data


def formatar_valor(v: float) -> str:
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cabecalho(data_hora: datetime) -> str:
    linha = "=" * 70
    titulo = f"Simulador de Meio de Pagamento {data_hora.strftime('%d/%m/%Y')}"
    menu = (
        "Meio de pagamento disponível:\n"
        "  0 – Cartão de Débito\n"
        "  1 – Cartão de Crédito à Vista\n"
        "  2 – Cartão de Crédito Parcelado\n"
        "  9 – Sair"
    )
    return f"{linha}\n{titulo}\n{menu}"


def ler_valor(prompt: str) -> float:
    """Lê um valor monetário aceitando vírgula ou ponto como decimal."""
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            v = float(raw)
            if v <= 0:
                print("  ⚠  O valor deve ser maior que zero. Tente novamente.")
                continue
            return v
        except ValueError:
            print("  ⚠  Valor inválido. Use números (ex.: 300,00 ou 300.00).")


def ler_parcelas() -> int:
    """Lê a quantidade de parcelas (2 ou 3)."""
    while True:
        raw = input("Quantidade de parcelas (2 ou 3): ").strip()
        if raw in ("2", "3"):
            return int(raw)
        print("  ⚠  Opção inválida. Digite 2 ou 3.")


# ─────────────────────────────────────────────
# PROCESSAMENTO DE PAGAMENTO
# ─────────────────────────────────────────────

def processar_debito(valor: float, agora: datetime):
    mdr       = round(valor * MDR_DEBITO, 2)
    liquido   = round(valor - mdr, 2)
    # D+1, avança se cair no fim de semana
    credito   = proximo_dia_util(agora + timedelta(days=1))

    print("\n" + "=" * 70)
    print(f"Data da compra         : {agora.strftime('%d/%m/%Y')}")
    print(f"Hora da compra         : {agora.strftime('%H:%M')}")
    print(f"Meio de pagamento      : 0 – Cartão de Débito")
    print(f"Valor da compra        : {formatar_valor(valor)}")
    print(f"Valor do MDR (taxa)    : {formatar_valor(mdr)}")
    print(f"Valor líquido          : {formatar_valor(liquido)}")
    print(f"Data de crédito        : {credito.strftime('%d/%m/%Y')}")
    print("=" * 70)


def processar_credito_vista(valor: float, agora: datetime):
    mdr       = round(valor * MDR_CREDITO, 2)
    liquido   = round(valor - mdr, 2)
    # D+30, avança se cair no fim de semana
    credito   = proximo_dia_util(agora + timedelta(days=30))

    print("\n" + "=" * 70)
    print(f"Data da compra         : {agora.strftime('%d/%m/%Y')}")
    print(f"Hora da compra         : {agora.strftime('%H:%M')}")
    print(f"Meio de pagamento      : 1 – Cartão de Crédito à Vista")
    print(f"Valor da compra        : {formatar_valor(valor)}")
    print(f"Valor do MDR (taxa)    : {formatar_valor(mdr)}")
    print(f"Valor líquido          : {formatar_valor(liquido)}")
    print(f"Data de crédito        : {credito.strftime('%d/%m/%Y')}")
    print("=" * 70)


def processar_credito_parcelado(valor: float, n_parcelas: int, agora: datetime):
    mdr     = round(valor * MDR_CREDITO, 2)
    liquido = round(valor - mdr, 2)

    # Calcula parcelas com arredondamento correto
    parcela_base = round(liquido / n_parcelas, 2)
    # A primeira parcela absorve a diferença de centavos
    soma_restantes = round(parcela_base * (n_parcelas - 1), 2)
    primeira_parcela = round(liquido - soma_restantes, 2)

    parcelas = [primeira_parcela] + [parcela_base] * (n_parcelas - 1)

    # Datas: D+30, D+60, D+90 … avançando fins de semana
    datas = []
    for i in range(1, n_parcelas + 1):
        d = proximo_dia_util(agora + timedelta(days=30 * i))
        datas.append(d)

    print("\n" + "=" * 70)
    print(f"Data da compra         : {agora.strftime('%d/%m/%Y')}")
    print(f"Hora da compra         : {agora.strftime('%H:%M')}")
    print(f"Meio de pagamento      : 2 – Cartão de Crédito Parcelado")
    print(f"Valor da compra        : {formatar_valor(valor)}")
    print(f"Valor do MDR (taxa)    : {formatar_valor(mdr)}")
    print(f"Valor líquido total    : {formatar_valor(liquido)}")

    for i in range(n_parcelas):
        print(f"\n  Parcela              : {i + 1}/{n_parcelas}")
        print(f"  Valor líquido        : {formatar_valor(parcelas[i])}")
        print(f"  Data de crédito      : {datas[i].strftime('%d/%m/%Y')}")

    print("=" * 70)


# ─────────────────────────────────────────────
# LOOP PRINCIPAL
# ─────────────────────────────────────────────

def main():
    while True:
        agora = datetime.now()
        print("\n" + cabecalho(agora))

        opcao = input("\nEscolha o meio de pagamento: ").strip()

        if opcao == "9":
            print("\nEncerrando o SMM. Até logo!")
            break

        elif opcao == "0":
            valor = ler_valor("Valor da compra: R$ ")
            processar_debito(valor, agora)

        elif opcao == "1":
            valor = ler_valor("Valor da compra: R$ ")
            processar_credito_vista(valor, agora)

        elif opcao == "2":
            valor     = ler_valor("Valor da compra: R$ ")
            n_parcelas = ler_parcelas()
            processar_credito_parcelado(valor, n_parcelas, agora)

        else:
            print("\n  ⚠  Opção inválida. Por favor, escolha 0, 1, 2 ou 9.")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    main()