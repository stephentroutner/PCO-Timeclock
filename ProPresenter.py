from websocket import create_connection
ws = create_connection("ws://vp-graphics1.local:49752/remote")
print("Sending request")
ws.send('{"action":"authenticate","protocol":"700","password":"timeclock"}')
print("Sent")
print("Authenticating...")
result =  ws.recv()
print("Received '%s'" % result)
ws.send('{ "action":"presentationCurrent", "presentationSlideQuality": 25}')
print("Sent")
print("Receiving...")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()