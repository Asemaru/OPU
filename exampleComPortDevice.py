from ComPortClient import ComPort

port = "COM1"


client = ComPort()
client.Connect(port, 9600)

def requestProcessing(request:str):

    if("*IDN?" in request):
        responce = "I am server on port " + str(port)
        return responce + "\n"
    
    if("exit" in request):
        responce = "Poka!"
        return responce + "\n"

    else:
        responce = "ERROR"
        return responce + "\n"
    

if(client.Connected):
    while True:
        readMessage = client.ReceiveStr()
        sendMessage = ""
        try:
            sendMessage = requestProcessing(readMessage)
        except:
            print("Error!!!")
        finally:
            client.Send(sendMessage)
    