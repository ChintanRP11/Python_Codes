class Book:
    def __init__(self,bname, pvname):
        self._bname = bname
        self.__pvname = pvname

    def set_bname(self, bname):
        self._bname = bname.upper()          # here, it will set data to upper case and data will return using get method
    
    def get_bname(self):
        return(self._bname)


    def set_pvname(self, pvname):
        self.__pvname = pvname.lower()

    def get_pvname(self):
        return(self.__pvname)

    
    

ob = Book('Maths', 'PRIvate')                          #it simply set data to bname variable
print(ob.get_bname())
print(ob._bname)

ob.set_bname("Science")
print(ob.get_bname())
print(ob._bname)

ob.set_pvname("TESTprivate")    # this set method allows us to change private members of class
# print(ob.__pvname)              # it gives an error because it is private member and we cannot directly access it.
print(ob.get_pvname())          # this get method allows us to access private members of class.


ob.set_bname('Physics')                     #it set data in uppercase to bname variable
print(ob.get_bname())