import boto3
import json
import pandas as pd

    
def donwload(client, start, end, group, folder_download, subfijo):
    
    metric = 'BlendedCost'

    response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start,
        'End': end
    },

    Granularity='DAILY',

    Metrics=['BlendedCost'],

    GroupBy=group
    )
    
    response = response['ResultsByTime']
    
    i = 0
    list_df = []
    while True:
        try:
            df = pd.json_normalize(response[i]['Groups'])
            timestart = response[i]['TimePeriod']['Start']
            timeend = response[i]['TimePeriod']['End']
            df["Period_start"] = timestart
            df["Period_end"] = timeend

            df = df.rename(columns={'Keys': 'Service',
                                    'Metrics.BlendedCost.Amount': 'Amount',
                                    'Metrics.BlendedCost.Unit': 'CurrencyCode',})
            
            df['Amount'] = df['Amount'].astype(float)
            
            i = i + 1
            
            list_df.append(df)
            
        except IndexError:
            break
    
    result = pd.concat(list_df)
    dic = result.to_dict(orient='records')
    
    namefile = subfijo + start + '.json'

    jsonfile = open(folder_download + namefile, 'w')
    
    for row in dic:
        json.dump(row, jsonfile)
        jsonfile.write('\n')
    jsonfile.close()