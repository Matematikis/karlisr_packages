
import pandas as pd
from datetime import datetime


def save_as_parquet(df, path):
    '''
    Save dataframe as a parquet file
    :param str path: Path for the parquet file
    :param pandas dataframe df: Dataframe to save
    '''
    timeBef = datetime.now()
    print("Save as parquet started at: " + str(timeBef))
    try:
        df.to_parquet(path, compression='gzip')
    except:
        print('Save data as parquet file failed: '+ path )
    timeAft = datetime.now()
    timeElapsed = timeAft - timeBef
    print("Elapsed Time: " + str(timeElapsed))

