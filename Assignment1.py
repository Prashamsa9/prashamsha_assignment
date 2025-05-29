#1.calculate the TotalRevenue
def calculate_total_revenue(inventory):
    return sum(item[2]*item[3] for item in inventory)


inventory = [

    ["Strawberry", "Fruit",      3.50,        40,          10],

    ["Broccoli",   "Vegetable",  2.20,        25,           8],

    ["Cheddar",    "Dairy",      5.00,        18,           4],

    ["Baguette",   "Bakery",     2.80,        35,           2],

    ["Blueberry",  "Fruit",      4.00,        22,           6],

    ["Spinach",    "Vegetable",  1.80,        30,          12],

    ["Yogurt",     "Dairy",      1.20,        50,          15],

    ["Croissant",  "Bakery",     3.00,        28,           3],

]

Totalrevenue=calculate_total_revenue(inventory)
print('Total revenue is :',Totalrevenue)


#2.List Low stock item if stock is less than 5

def lowestunitssold(inventory):
    names=[]
    for item in inventory:
        name=item[0]
        units_sold=item[4]
        if units_sold<5:
            names.append(name)
    return names

    



inventory = [

    ["Strawberry", "Fruit",      3.50,        40,          10],

    ["Broccoli",   "Vegetable",  2.20,        25,           8],

    ["Cheddar",    "Dairy",      5.00,        18,           4],

    ["Baguette",   "Bakery",     2.80,        35,           2],

    ["Blueberry",  "Fruit",      4.00,        22,           6],

    ["Spinach",    "Vegetable",  1.80,        30,          12],

    ["Yogurt",     "Dairy",      1.20,        50,          15],

    ["Croissant",  "Bakery",     3.00,        28,           3],

]

names1=lowestunitssold(inventory)
for item in names1:
    print(item," ")

inventory = [

    ["Strawberry", "Fruit",      3.50,        40,          10],

    ["Broccoli",   "Vegetable",  2.20,        25,           8],

    ["Cheddar",    "Dairy",      5.00,        18,           4],

    ["Baguette",   "Bakery",     2.80,        35,           2],

    ["Blueberry",  "Fruit",      4.00,        22,           6],

    ["Spinach",    "Vegetable",  1.80,        30,          12],

    ["Yogurt",     "Dairy",      1.20,        50,          15],

    ["Croissant",  "Bakery",     3.00,        28,           3],

]

category_wise= {}
for item in inventory:
    category=item[1]
    unit_price =item[2]
    units_sold=item[3]
    revenue= unit_price*units_sold
    
    if category not in category_wise:
        category_wise[category]=0
    category_wise[category] +=revenue

print("category_wise revenue:")  
for category, revenue in category_wise.items():
    print(f'{category},{revenue}')
