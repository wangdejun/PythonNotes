class Human(object):
    laugh = 'hahaha'
    def show_laugh(self):
        print self.laugh
    def laugh_100th(self):
        for i in range(100):
            print i,
            self.show_laugh()

li_lei = Human()
li_lei.laugh_100th()
