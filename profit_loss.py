actual_cost = float(input("Please enter the Actual Product Price:"))
sale_amount = float (input("Please enter the Sales Amount:"))
if (sale_amount > actual_cost):
    profit = sale_amount-actual_cost
    print ("Total profit = {0}" .format(profit))
else:
    print ("No Profit!!!")
