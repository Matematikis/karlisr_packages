
import pandas as pd
from datetime import datetime


def read_from_parquet(path):
    '''
    Read dataframe from parquet file
    :param str path: Path to the parquet file
    :return: Data table
    :rtype: Pandas dataframe
    '''
    timeBef = datetime.now()
    print("Read from parquet started at: " + str(timeBef))
    try:
        df = pd.read_parquet(path)
    except:
        print('Read data from parquet file failed: '+ path )
    timeAft = datetime.now()
    timeElapsed = timeAft - timeBef
    print("Elapsed Time: " + str(timeElapsed))
    return df