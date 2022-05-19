price = float(input("Digite o preço do produto: "))
price_descount = price-((price/100)*5)

print("O produto com preço total de {} sai por {} com 5% de desconto.".format(price, price_descount))
