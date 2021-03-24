from datetime import timedelta, date
import os
import pandas
from facebookads.adobjects.adaccount import AdAccount
from facebookads.api import FacebookAdsApi
import time
import numpy as np
import json

# from facebookads.adobjects.adsinsights import AdsInsights
##

##Set working dir
os.chdir('/home/i-sip_iot/PycharmProjects/ETL_DataIngestion/Free_Data_Resources/facebook')

##Static parameters got from Facebook App
secrets = json.loads(open('../../../facebook_app_credential.json', 'r').read())
my_app_id = secrets['auth']['api_id']
my_app_secret = secrets['auth']['api_secret']
my_access_token = secrets['auth']['access_token']
# proxies = {'http': '<HTTP_PROXY>', 'https': '<HTTPS_PROXY>'} # add proxies if needed
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)


## iterates through an array of dates
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


## the end date will always be today
today = date.today()
end_date = today
print(end_date)

## start date
deltaMonth = timedelta(days=-30)
start_date = today + deltaMonth
print("Will get data from " + start_date.strftime("%Y-%m-%d") + "to" + end_date.strftime("%Y-%m-%d"))

## create a dataframe
dataFrame = pandas.DataFrame()

## facebook's fields to get
# Documentation > https://developers.facebook.com/docs/marketing-api/reference/ads-insights

fields = [
    'ad_name',
    'adset_name',
    'campaign_name',
    'date_start',
    'date_stop',
    'spend',
    'impressions',
    'unique_clicks',
    'clicks',
    'actions',
]

## creating a counter so I can stop the requests not to be kicked
counter = 1

# iterates through date to get the result
print("Starting to get data ....")
for single_date in daterange(start_date, end_date):

    ## gets D - 1 for single_date
    single_date_less = single_date

    ## transforms dates in strings for facebook's api
    start = single_date_less.strftime("%Y-%m-%d")
    end = single_date.strftime("%Y-%m-%d")

    ##sets the starting date and ending date as params for fb
    params = {
        'level': 'ad',
        'filtering': [{'field': 'impressions', 'operator': 'GREATER_THAN', 'value': '0'}],
        'time_range': {'since': end, 'until': end},
    }

    ## if the counter is divisible by 20, this variable is true
    sleep = False

    if (counter % 20 == 0):
        sleep = True

    ## sleeps for 305 sec to not be kicked
    if (sleep == True):
        print("Sleeping for 305 seconds")
        time.sleep(305)
        print("Continuing to get data")

    # requests the data
    responses = AdAccount(ad_account_id).get_insights(fields=fields, params=params, )

    ## adds one to the sleep counter
    counter = counter + 1

    ## iterates through the array of responses
    result = [x for x in responses]

    ## creates the dataframe all data
    resultDataFrame = pandas.DataFrame(result)
    isNone = resultDataFrame.empty

    if (isNone == True):
        continue

    ##creates a dataframe with actions results
    dfActions = resultDataFrame['actions']

    ##creates a list to iterate over
    purchaseList = list()

    ##parses the JSON looking for the actions "purchase"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("purchase")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            purchaseList.append(p)
        else:
            purchaseList.append(0)
    ##creates a list to iterate over
    leadList = list()

    ##parses the JSON looking for the actions "leads"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("lead")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
                p = int(w)
                leadList.append(p)
        else:
            leadList.append(0)

    ##creates a list to iterate over
    entrouList = list()

    ##parses the JSON looking for the actions "xx"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("xx")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            entrouList.append(p)
        else:
            entrouList.append(0)

    ##creates a list to iterate over
    cnpjPositivoList = list()

    ##parses the JSON looking for the actions "yy"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("yy")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            cnpjPositivoList.append(p)
        else:
            cnpjPositivoList.append(0)

    ##creates a list to iterate over
    cadastroAbrirList = list()

    ##parses the JSON looking for the actions "zz"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("zz")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            cadastroAbrirList.append(p)
        else:
            cadastroAbrirList.append(0)

    ##creates a list to iterate over
    iniciouMGList = list()

    ##parses the JSON looking for the actions "pp"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("pp")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            iniciouMGList.append(p)
        else:
            iniciouMGList.append(0)

    ##creates a list to iterate over
    iniciouABList = list()

    ##parses the JSON looking for the actions "uu"
    for x in dfActions:
        y = str(x)
        purchaseNum = y.find("uu")
        if (purchaseNum != -1):
            z = y.find("}", purchaseNum)
            w = y[z - 3:z - 1]
            if (w.find("\'") != -1):
                w = w[1:2]
            p = int(w)
            iniciouABList.append(p)
        else:
            iniciouABList.append(0)

    ## transforms the lists into arrays
    ##Creates dataframes
    purchasesDataFrame = pandas.DataFrame(np.array(purchaseList))
    leadsDataFrame = pandas.DataFrame(np.array(leadList))
    entrouDataFrame = pandas.DataFrame(np.array(entrouList))
    cnpjPositivoDataFrame = pandas.DataFrame(np.array(cnpjPositivoList))
    cadastroAbrirDataFrame = pandas.DataFrame(np.array(cadastroAbrirList))
    iniciouMGDataFrame = pandas.DataFrame(np.array(iniciouMGList))
    iniciouABDataFrame = pandas.DataFrame(np.array(iniciouABList))

    purchasesDataFrame.columns = ['purchases']
    leadsDataFrame.columns = ['leads']
    entrouDataFrame.columns = ['entrou_HB']
    cnpjPositivoDataFrame.columns = ['cnpj_Positivo']
    cadastroAbrirDataFrame.columns = ['cadastro_Abrir']
    iniciouMGDataFrame.columns = ['iniciou_MG']
    iniciouABDataFrame.columns = ['iniciou_AB']

    # joins dataframes
    result = resultDataFrame.join(purchasesDataFrame)
    result = result.join(leadsDataFrame)
    result = result.join(entrouDataFrame)
    result = result.join(cnpjPositivoDataFrame)
    result = result.join(cadastroAbrirDataFrame)
    result = result.join(iniciouMGDataFrame)
    result = result.join(iniciouABDataFrame)

    ## creates a file with the date name
    filename = ("facebook-data-" + end + ".csv")
    file = open(filename, 'w', encoding='utf-8')
    ## creates a dataset and writes a csv with it
    result.to_csv(file, sep='\t', encoding='utf-8')
    print("    - " + filename)

print("Sucess!")

# import requests
#
# access_token = "EAAHSpPtSzIABALptC6h7sDXu2j6ZAZCe0VdTZBSlkBZBVbzVGCKGLo0hqGWlCZBdFpPHYxbxnJpc96uXtNHugaUIZAlecU3h2yObSxeGatVd5ZChVQMb7ZAXAf1CmHaZA6tbYIQWY5BUOaOmL8BAjAHMMrtNmVUBJSZA5qyaSmRcUNZBM499fU5DXr025zdv9apNZBwRdXO5eoFmZBU3TYHV8YIrMEEwZAnxDlkl9LbmZBiZBJThmQZDZD"
#
#
# def get_json_response(url, access_token):
#     headers = {"Authorization": "Bearer {}".format(access_token)}
#     response = requests.request("GET", url, headers=headers)
#     if response.status_code != 200:
#         raise Exception(response.status_code, response.text)
#     return response.json()
#
# url_ = "https://graph.facebook.com/v8.0/ads_archive?ad_reached_countries=['US', 'IN', 'BR']&search_page_ids=[338109312883186,300653326696613]&fields=['id',‘impressions’,‘region_distribution’]"
# print(get_json_response(url_, access_token))
#
#
# import pandas as pd
# url = url_ #From parts (b) through (d)
# response = get_json_response(url) #We wrote this above
# data = response['data']
#
# #Make an empty Pandas dataframe, append new data onto it.
# ads_df = pd.DataFrame()
# while len(data) > 0: #until the next page of data is empty
#     ads_df = ads_df.append(data)
#     url = response['paging']['next']
#     response = get_json_response(url)
#     data = response['data']
# ads_df = ads_df.reset_index(drop=True) #avoid funky indexing issues