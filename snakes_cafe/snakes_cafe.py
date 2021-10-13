print(
"""   
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

""" )

our_items={
"Wings":0,
"Cookies" :0,
"Spring Rolls":0,
"Salmon":0,
"Steak":0,
"Meat Tornado":0,
"A Literal Garden":0,
"Ice Cream":0,
"Cake":0,
"Pie":0,
"Coffee":0,
"Tea":0,
"Unicorn Tears":0
}

def summary(object):
    the_ordered_items=''
    for item in object:
        if object[item]>0:
          the_ordered_items += f"{object[item]} {item} \n"  
    return the_ordered_items

def response(order : str)-> str:
    if order in our_items:
        our_items[order]+=1
        return f"**{our_items[order]} order of {order} have been added to your meal **"
    elif order == "quit":
        the_order=summary(our_items)
        print(
        """   
        **************************************
                  **   Summary   **
        **************************************
        """  )
        return the_order
    else: 
        return f"Try again,check your spelling"



def main():
    answers=None
    while answers!= "quit":
        answers=input("your order >")
        print(response(answers))

if __name__ == "__main__":
    main()