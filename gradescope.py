import pandas as pd

def get_list_of_TAs(roster):
    df = pd.read_excel(roster, header = 2).dropna()
    df[['Last Name', 'First Name']] = df.Name.str.split(", ", expand = True)
    return df

df = get_list_of_TAs("roster.xlsx")
print(df)