
import pandas as pd
from datetime import datetime

def read_from_sql(sql,conn):
    '''
    Read dataframe from sql database
    :param str sql: SQL command to read data
    :return: Data table
    :rtype: Pandas dataframe
    '''
    timeBef = datetime.now()
    print("Read from sql started at: " + str(timeBef))
    try:
        df = pd.read_sql(sql,conn)
    except:
        print('Read data from sql failed: '+ sql )
    timeAft = datetime.now()
    timeElapsed = timeAft - timeBef
    print("Elapsed Time: " + str(timeElapsed))
    return df
