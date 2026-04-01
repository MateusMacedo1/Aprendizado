# --- ENTRADAS ---
custo = float(input("Custo do produto (Compra/Reposição): R$ "))

# --- REGRAS DA NOVA POLÍTICA SHOPEE ---
# Como não sabemos o preço final ainda, estimamos a faixa pela base do custo
if custo < 50:
    taxa_fixa, comissao_pct = 4.0, 0.20
else:
    taxa_fixa, comissao_pct = 16.0, 0.14

# --- CÁLCULOS DE PREÇO SUGERIDO ---
# Preço = (Custo + Taxa Fixa) / (1 - (Comissão% + Lucro%))
venda_20 = (custo + taxa_fixa) / (1 - (comissao_pct + 0.20))
venda_30 = (custo + taxa_fixa) / (1 - (comissao_pct + 0.30))

# --- CÁLCULO DAS TAXAS QUE VOCÊ VAI PAGAR EM CADA CENÁRIO ---
taxa_paga_20 = (venda_20 * comissao_pct) + taxa_fixa
taxa_paga_30 = (venda_30 * comissao_pct) + taxa_fixa

# --- RESULTADO FINAL ---
print("\n" + "="*50)
print(f"ESTRATÉGIA DE PRECIFICAÇÃO")
print("="*50)
print(f"CUSTO DA PEÇA: R$ {custo:.2f}")

print("-" * 50)
print(f"MARGEM DE 20%")
print(f" > Preço de Venda:    R$ {venda_20:.2f}")
print(f" > TAXA SHOPEE:      R$ {taxa_paga_20:.2f} (Retirado)")
print(f" > Seu Lucro Real:   R$ {venda_20 * 0.20:.2f}")

print("-" * 50)
print(f"MARGEM SUGERIDA DE 30%")
print(f" > Preço de Venda:    R$ {venda_30:.2f}")
print(f" > TAXA SHOPEE:      R$ {taxa_paga_30:.2f} (Retirado)")
print(f" > Seu Lucro Real:   R$ {venda_30 * 0.30:.2f}")
print("="*50)