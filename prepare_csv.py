import pyodbc 
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as psql
import numpy as py

def prepare_csv(date_from, date_to, country, markchan, marketingid):
    
    cnxn = pyodbc.connect("Driver={SQL Server};Server=;Database=;uid=;Trusted_Connection=yes;autocommit=False")
    cursor = cnxn.cursor()

    countryfil = country
    marketingid = str(marketingid)
    
    # The lines 16 - 30 are processing the list of marketing channels and returning a string ('channel1', 'n-channel',..,'channel2')that is used in SQL query below
    x=0
    i = int(len(markchan))-1

    while x <= i:
        if i == 0:
            marketingchannelf="(" + "'" + markchan[x] + "'" + ")"
            break
        elif x == 0:
            marketingchannels= "'" + markchan[x] + "', "
        elif (x > 1 and x < i):
            marketingchannels = marketingchannels + "'" + markchan[x] + "', "
        elif x == i:
            marketingchannelf ="(" + marketingchannels + "'" + markchan[x] + "')"
            break
        x=x+1

      
    sql = ("select FIELDS from PresentationLayer.dbo.CustomerAccountBase as AAA "
          "left join TABLE (NOLOCK) as XXX on AAA.FIELD1 = XXX.pFIELD1 "
          "where AAA.date > " + "'"+ date_from +"'"
          "and AAA.date < " + "'"+ date_to +"' "
          "and AAA.country = " + "'"+ countryfil +"' "
          "and XXX.marketingchannel in " + marketingchannelf 
          )
    
    cursor.close()
    df = psql.read_sql(sql, cnxn)

    df['searchkey'] = df['FIELD-A'].map(str) + df['FIELD-B'].map(str) + df['FIELD-C'].map(str)
    df=df[df['searchkey'].str.contains(marketingid)]
    
    return(df)
