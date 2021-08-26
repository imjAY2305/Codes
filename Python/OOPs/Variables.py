class Sample:
    wheels = 4 #Changes are effected everywhere
    def __init__(self,mil=0,com="NONE"):
        #Changes are object dependent
        self .mil = mil
        self.com = com
    def __set__(self):
        print(self.mil)

s1 = Sample()