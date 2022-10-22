class Book:
    def __init__(self,bname):
        self.bname = bname

    def set_bname(self, bname):
        self.bname = bname.upper()          # here, it will set data to upper case and data will return using get method

    def get_bname(self):
        return(self.bname)

ob = Book('Maths')                          #it simply set data to bname variable
print(ob.get_bname())

ob.set_bname('Physics')                     #it set data in uppercase to bname variable
print(ob.get_bname())