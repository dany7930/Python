def calculate_bill():
    items = []
    print("\nWelcome to the Bill Calculator!")
    print("Enter items one by one. Type 'done' when finished.\n")
    
    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        
        try:
            price = float(input("Enter item price: "))
            quantity = float(input("Enter quantity: "))
            items.append({
                'name': item_name,
                'price': price,
                'quantity': quantity,
                'total': price * quantity
            })
        except ValueError:
            print("Please enter valid numbers for price and quantity.")
            continue
    
    if not items:
        print("No items entered. Exiting...")
        return
    
    # Calculate subtotal
    subtotal = sum(item['total'] for item in items)
    
    # Apply tax
    try:
        tax_rate = float(input("\nEnter tax rate percentage (e.g., 8.5 for 8.5%): "))
        tax_amount = subtotal * (tax_rate / 100)
    except ValueError:
        print("Invalid tax rate. Setting to 0%.")
        tax_amount = 0
    
    # Apply discount
    try:
        discount = input("Enter discount amount (fixed) or percentage (with % sign): ")
        if '%' in discount:
            discount_rate = float(discount.replace('%', ''))
            discount_amount = subtotal * (discount_rate / 100)
        else:
            discount_amount = float(discount)
        
        # Ensure discount doesn't exceed subtotal
        discount_amount = min(discount_amount, subtotal)
    except ValueError:
        print("Invalid discount. Setting to 0.")
        discount_amount = 0
    
    # Calculate final total
    total = subtotal + tax_amount - discount_amount
    
    # Display bill
    print("\n" + "="*40)
    print("BILL SUMMARY".center(40))
    print("="*40)
    print(f"{'Item':<20}{'Qty':>6}{'Price':>8}{'Total':>8}")
    print("-"*40)
    
    for item in items:
        print(f"{item['name'][:18]:<20}{item['quantity']:>6}{item['price']:>8.2f}{item['total']:>8.2f}")
    
    print("-"*40)
    print(f"{'Subtotal:':<30}{subtotal:>10.2f}")
    print(f"{f'Tax ({tax_rate}%):':<30}{tax_amount:>10.2f}")
    print(f"{'Discount:':<30}{discount_amount:>10.2f}")
    print("="*40)
    print(f"{'TOTAL:':<30}{total:>10.2f}")
    print("="*40)

if __name__ == "__main__":
    calculate_bill()