#Product Cost

print('Product Cost')

total_cost = cheap_product = expensive_product = 0
cheap_product_name = ' '
product_counter = 0

while True:
	product_name = input('Product name:')
	product_price = int(input('Product price:'))
	
	total_cost += product_price
	product_counter += 1
	
	if product_price >= 1000:
		expensive_product += 1
	
	if product_counter == 1 or product_price < cheap_product:
		cheap_product = product_price
		cheap_product_name = product_name
	
	print(f'Total cost {total_cost}, {expensive_product} products cost more than 1000$, The cheapest product was {cheap_product_name}')
	question = input('Continue? [Y or N]').strip().upper()[0]
	
	if question == 'N':
		print('Program finished')
		break