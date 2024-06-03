import googleapiclient.discovery
import googleapiclient.errors

# create YOUTUBE API call service
api_service_name = "youtube"
api_service_version = "v3"
DEVELOPER_KEY = "AIzaSyB7yXvkAnhNmRcx-QUGkHWtzZU6QVjcy7g"
youtube = googleapiclient.discovery.build(api_service_name, api_service_version, developerKey = DEVELOPER_KEY)

# initially prompt for a url -- need to create a URL verifier
video_url = input("Enter a video url: ")
number_of_clips = input("Enter a number of clips to create: ")

# extract video_id from video_url
video_id = video_url[-11:]

# comb through comments and make a list of comment ids based on number of appearances
request = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=100)
response = request.execute()
print(response)