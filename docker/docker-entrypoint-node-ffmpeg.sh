# first start jsmpeg websocket
cd /jsmpeg
nohup node websocket-relay.js supersecret 8081 8082 &
sleep 1

# Then start video converter 
cd /jsmpeg
nohup ffmpeg -i rtsp://admin:qwer123456@192.168.0.6:554/h264/ch1/main/av_stream -q 0 -f mpegts -codec:v mpeg1video -s 1280x720 http://127.0.0.1:8081/supersecret &
sleep 1

# Then start http server
cd /jsmpeg
nohup http-server &
sleep 1

echo starting shell ...
/bin/bash
echo exited shell
