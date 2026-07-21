import pandas as pd
import sys
from datetime import datetime
today = datetime.now()
f1 = today.strftime("%d-%m-%Y")
f2 = today.strftime("%Y%d%m")
def main():
    print("="*80)
    print("Hello, welcome to your personalized INVENTORY MANAGEMENT SYSTEM!")
    print("="*80)
    print("📋Main Menu:\n1. Product Management\n2. Inventory Management\n3. Billing System\n4. Reports\n5. Exit")
    print("="*80)
    while True:
        try:
            opt = int(input("Your choice: "))
            if 0<opt<6:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    if opt==1:
        product_management()
    elif opt==2:
        inventory_management()
    elif opt==3:
        billing_system()
    elif opt==4:
        reports()
    else:
        exit()
def product_management():
    print("="*80)
    print("📋Product Management Menu:\n1. Add Product\n2. Update Product\n3. Delete Product\n4. Search Product\n5. List All Products\n6. Back")
    print("="*80)
    while True:
        try:
            opt = int(input("Your choice: "))
            if 0<opt<7:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    product_list = pd.read_csv("product_list.csv",dtype={"ID":str})
    if opt==1:
        print("="*80)
        print("ADD PRODUCT")
        print("="*80)
        pro_id = input("Product Id: ").strip()
        pro_name = input("Product Name: ").strip().upper()
        pro_price = float(input("Product Price: "))
        pro_quantity = int(input("Product Quantity: "))
        new_product = {"ID":[pro_id],
               "NAME":[pro_name],
               "PRICE":[pro_price],
               "QUANTITY":[pro_quantity]}
        product_list = pd.concat([product_list,pd.DataFrame(new_product)])
        product_list.to_csv("product_list.csv",index=False)
        print("="*80)
        print("Product added successfully...✅")
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==2:
        print("="*80)
        print("UPDATE PRODUCT")
        print("="*80)
        id = input("Enter product ID to update: ")
        print("Select what you want to update:\n1. Product Name\n2. Product Price\n3. Product Quantity\n4. Cancel")
        while True:
            try:
                op = int(input("Your choice: "))
                if 0<op<5:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if op==1:
            print("="*80)
            print("Current Name:", product_list.loc[product_list["ID"]==id,"NAME"].values[0])
            new_name = input("New name: ").strip().upper()
            product_list.loc[product_list["ID"]==id,"NAME"] = new_name
            product_list.to_csv("product_list.csv",index=False)
            print("Name updated successfully...✅")
            print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        elif op==2:
            print("="*80)
            print("Current Price:", product_list.loc[product_list["ID"]==id,"PRICE"].values[0])
            new_price = float(input("New price: "))
            product_list.loc[product_list["ID"]==id,"PRICE"] = new_price
            product_list.to_csv("product_list.csv",index=False)
            print("Price updated successfully...✅")
            print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        elif op==3:
            print("="*80)
            print("Current Stock:", product_list.loc[product_list["ID"]==id,"QUANTITY"].values[0],"items")
            new_stock = float(input("New stock: "))
            product_list.loc[product_list["ID"]==id,"QUANTITY"] = new_stock
            product_list.to_csv("product_list.csv",index=False)
            print("Stock updated successfully...✅")
            print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        else:
            main()
    elif opt==3:
        print("="*80)
        print("DELETE PRODUCT")
        print("="*80)
        id = input("Enter product ID to delete: ")
        product_list = product_list[product_list["ID"]!=id]
        product_list.to_csv("product_list.csv",index=False)
        print("Product deleted successfully...✅")
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==4:
        print("="*80)
        print("SEARCH PRODUCT")
        print("="*80)
        print("Search by:\n1. Product ID\n2. Product NAME\n3. Cancel/Back to main menu")
        while True:
            try:
                op = int(input("Your choice: "))
                if 0<op<4:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if op==1:
            print("="*80)
            id = input("Enter product ID to search: ").strip()
            result = product_list[product_list["ID"]==id]
            if result.empty:
                print("Product not found!")
            else:
                print(result.to_string(index=False))
            print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        elif op==2:
            print("="*80)
            name = input("Enter product name to search: ").strip().upper()
            result = product_list[product_list["NAME"]==name]
            if result.empty:
                print("Product not found!")
            else:
                print(result.to_string(index=False))
            print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        else:
            main()
    elif opt==5:
        print("="*80)
        print("PRODUCT LIST")
        print("="*80)
        product_list = pd.DataFrame(product_list)
        print(product_list.to_string(index=False))
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    else:
        main()
def inventory_management():
    print("="*80)
    print("📋Inventory Menu:\n1. Add Stock to Product\n2. Reduce Stock for Testing\n3. Check Stock\n4. Back")
    print("="*80)
    while True:
        try:
            opt = int(input("Your choice: "))
            if 0<opt<5:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    product_list = pd.read_csv("product_list.csv",dtype={"ID":str})
    if opt==1:
        print("="*80)
        id = input("Enter product ID: ").strip()
        current_quantity = product_list.loc[product_list["ID"]==id,"QUANTITY"].values[0]
        print("Current Quantity:", current_quantity,"items")
        new_stock = int(input("Enter quantity to add: "))
        product_list.loc[product_list["ID"]==id,"QUANTITY"] = new_stock+current_quantity
        product_list.to_csv("product_list.csv",index=False)
        print("Stock updated successfully...✅")
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==2:
        print("="*80)
        id = input("Enter product ID: ").strip()
        current_quantity = product_list.loc[product_list["ID"]==id,"QUANTITY"].values[0]
        print("Current Quantity:", current_quantity,"items")
        new_stock = int(input("Enter quantity to remove: "))
        product_list.loc[product_list["ID"]==id,"QUANTITY"] = current_quantity-new_stock
        product_list.to_csv("product_list.csv",index=False)
        print("Stock updated successfully...✅")
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==3:
        print("="*80)
        print("1. Check by product ID\n2. Display all products\n3. Back")
        while True:
            try:
                op = int(input("Your choice: "))
                if 0<op<4:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if op==1:
            id = input("Enter product ID to search: ").strip()
            result = product_list[product_list["ID"]==id]
            if result.empty:
                print("="*80)
                print("Product not found!")
                print("="*80)
            else:
                print("="*80)
                result = result.drop(columns=["PRICE"])
                print(result.to_string(index=False))
                print("="*80)
        elif op==2:
            print("="*80)
            print("INVENTORY")
            print("="*80)
            product_list = pd.DataFrame(product_list)
            result = product_list.drop(columns=["PRICE"])
            print(result.to_string(index=False))
            print("="*80)
        else:
            inventory_management()
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    else:
        main()
def billing_system():
    print("="*80)
    print("📋Billing Menu:\n1. Create New Bill\n2. View Billing History\n3. Search Bill\n4. Back")
    print("="*80)
    while True:
        try:
            opt = int(input("Your choice: "))
            if 0<opt<5:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    product_list = pd.read_csv("product_list.csv",dtype={"ID":str})
    if opt==1:
        def gst(am,tp = 0.18):
            gam = am*tp
            return gam
        print("="*80)
        customer_name = input("Enter customer name: ").strip().upper()
        flag = True
        subtotal = 0
        cust_bill = {
            "ID":[],
            "NAME":[],
            "PRICE":[],
            "QUANTITY":[],
            "TOTAL":[]
        }
        while flag:
            id = input("Enter product ID: ").strip()
            result = product_list[product_list["ID"]==id]
            if result.empty:
                print("Product not found!")
                continue
            quantity = int(input("Enter quantity: "))
            pro_quantity = product_list.loc[product_list["ID"]==id,"QUANTITY"].values[0]
            if quantity==0:
                print("Product not added...")
                continue
            if pro_quantity<quantity:
                print(f"{pro_quantity} left!")
                print("Product not added...")
                continue
            product_list.loc[product_list["ID"]==id,"QUANTITY"] = pro_quantity-quantity
            pro_name = product_list.loc[product_list["ID"]==id,"NAME"].values[0]
            cost = product_list.loc[product_list["ID"]==id,"PRICE"].values[0]*quantity
            subtotal += cost
            cust_bill["ID"].append(id)
            cust_bill["NAME"].append(pro_name)
            cust_bill["PRICE"].append(product_list.loc[product_list["ID"]==id,"PRICE"].values[0])
            cust_bill["QUANTITY"].append(quantity)
            cust_bill["TOTAL"].append(cost)
            product_list.to_csv("product_list.csv",index=False)
            productwiseSales = pd.read_csv("product_sales.csv",dtype={"ID":str})
            salesReport = productwiseSales[productwiseSales["ID"]==id]
            if salesReport.empty:
                new_row = pd.DataFrame([{
                "ID": id,
                "NAME": pro_name,
                "QUANTITY SOLD": quantity,
                "TOTAL AMOUNT": cost
                }])
                productwiseSales = pd.concat([productwiseSales, new_row], ignore_index=True)
                productwiseSales.to_csv("product_sales.csv", index=False)
            else:
                sales_quantity = productwiseSales.loc[productwiseSales["ID"]==id,"QUANTITY SOLD"].values[0]
                sales_cost = productwiseSales.loc[productwiseSales["ID"]==id,"TOTAL AMOUNT"].values[0]
                productwiseSales.loc[productwiseSales["ID"]==id,"QUANTITY SOLD"] = sales_quantity + quantity
                productwiseSales.loc[productwiseSales["ID"]==id,"TOTAL AMOUNT"] = sales_cost + cost
                productwiseSales.to_csv("product_sales.csv",index=False)
            print("="*80)
            print(f"{pro_name} added successfully...✅")
            print(f"Subtotal: {subtotal}")
            print("="*80)
            add_exit = int(input("1. Add another item\n2. Generate bill\nYour choice: "))
            print("="*80)
            if add_exit==1:
                flag = True
            else:
                flag=False
                print("Generating bill...")
        df = pd.DataFrame(cust_bill)
        bill_details = {"Bill No":[],
               "Customer Name":[],
               "Date":[],
               "Total Amount":[]}
        bill_history = pd.read_csv("bill_history.csv")
        product_list_df = pd.DataFrame(bill_history)
        if not bill_history.empty:
            last_bill = product_list_df.iloc[-1]["Bill No"]
        else:
            last_bill = "00000000000"
        if str(last_bill)[0:8]!=f2:
            count = 1
        else:
            count = int(str(last_bill)[8:])+1
        bill_details["Bill No"].append(f'{f2}00{count}')
        bill_details["Customer Name"].append(customer_name)
        bill_details["Date"].append(f1)
        bill_details["Total Amount"].append(f"{subtotal:.2f}")
        df_bill = pd.DataFrame(bill_details)
        bill_history = pd.concat([bill_history,df_bill])
        with open(f"{f2}00{count}_{customer_name}.docx","w") as f:
            gst_amount = gst(subtotal)
            f.write(f"Customer Name: {customer_name}\n")
            f.write(f"Date of billing: {f1}\n")
            f.write("-"*70+"\n")
            f.write(df.to_string(index=False))
            f.write("\n"+"-"*70+"\n")
            f.write(f"GST appilcable = 18%\n")
            f.write(f"GST amount = {gst_amount:.2f}\n")
            f.write("-"*70+"\n")
            f.write(f"Total Amount: {subtotal+gst_amount:.2f}\n")
            f.write(f"Bill Number: {f2}00{count}")
        bill_history.to_csv("bill_history.csv",index=False)
        print("Bill created successfully...✅")
        exit()
    elif opt==2:
        bill_history = pd.read_csv("bill_history.csv")
        bill_history = pd.DataFrame(bill_history)
        print("="*80)
        print("BILLING HISTORY")
        print("="*80)
        if bill_history.empty:
            print("No bills found!")
        else:
            print(bill_history.to_string(index=False))
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==3:
        print("="*80)
        print("SEARCH BILL")
        print("="*80)
        print("1. Search by bill number\n2. Search by name\n3. Search by date\n4. Back")
        while True:
            try:
                op = int(input("Your choice: "))
                if 0<op<5:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        bills = pd.read_csv("bill_history.csv")
        if op==1:
            bill_no = int(input("Enter bill number: "))
            result = bills[bills["Bill No"]==bill_no]
            if result.empty:
                print("="*80)
                print("Bill not found!")
                print("="*80)
            else:
                print("="*80)
                print(result.to_string(index=False))
                print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        elif op==2:
            name = input("Enter customer name: ").strip().upper()
            result = bills[bills["Customer Name"]==name]
            if result.empty:
                print("="*80)
                print("Bill not found!")
                print("="*80)
            else:
                print("="*80)
                print(result.to_string(index=False))
                print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        elif op==3:
            date = input("Enter date in (dd-mm-yyyy) format: ").strip()
            result = bills[bills["Date"]==date]
            if result.empty:
                print("="*80)
                print("Bill not found!")
                print("="*80)
            else:
                print("="*80)
                print(result.to_string(index=False))
                print("="*80)
            print("1. Back to main menu\n2. Exit")
            while True:
                try:
                    choice = int(input("Your choice: "))
                    if 0<choice<3:
                        break
                    else:
                        print("Invalid choice!")
                except ValueError:
                    print("Invalid choice!")
            if choice==1:
                main()
            else:
                exit()
        else:
            billing_system()
        pass
    else:
        main()
def reports():
    print("="*80)
    print("📋Inventory Management Menu:\n1. Daily Sales Report\n2. Product-wise Sales Report\n3. Low Stock Report\n4. Back")
    print("="*80)
    while True:
        try:
            opt = int(input("Your choice: "))
            if 0<opt<5:
                break
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid choice!")
    bills = pd.read_csv("bill_history.csv")
    product_sales = pd.read_csv("product_sales.csv",dtype={"ID":str})
    product_list = pd.read_csv("product_list.csv",dtype={"ID":str})
    if opt==1:
        print("="*80)
        print("DAILY SALES REPORT")
        print("="*80)
        date = input("Enter date in (dd-mm-yyyy) format: ").strip()
        result = bills[bills["Date"]==date]
        if result.empty:
            print("="*80)
            print(f"No Sales on {date}!")
            print("="*80)
        else:
            df = pd.DataFrame(result)
            no_sales = len(df)
            total_sales = df["Total Amount"].sum()
            df = df.drop(columns=["Date"])
            print("="*80)
            print(f"Date: {date}")
            print(f"Total Bills: {no_sales}")
            print('-'*80)
            print(df.to_string(index=False))
            print('-'*80)
            print(f"Total sales: {total_sales}")
            print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==2:
        print("="*80)
        print("PRODUCT-WISE SALES REPORT")
        print("="*80)
        print("1. Search by product id\n2. Search by product name\n3. Back")
        while True:
            try:
                op = int(input("Your choice: "))
                if 0<op<4:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if op==1:
            id = input("Enter product ID: ").strip()
            result = product_sales[product_sales["ID"]==id]
            if result.empty:
                print("="*80)
                print("No sales found!")
                print("="*80)
            else:
                print("="*80)
                print(result.to_string(index=False))
                print("="*80)
        elif op==2:
            name = input("Enter product name: ").strip().upper()
            result = product_sales[product_sales["NAME"]==name]
            if result.empty:
                print("="*80)
                print("No sales found!")
                print("="*80)
            else:
                print("="*80)
                print(result.to_string(index=False))
                print("="*80)
        else:
            reports()
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    elif opt==3:
        print("="*80)
        print("LOW STOCK REPORT")
        print("="*80)
        df = product_list[product_list["QUANTITY"]<10]
        print(df.to_string(index=False))
        print("="*80)
        print("1. Back to main menu\n2. Exit")
        while True:
            try:
                choice = int(input("Your choice: "))
                if 0<choice<3:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")
        if choice==1:
            main()
        else:
            exit()
    else:
        main()
def exit():
    print("="*80)
    print("Thanks for using Inventory Management System!")
    print("Exiting program now....")
    print("Goodbye!")
    print("="*80)
    sys.exit()
main()