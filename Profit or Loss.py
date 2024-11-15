actual_cost=float(input("enter the actual product price: "))
sale_amount=float(input("enter the sale amount: "))
if actual_cost<sale_amount:
    amount=sale_amount-actual_cost
    print("Total profit= {0}".format(amount))
else:
    print("no profit")