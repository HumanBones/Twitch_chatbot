import re
import socket
import json

class ChatBot():
    massage = "" 

    def __init__(self):
        with open('settings.json') as jsonfile:
            data = jsonfile.read()

        obj = json.loads(data)
        #print(obj)
        BOT =  obj["username"]
        CHANNEL  = obj["channel"]
        TOKEN = obj["oauth"]
        SERVER  = obj["server"]
        PORT  = obj["port"]
        s_prep = socket.socket()
        s_prep.connect((SERVER, PORT))
        s_prep.send(("PASS " + TOKEN + "\r\n").encode())
        s_prep.send(("NICK " + BOT + "\r\n").encode())
        s_prep.send(("JOIN #" + CHANNEL + "\r\n").encode())
        self.joinchat(s_prep, CHANNEL)
        readbuffer = ""
    
    def getMessage(slef,line):
        try:
            message = (line.split(":", 2))[2]
        except:
            message = ""
        return message

    def getUser(self,line):
        separate = line.split(":", 2)
        user = separate[1].split("!", 1)[0]
        return user


    def Console(self,line):
        if "PRIVMSG" in line:
            return False
        else:
            return True

    def sendMessage(self, s,channel, message):
        messageTemp = "PRIVMSG #" + channel +" :" + message
        s.send((messageTemp + "\r\n").encode())

    def joinchat(self,s,name):
        readbuffer_join = "".encode()
        Loading = True
        while Loading:
            readbuffer_join = s.recv(1024)
            readbuffer_join = readbuffer_join.decode()
            temp = readbuffer_join.split("\n")
            readbuffer_join = readbuffer_join.encode()
            readbuffer_join = temp.pop()
            for line in temp:
                if ("End of /NAMES list" in line):
                    print("Bot has joinde " + name + " channel!")
                    self.sendMessage(s,name,"CHAT JOINED!")
                    break
                elif line == "":
                    print("CONNECTION LOST!")
                    break

                if "PING" in line and self.Console(line): #if user typs in chat PING, Console is for detecting if its the server or user
                    msgg = "PONG tmi.twtich.tv\r\n".encode()
                    s.send(msgg)
                    print(msgg)
                    break 
                
                user = self.getUser(line)
                message = self.getMessage(line)
                chat_message = user + " > " + message
                print(chat_message)
                PMSG = "/w" + user + " "
                if "!global" in message:
                    self.sendMessage(s, name,"This is a global message!")
                    break
                if "!private" in message:
                    self.sendMessage(s,PMSG,"This is a private msg!")
                    break

if __name__ == "__main__":
    ChatBot().start()