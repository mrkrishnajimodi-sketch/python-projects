"""THIS IS MY FIRST PROJECT IN PYTHON TODAY I AM BULIDING PROJECT on diamond management system"""
# i am using dictonaries for showing price of diamonds brand
diamonds={"indian_diamond":266000, 
          "american_diamonds":400000,
          "french_diamonds":330000,
          "italy_diamonds":500000,
         "pakistan_diamonds":40000,
         "china_diamonds":150000}

# first of all we have to greet 
print("welcome to Modi's Groups of diamonds and tell me how can help you ")
total_bill=0

items_1=input("tell me which diamonds you want")

if items_1 in diamonds:#members operator
    print(f"this is {items_1} & it is so beautiful")
    total_bill+=diamonds[items_1]

    print(" do you want something else yes/no")
    another_product=input(" do you want anything else tell me yes or no ")
    if another_product=="yes":
        items_2=input("tell your next product")
        if items_2 in diamonds:
            print(f"this is {items_2} & its so elegant")
            total_bill+=diamonds[items_2]
            print("this is your total bill you have to pay",total_bill)
        elif another_product=="NO":
            print(f"this is your total bill you have to pay",total_bill)
        else:
            print("sorry we dont have items 2")
            
else:
    print("sorry we dont have this product tell me anyhing esle:")


    
#
    


