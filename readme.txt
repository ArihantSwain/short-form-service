For use:

Simply input a video from youtube, select a number of clips (max of 99), and select a folder for files
to flow into. By doing so, the folder will be populated with minute-long clips starting at 5 seconds before
a comment's stated time. As such, if a commenter explicitly notes 10:05 as a funny moment, the program will go
from 10:00 to 11:00 and clip it as such. Further implementation will allow custom timing.

Before use, please enter an API Key within main.py at line 7:

ex:

api_service_name = "youtube"
api_service_version = "v3"
DEVELOPER_KEY = "D25joijDx-1123"
youtube = googleapiclient.discovery.build(api_service_name, api_service_version, developerKey = DEVELOPER_KEY)
