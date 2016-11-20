class Secretive:
    def __inaccessible(self):
        print "Bet you cant see me"
    def accessible(self):
        print "the secret message is:"
        self.__inaccessible()

S = Secretive()
S.accessible()
S.__inaccessible()
