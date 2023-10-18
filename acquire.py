import pandas as pd
from pydataset import data
import env
import os

# 1. Make a function named get_titanic_data that returns the Titanic data from the codeup data science database as a pandas data frame. Obtain your data from the Codeup Data Science Database.

def new_titanic_data(SQL_query):
    """
    This function will:
    - take in the SQL query
    - create connection_url to mySQL
    - return a df off of the query from the titanic_db
    """
    url = get_db_url('titanic_db')
    
    return pd.read_sql(SQL_query, url)


def get_titanic_data(SQL_query, directory, filename = 'titanic.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return csv if exists
    - if csv doesn't exist:
        - creates df from sql query
        - write df to csv
    - outputs titanic df
    """
    if os.path.exists(directory+filename):
        df = pd.read_csv(filename)
        return df
    else:
        df = new_titanic_data(SQL_query)
        df.to_csv(filename)
        return df

titanic_query = "SELECT * FROM passengers"
directory = os.getcwd()

titanic_df = get_titanic_data(titanic_query, directory)

titanic_df.head()


# 2. Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the species_ids. Obtain your data from the Codeup Data Science Database.

def new_iris_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the iris_db
    """
    url = get_db_url('iris_db')
    
    return pd.read_sql(SQL_query, url)


def get_iris_data(SQL_query, directory, filename = 'iris.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv
    - outputs iris df
    """
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_iris_data(SQL_query)

        df.to_csv(filename)
        return df
    
    
iris_query = """
            SELECT 
                species_id,
                species_name,
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            FROM measurements
            JOIN species USING(species_id)            
"""

iris_df = get_iris_data(iris_query, directory)
iris_df.head()
    
    
# 3. Make a function named get_telco_data that returns the data from the telco_churn database in SQL. In your SQL, be sure to join contract_types, internet_service_types, payment_types tables with the customers table, so that the resulting dataframe contains all the contract, payment, and internet service options. Obtain your data from the Codeup Data Science Database.

def new_telco_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the telco_db
    """
    url = get_db_url('telco_churn')
    
    return pd.read_sql(SQL_query, url)

def get_telco_data(SQL_query, directory, filename = 'telco.csv'):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - if csv doesn't exist:
        - creates df of sql query
        - writes df to csv
    - outputs telco df
    """
    if os.path.exists(directory+filename): 
        df = pd.read_csv(filename)
        return df
    else:
        df = new_telco_data(SQL_query)

        df.to_csv(filename)
        return df
    
telco_query = """
        SELECT * FROM customers
        JOIN contract_types USING (contract_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN payment_types USING (payment_type_id)
        """

telco_df = get_telco_data(telco_query, directory)
telco_df.head()

# 4. Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for the local filename of telco.csv, titanic.csv, or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.