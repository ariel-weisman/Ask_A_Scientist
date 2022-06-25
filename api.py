import mediacloud.api
import datetime
import pandas as pd
import config

mc = mediacloud.api.MediaCloud(config.my_API_key)

#dates selected based on start and end dates of the Ask a Scientist (AAS) Project
start_date = datetime.date(2020,1,1)
end_date = datetime.date(2020,5,13)
AAS_date_range = mc.dates_as_query_clause(start_date, end_date)

with open("C:\\Users\\ariel\\Documents\\python_projects\\ask_a_scientist\\keywords.txt", "r") as keywords_file:
    keyword_list = keywords_file.read().splitlines() 

#media tag is for MediaCloud's US-National collection of sources
for keyword in keyword_list:
    counts_by_date = mc.storyCount(f"(COVID or coronavirus or SARS-CoV-2 or COVID-19) and {keyword} and tags_id_media:34412234", AAS_date_range, split=True, split_period='day')
    df_results = pd.DataFrame(counts_by_date["counts"])
    df_results.to_csv (f"C:/Users/ariel/Documents/python_projects/ask_a_scientist/{keyword}.csv", index = False, header=True)

total_counts = mc.storyCount("tags_id_media:34412234",AAS_date_range,split = True,split_period = 'day')
df_total_results = pd.DataFrame(total_counts["counts"])
df_total_results.to_csv("C:/Users/ariel/Documents/python_projects/ask_a_scientist/total_stories.csv", index = False, header=True)