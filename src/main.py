from helper import (
    print_menu, 
    get_user_input, 
    get_str_user_input, 
    print_line
)

from update import (
    open_xlsx, 
    show_sorted_excel_data, 
    get_net_worth, 
    change_amount, 
    save_excel, 
    add_a_row, 
    remove_a_row
)


def main() :
    excel = "net_worth.xlsx"
    df = open_xlsx(excel)
    
    while True :
        print_line()
        print_menu()
        input_type = "menu choice"
        user_choice = get_user_input("Enter the number: ", input_type, None)
        print_line()
        
        if user_choice == 1 :
            all_data = show_sorted_excel_data(df)
            
            print(f"Your excel data: \n{all_data}")
            
        elif user_choice == 2 :
            net_worth = get_net_worth(df)
            
            print(f"Your net worth is: {net_worth}")
            
        elif user_choice == 3 :
            print(f"{df}\n")
            
            input_type = "row choice"
            row_id = get_user_input("Enter the row id: ", input_type, df)
            print(f"You chose: \n{df.loc[row_id]}")
            
            money_amount = get_user_input("Enter the amount: ", None, None)
            
            change_amount(df, row_id, money_amount)
            save_excel(df, excel)
            print(f"Row {row_id} changed!")
        
        elif user_choice == 4 :
            input_type = "money"
            money_source = get_str_user_input("Enter the money source: ", input_type, df)
            input_type = "type"
            money_type = get_str_user_input("Enter if it is a receivable or owned: ", input_type, None)
            amount = get_user_input("Enter the amount: ", None, None)
            
            new_df = add_a_row(df, money_source, money_type, amount)
            save_excel(new_df, excel)
            print("Successfully added a new row!")
        
        elif user_choice == 5 :
            print(f"{df}\n")
                        
            input_type = "row choice"
            row_id = get_user_input("Enter the row id: ", input_type, df)
            print(f"You chose: \n{df.loc[row_id]}")
            
            input_type = "verify"
            verify = get_str_user_input("Are you sure you want to proceed(y/n)? ", input_type, None)
            
            if verify == "y" :
                df = remove_a_row(df, row_id)
                save_excel(df, excel)
                print(f"Removed row {row_id}")
        
        else :
            break
    

if __name__ == "__main__" :
    main()