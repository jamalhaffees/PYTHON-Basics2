countries = ['USA','Canada','China','India','France','Germany']
print(countries)
print(countries[2])
print(countries[-1])
countries[0]='Iceland'
print(countries)

fruits = ['Banana','orange','apple','strawberry','watermelon']
vegetables = ['carrot','beans','cauliflower', 'potato']
final_shopping_list = (fruits + vegetables)
print(final_shopping_list)
if 'apple' in final_shopping_list:
    print("yes, 'apple' is in the shopping list")
print(len(final_shopping_list))
final_shopping_list.append('spinach')
print(final_shopping_list)
final_shopping_list.remove('potato')
print(final_shopping_list)
sweets = ['donuts', 'cakes','ice cream', 'biscotti']
final_shopping_list.extend(sweets)
print(final_shopping_list)
final_shopping_list.remove('apple')
print(final_shopping_list)
customer_info = 'Mike|Canada|30|Male'
customer = customer_info.split('|')
print(customer)