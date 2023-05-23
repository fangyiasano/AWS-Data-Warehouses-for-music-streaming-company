import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    We load the data from S3 to staging tables at Redshift
    
    Parameters: 
    cur:The object used to execute the sql statement
    conn: Objects used to connect redshift
    
    Returns: None
   
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert data from staging tabls into the fact and demension tables we created at Redshift
    
    Parameters: 
    cur:The object used to execute the sql statement
    conn: Objects used to connect redshift
    
    Returns: None
   
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Execute the entire ETL process
    
    Parameters: None 
    
    Returns: None
   
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()