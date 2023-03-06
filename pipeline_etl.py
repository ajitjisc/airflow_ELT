import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime
import s3fs

def run_data_pipeline():
    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"

    payload = {
        'client_id': "89356",
        'client_secret': '572ec4d45cdae9b496013483c89e95efd9008c43',
        'refresh_token': '518dbf193e8dfc1d22c725ebf4585952f266920d',
        'grant_type': "refresh_token",
        'f': 'json'
    }

    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    print("Access Token = {}\n".format(access_token))

    header = {'Authorization': 'Bearer ' + access_token}

    param = {'per_page': 200, 'page': 1}
    page_num = 1
    all_activities =[]

    while True:

        param = {'per_page': 200, 'page': page_num}
        my_dataset = requests.get(activites_url, headers=header, params=param).json()
        print(len(my_dataset))
        if len(my_dataset) == 0:
            print("no more activities")
            break
        if all_activities:
            print("all activities populating")
            all_activities.extend(my_dataset)

        else:
            print('activities are not populated')
            all_activities = my_dataset
        page_num +=1

    activities = json_normalize(all_activities)
    #Create new dataframe with only columns I care about
    cols = ['name', 'type', 'distance', 'moving_time',   
            'average_speed', 'max_speed','total_elevation_gain',
            'start_date_local','average_heartrate'
        ]
    activities = activities[cols]

    #Break date into start time and date
    activities['start_date_local'] = pd.to_datetime(activities['start_date_local'])
    activities['start_time'] = activities['start_date_local'].dt.time
    activities['start_date_local'] = activities['start_date_local'].dt.date
    # Save as csv
    return activities.to_csv("s3://airflow-strava-pipeline-test/activities.csv", index= False)

if __name__ == '__main__':
    data= run_data_pipeline()

# # # Load back in
# activities = pd.read_csv('activities.csv')



