import pandas as pd

GRADING_MIN = 11

def get_list_of_TAs(roster):
    df = pd.read_excel(roster, header = 2).dropna()
    df[['Last Name', 'First Name']] = df.Name.str.split(", ", expand = True)
    df['Full Name'] = df['First Name'].apply(lambda x: x + ' ') + df['Last Name']
    df['Done Grading'] = False
    return df

def search_html_for_TA(html, df):
    with open(html, 'r') as file:
        content = file.read()

    for index, name in df['Full Name'].iteritems():
        count = content.count(name)
        if count >= GRADING_MIN: 
            df.loc[df['Full Name'] == name, 'Done Grading'] = True        

def get_emails(df):
    name_array = ', '.join(df.loc[df['Done Grading'] == False]["Email"].to_list())
    print(f"[{name_array}]")

df = get_list_of_TAs("roster.xlsx")
search_html_for_TA('html_elem.txt', df)
get_emails(df)
