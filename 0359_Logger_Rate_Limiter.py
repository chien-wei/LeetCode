class Logger:
    def __init__(self):
        self.last_seen = {}

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.last_seen or timestamp - self.last_seen[message] >= 10:
            self.last_seen[message] = timestamp
            return True
        return False

logger = Logger()
print(logger.shouldPrintMessage(1, "foo"))
print(logger.shouldPrintMessage(2, "bar"))
print(logger.shouldPrintMessage(3, "foo"))
print(logger.shouldPrintMessage(8, "bar"))
print(logger.shouldPrintMessage(10, "foo"))
print(logger.shouldPrintMessage(11, "foo"))