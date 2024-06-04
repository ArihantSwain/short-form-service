import googleapiclient.discovery
import googleapiclient.errors

# create YOUTUBE API call service
api_service_name = "youtube"
api_service_version = "v3"
DEVELOPER_KEY = "AIzaSyDZplUSKPY_WyGCoYShjCHAykfA6-EBQtY" # ENTER API CREDENTIALS KEY HERE
youtube = googleapiclient.discovery.build(api_service_name, api_service_version, developerKey = DEVELOPER_KEY)

# initially prompt for a url -- need to create a URL verifier
video_url = input("Enter a video url: ")
number_of_clips = input("Enter a number of clips to create: ")

# extract video_id from video_url
video_id = video_url[-11:]

# comb through comments and make a list of comment ids based on number of appearances
request = youtube.commentThreads().list(part="snippet,replies", videoId=video_id, maxResults=100)
response = request.execute()
valid = response
commentlist = []

print(valid.items())

for x in range(4):
    valid.pop(valid.items().get(x))

print(valid)
count = 0
for x in range(5):
    print(valid.get(x))
    if x[0] != "items":
        valid.pop(x)
