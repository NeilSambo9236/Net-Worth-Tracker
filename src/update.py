import pandas as pd


def save_excel(df, excel) :
    df.to_excel(excel, index=False)
    
    
def remove_a_row(df, row_id) :
    return df.drop(index=row_id)


def add_a_row(df, money_source, type, amount) :
    money_source, type = money_source.title(), type.title()
    df.loc[len(df)] = [money_source, type, amount]

    return df


def subtract_amount(df, row_id, money_amount_to_subtract) :
    df.loc[row_id, "Amount"] -= money_amount_to_subtract


def add_amount(df, row_id, money_amount_to_add) :
    df.loc[row_id, "Amount"] += money_amount_to_add


def change_amount(df, row_id, money_amount) :
    df.loc[row_id, "Amount"] = money_amount

    
def get_net_worth(df) :
    return df["Amount"].sum()

    
def show_sorted_excel_data(df) :
    return df.sort_values(["Amount"], ascending=False)
    
    
def open_xlsx(excel) :
    df = pd.read_excel(excel)
    
    return df