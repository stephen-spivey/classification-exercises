import pandas as pd
import numpy as np
import os
import env


directory = os.getcwd()

def get_connection_url(db, username=env.username, host=env.host, password=env.password):
    """
    This function will:
    - take username, pswd, host credentials from imported env module
    - output a formatted connection_url to access mySQL db
    """
    return f'mysql+pymysql://{username}:{password}@{host}/{db}'


def new_titanic_data(SQL_query):
    """
    This function will:
    - take in the SQL query
    - create connection_url to mySQL
    - return a df off of the query from the titanic_db
    """
    url = get_connection_url('titanic_db')
    
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

    

def new_iris_data():
    '''
    This function reads the iris data from the Codeup db into a df.
    '''
    sql_query = """
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
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection_url('iris_db'))
    
    return df


def get_iris_data():
    '''
    This function reads in iris data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a df.
    '''
    if os.path.isfile('iris_df.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('iris_df.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_iris_data()
        
        # Cache data
        df.to_csv('iris_df.csv')
        
    return df


def new_telco_data(SQL_query):
    """
    This function will:
    - take in a SQL_query
    - create a connection_url to mySQL
    - return a df of the given query from the telco_db
    """
    url = get_connection_url('telco_churn')
    
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