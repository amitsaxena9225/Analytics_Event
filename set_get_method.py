import requests

payload ={"data":{
 "sid":"preintegration6",
 "start_ts":1556675000,
 "user_agent":"postman",
 "uuid":"preintegration",
 "widget_id":"02",
 "widget_url":"https://preintegration.com/widget05.html",
 "isManual":"false",
  "event_name":"CLICK",
 "video_type":"ad",
"video_id":"5c6da0e8d21619a9431ed2ce",
"label":"VIDEOPLAY"
}}

var = requests.post("https://dev-api.yupl.us/engagement/track",data=payload)

print(var.status_code)