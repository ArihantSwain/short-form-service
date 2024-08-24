import os

import googleapiclient.discovery
import googleapiclient.errors
from pytubefix import YouTube
from pathlib import Path

# has letters is a method to check if a str has letters
def has_letters(entered_string):
    for x in entered_string:
        if x.isalpha():
            return True
    return False


# create YOUTUBE API call service
api_service_name = "youtube"
api_service_version = "v3"
DEVELOPER_KEY = ""  # ENTER API CREDENTIALS KEY HERE
youtube = googleapiclient.discovery.build(api_service_name, api_service_version, developerKey=DEVELOPER_KEY)
path = os.getcwd()
print(os.getcwd())
if os.path.isfile(path + '/video_clips_download'):
    os.mkdir('video_clips_download')

final_path = path + "/video_clips_download"
print(final_path)

# initially prompt for a url -- need to create a URL verifier
video_url = input("Enter a video url: ")
number_of_clips = input("Enter a number of clips to create: ")

# on input of this, run code to download video for future use
video_download = YouTube(video_url)

raw_value_download = video_download.streams.get_highest_resolution()
raw_value_download.download(output_path=final_path)
print("downloaded video")

# extract video_id from video_url
video_id = video_url[-11:]

# comb through comments and make a list of comment ids based on number of appearances
request = youtube.commentThreads().list(part="snippet,replies", videoId=video_id, maxResults=100)
response = request.execute()
valid = response
int_response_list = valid.get('items')
comment_outer = []
comment_secondary = []
comment_tertiary = []
comment_final = []
timestamps = []
timestamps_culled = []

# the response given is a dictionary of lists of dictionaries, which when keyed, also leads to another set
# of dictionaries. these dictionaries are nested heavily, the code below retrieves comments from this nested
# format, thus allowing us to gather the necessary timestamps.
for i in int_response_list:
    comment_outer.append(i.get('snippet'))

for i in comment_outer:
    comment_secondary.append(i.get('topLevelComment'))

for i in comment_secondary:
    comment_tertiary.append(i.get('snippet'))

for i in comment_tertiary:
    comment_final.append(i.get('textDisplay'))

for i in comment_final:
    if ">" in i:
        print(i)
        new_string = i.split('>', 1)
        final_string = new_string[1].split('<', 1)
        timestamps.append(final_string[0])

for i in timestamps:
    if i != "" and has_letters(i) is False:
        timestamps_culled.append(i)

print(timestamps_culled)