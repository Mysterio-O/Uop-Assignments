# this is the function and its taking an argument as radius
def print_circum(radius):
    # first imported the math module (math has some its own methods for many complex calculations, like : pi)
    import math;
    
    # actual pi = 3.141592653589793
    # math.pi is used to get the value of pi from the math module
    
    circumference = 2 * math.pi * radius # formula to calculate circumference of circle
    
    # here i'm printing the circumference value with f string
    print(f"the circumference of given {radius} is:- {circumference}")
    
# print_circum(5)
# print_circum(6)
# print_circum(7)










def online_store_catalog():
    # dictionary storing base prices of three items.
    # keys represent item numbers, values represent prices.
    item_prices = {
        1: 200.0,
        2: 400.0,
        3: 600.0,
    }
    # nested helper function that calculates total price and applies the correct discount depending on how many unique items are included.
    def total_with_discount(items):
        # calculate the subtotal by adding the prices of all item numbers passed inside the 'items' list.
        subtotal = sum(item_prices[i] for i in items)

        # discount rules based on number of items:
        if len(items) == 1:              # single item -> no discount
            discount_rate = 0.00
        elif len(items) == 2:            # two unique items -> 10% discount
            discount_rate = 0.10
        else:                            # all three items -> 25% discount
            discount_rate = 0.25

        # apply the discount and return final price.
        return subtotal * (1 - discount_rate)

    # --------- output section (Receipt Format) ----------
    print("Online Store")
    print("---------------------------")
    # format the header into two aligned columns.
    print(f"{'Product(S)':<20}{'Price'}")

    # print individual items with no discount
    print(f"{'Item 1':<20}{total_with_discount([1]):.1f}")
    print(f"{'Item 2':<20}{total_with_discount([2]):.1f}")
    print(f"{'Item 3':<20}{total_with_discount([3]):.1f}")

    # print combo packs and automatically apply discount logic
    print(f"{'Combo 1(Item 1 + 2)':<20}{total_with_discount([1, 2]):.1f}")
    print(f"{'Combo 2(Item 2 + 3)':<20}{total_with_discount([2, 3]):.1f}")
    print(f"{'Combo 3(Item 1 + 3)':<20}{total_with_discount([1, 3]):.1f}")
    print(f"{'Combo 4(Item 1 + 2 + 3)':<20}{total_with_discount([1, 2, 3]):.1f}")

    # footer
    print("---------------------------")
    print("For delivery Contact:98764678899")


# call the function so we can see the printed receipt
online_store_catalog()

