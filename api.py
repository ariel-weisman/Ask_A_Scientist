import mediacloud.api
import datetime
mc = mediacloud.api.MediaCloud('apikey')
start_date = datetime.date(2020,1,1)
end_date = datetime.date(2020,5,13)
date_range_2020 = mc.dates_as_query_clause(start_date, end_date)
my_query = '(COVID-19 or coronavirus or SARS-CoV-2 or covid) and tags_id_media:34412234'
results = mc.storyCount(my_query, date_range_2020, split=True, split_period='day')
results = results.pop('counts', None)
import pandas as pd
df = pd.DataFrame.from_dict(results)
df.to_csv (r'C:\Users\ariel\Downloads\Mediacloud Downloads\export_test.csv', index = False, header=True)