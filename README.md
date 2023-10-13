---
title: conversational_uav_explorer
app_file: app.py
sdk: gradio
sdk_version: 3.35.2
---


-----------run --------------------

export OPENAI_API_KEY=sk-....B3d 
streamlit run app.py
	specify server_url where the cmd will be sent to.

server_url options:
	(1) simple http server @Robot:
		cd server; flask --app jackal_api.py run 
	(2) grpc signaling server robot.coldspringworks.com 
		see jackal_grpc.py

----------installation -------------------------

Ubuntu:
sudo apt install portaudio19-dev
sudo apt-get install python3-pyaudio
pip install -r requirements
	pip install streamlit-audiorecorder
sudo apt install ffmpeg

------------ 10/13/23 video test ----------------------------
python3 tools/chrome.py                                                       
    this generate url to access video for local machine test   

baal-pctt test link: (local)                                                           
  http://localhost:8080/?url=wss%3A%2F%2Flivekit.coldspringworks.com&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTc3Nzc4OTcsImlzcyI6ImRldmtleSIsIm5hbWUiOiJib3QiLCJuYmYiOjE2OTcxNzMwOTcsInN1YiI6ImJvdCIsInZpZGVvIjp7InJvb20iOiJyb29tLSIsInJvb21Kb2luIjp0cnVlfX0.bF0IEDsqav2FLr7xb5oBA0SGnlobfWI_zw4kaSD0h1w

------------ 10/13/23 grpc example  ----------------------------
get data from gprc server:
  Map
  Pose
api: jackal_grpc.py:
    #jackal_grpc_test()
    #jackal_grpc_goto()
    #jackal_grpc_get_poseasync()
    jackal_grpc_get_mapasync()
    #jackal_grpc_get_temperatureasync()
    #jackal_grpc_gotorel(x=0.5, rotation=-10)   

jackal_grpc.py
  device=device 
---------------10/3/23 grpc python code adding gotorel  -----
grpc btw client and device(server):
  client: SendTask(.. "goalrel")
  device: inteceptor created using "goalrel", RecvTask() will only tap to such message

need Tang to add goalrel.py rosnode

---------------10/3/23 grpc python code test  -----

streaming:
python jackal_grpc_client.py  --jwt_secret 123456 --function temperature:Temperature post
python jackal_grpc_client.py  --jwt_secret 123456 --function pose:Pose post
python jackal_grpc_client.py  --jwt_secret 123456 --function map:Map post

get one:
python jackal_grpc.py

---------------10/2/23 webrtc video stream -----
https://www.whitphx.info/posts/20211231-streamlit-webrtc-video-app-tutorial/
https://webrtc.streamlit.app/object_detection

