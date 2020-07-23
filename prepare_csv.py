import pyodbc 
import pandas as pd
from pandas import DataFrame
import pandas.io.sql as psql
import numpy as py

def prepare_csv(date_from, date_to, country, markchan, marketingid):
    
    cnxn = pyodbc.connect("Driver={SQL Server};Server=SC1WNPRNDB003\\DPE_PROD;Database=PresentationLayer;uid=WHGROUP\pkatidis;Trusted_Connection=yes;autocommit=False")
    cursor = cnxn.cursor()

    countryfil = country
    marketingid = str(marketingid)
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

    sql = ("select cab.RegistrationDt, cab.CustomerAccountNumber, cab.username, cou.Countrynm, (case when pla.platformnm <> 'Mobile' then 'Desktop' else 'Mobile' end) as Device, mac.MarketingChannelNm,"
          " cab.RegistrationTrackingAccountCd, cab.RegistrationTrackingAdCreativeCd, cab.RegistrationTrackingAdSetCd, cab.RegistrationTrackingCampaignCd, cab.RegistrationTrackingCdBtag,"
          " (case when cab.FirstDepositAmount > 0 THEN 'Y' ELSE 'NO' END) as FD from PresentationLayer.dbo.CustomerAccountBase as cab "
          "left join PresentationLayer.dbo.ProductSource (NOLOCK) as psc on cab.registrationproductsourceid = psc.productsourceid "
          "left join PresentationLayer.dbo.MarketingChannel (NOLOCK) as mac on cab.RegistrationMarketingChannelId = mac.MarketingChannelId "
          "left join PresentationLayer.dbo.country (NOLOCK) as cou on cab.RegistrationCountryId = cou.CountryId "
          "left join PresentationLayer.dbo.Platform (NOLOCK) as pla on cab.RegistrationPlatformId = pla.PlatformId "
          "where cab.RegistrationDt > " + "'"+ date_from +"'"
          "and cab.RegistrationDt < " + "'"+ date_to +"' "
          "and (CASE WHEN cou.CountryNm = 'United Kingdom' THEN 'uk' WHEN cou.CountryNm = 'Spain' THEN 'es' WHEN cou.CountryNm = 'it' THEN 'IT' ELSE 'row' END) = " + "'"+ countryfil +"' "
          "and mac.MarketingChannelNm in " + marketingchannelf 
          )
    
    cursor.close()
    uno = psql.read_sql(sql, cnxn)

    uno['searchkey'] = uno['RegistrationTrackingAccountCd'].map(str) + uno['RegistrationTrackingAdCreativeCd'].map(str) + uno['RegistrationTrackingAdSetCd'].map(str) + uno['RegistrationTrackingCampaignCd'].map(str) + uno['RegistrationTrackingCdBtag'].map(str)
    uno=uno[uno['searchkey'].str.contains(marketingid)]
    print(uno)

    return(uno)