import googleapiclient.discovery
import googleapiclient.errors
import ffmpeg
import os
from pytube import YouTube


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

# initially prompt for a url -- need to create a URL verifier
video_url = input("Enter a video url: ")
number_of_clips = input("Enter a number of clips to create: ")
duration_front = input("Enter the size of the clip prior to the timestamp in seconds: ")
duration_back = input("Enter the size of the clip after the timestamp in seconds: ")

# change directory of files
abspath = os.path.abspath("main.py")
dirname = os.path.dirname(abspath)
os.chdir(dirname + "/videos/")

# download video from URL to use to trim clips later
download = YouTube(video_url)
download.streams\
    .filter(type="video", file_extension="mp4")\
    .order_by()\
    .desc()\
    .first()\
    .download(filename_prefix="original_video")

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

