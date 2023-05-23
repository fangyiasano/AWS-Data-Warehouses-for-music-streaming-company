import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
     """
    It is used for dropping the tables
    
    Parameters: 
    cur:The object used to execute the sql statement
    conn: Objects used to connect redshift
    
    Returns: None
   
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
     """
    It is used for creating the tables
    
    Parameters: 
    cur:The object used to execute the sql statement
    conn: Objects used to connect redshift
    
    Returns: None
   
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    This is used for executing the functions of creating tables and deleting tables
    
    Parameters: None 
    
    Returns: None
   
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()