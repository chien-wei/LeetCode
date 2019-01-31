import string
import random
class Codec:
    def __init__(self):
        self.en = {}
        self.de = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        en = self.en
        de = self.de
        if longUrl in en:
            return en[longUrl]
        else:
            rand = random.choice(string.ascii_letters)
            while rand in en:
                rand += random.choice(string.ascii_letters)
            en[longUrl] = rand
            de[rand] = longUrl
            return rand

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        en = self.en
        de = self.de
        if shortUrl in de:
            return de[shortUrl]
        else:
            return None
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))