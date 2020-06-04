# my_lambdata/assigment.py

from pandas import DataFrame

# TODO? helper fnc from Assignment
# State abbreviation -> Full name and vice versa
# FL -> Florida, etc. 

def add_state_names_column(my_df):
    """
    Add a column of corresponding state names to a dataframe.

    Params (my_df) a DataFrame with a column called "abbrev" that has state abreviations.

    Return a copy of ther original  dataframe, but with an extra column.,
    """
    
    new_df = my_df.copy()
    
    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}

    new_df["name"] = new_df["abbrev"].map(names_map)
    
    return new_df
    

if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())
    
    mapped_df = add_state_names_column(df)
    print(mapped_df.head())
