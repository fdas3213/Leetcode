class Logger:

    def __init__(self):
        self.messageMap = defaultdict(int)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.messageMap:
            self.messageMap[message] = timestamp
            return True
        else:
            if timestamp-self.messageMap[message]<10:
                return False
            #update the timestamp for the incoming message
            self.messageMap[message]=timestamp
            return True
    


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)