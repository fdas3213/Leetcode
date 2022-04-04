class Logger:

    def __init__(self):
        #use a hashmap to store the message and its previous timestamp
        self.messageMap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        prevTime = self.messageMap.get(message, -1)
        
        if prevTime==-1 or timestamp-prevTime>=10:
            self.messageMap[message] = timestamp
            return True
        else:
            return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)