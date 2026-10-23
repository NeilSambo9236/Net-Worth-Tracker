from textwrap import dedent


def print_line() :
    print("_" * 38)


def print_invalid_message() :
    print("Invalid input. Please try again. ", end="")
    
    
def get_str_user_input(query, input_type, df) :
    while True :
        user_input = input(query).strip()
        
        if input_type == "money" :
            if user_input.title() in df["Name"].values :
                print("Money source is already saved. ", end="")
                continue
            
        if input_type == "type" :
            if user_input.lower() not in ("receivable", "owned") :
                print_invalid_message()
                continue
            
        if input_type == "verify" :
            if user_input.lower() not in ("y", "n") :
                print_invalid_message()
                continue
            
        if input_type == "amount updater" :
            if user_input not in ("1", "2", "3") :
                print_invalid_message()
                continue
    
        return user_input
    
    
def get_float_user_input(query) :
    while True :
        user_input = input(query).strip()
        
        if user_input == "" :
            continue
        
        try :
            user_input = float(user_input)
            
            if user_input <= 0 :
                print("Cannot put negative values! ", end="")
                continue
            
            return user_input
            
        except ValueError :
            print_invalid_message()
            continue        


def get_int_user_input(query, input_type, df) :
    while True :
        user_input = input(query).strip()
        
        if user_input == "" :
            continue
        
        try :
            user_input = int(user_input)
            
            if input_type == "menu choice" :
                if 0 < user_input <= 6 :
                    return user_input
                
                else :
                    print_invalid_message()
                    continue
            
            elif input_type == "row choice" :
                if df.index.min() <= user_input <= df.index.max() :
                    return user_input
                
                else :
                    print_invalid_message()
                    continue
        
        except ValueError :
            print_invalid_message()
            continue
        
        
def print_amount_updater_choices() :
    print(dedent(
    """
    Choose:
    1 - Change an amount
    2 - Add to an amount
    3 - Subtract from an amount
    """))


def print_menu() :
    print(dedent(
    """
    Choose: 
    1 - Print excel data
    2 - Show net worth
    3 - Change an amount
    4 - Add a row
    5 - Delete a row
    6 - Exit
    """))