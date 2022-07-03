import logging


class stringz:
    def __init__(self,s):
        import logging
        logging.basicConfig(filename='stringz.log', level=10, format='%(levelname)s : %(asctime)s : %(name)s : %(message)s')
        logging.info('strings module imported')
        self.s = s

    def extract_jump(self,n1,n2,n3):
        try:
            logging.info("success in extract_jump - %s",self.s[n1:n2:n3])
            return self.s[n1:n2:n3]
        except Exception as e:
            logging.exception(e)

    def extract(self,n1,n2):
        try:
            logging.info("success in extract - %s",self.s[n1:n2])
            return self.s[n1:n2:1]
        except Exception as e:
            logging.exception(e)

    def reverse(self):
        try:
            logging.info("success in reverse - %s",self.s[-1:-(l+1):-1])
            l = len(self.s)
            return self.s[-1:-(l+1):-1]
        except Exception as e:
            logging.exception(e)

    def upp(self):
        try:
            logging.info("success in upp - %s",self.s.upper())
            return self.s.upper()
        except Exception as e:
            logging.exception(e)

    def loww(self):
        try:
            logging.info("success in loww - %s",self.s.lower())
            return self.s.lower()
        except Exception as e:
            logging.exception(e)

    def splitt(self,x):
        try:
            logging.info("success in splitt - %s",self.s.split())
            return self.s.split(str(x))
        except Exception as e:
            logging.exception(e)

    def capp(self):
        try:
            logging.info("success in capp - %s",self.s.capitalize())
            return self.s.capitalize()
        except Exception as e:
            logging.exception(e)

    def exptab(self):
        try:
            logging.info("success in exptab - %s",self.s.expandtabs())
            return self.s.expandtabs()
        except Exception as e:
            logging.exception(e)

    def stripp(self,x):
        try:
            logging.info("trying stripp")
            if x == 'l':
                logging.info("x == 'l' found")
                return self.s.lstrip()
            elif x == 'r':
                logging.info("x == 'r' found")
                return self.s.rsrtip()
            elif x == 's':
                logging.info("x == 's' found")
                return self.s.strip()
            else:
                logging.info("incorrect input!")
        except Exception as e:
            logging.exception(e)

    def replacee(self,x,y):
        try:
            logging.info("trying replacee")
            return self.s.replace(x,y)
        except Exception as e:
            logging.exception(e)

    def cent(self,x,y):
        try:
            logging.info("trying cent")
            return self.s.center(x,str(y))
        except Exception as e:
            logging.exception(e)

def search(ll,x):
    for i in ll:
        if type(i) == list:
            search(i,x)
        elif type(i) == tuple:
            try:
                i.index(x)
                print(i,x)
            except ValueError as e:
                print(e)
        else:
            if i == x:
                print(i,x)
            else:
                print('does not exists!')
                break
def listtilllast(ll):
    for i in ll:
        if type(i) == list:
            listtilllast(i)
        else:
            if i.isnumeric():
                print(i)

def tupletilllast(ll):
    for i in ll:
        if type(i) == tuple:
            tupletilllast(i)
        else:
            if i.isnumeric():
                print(i)

def onlydict(ll):
    for i in ll:
        if type(i) == dict:
            print(i.items())
            for key, val in i.items():
                if (type(key) == int):
                    print(key)
                if type(val) == int:
                    print(val)
def onlysets(ll):
    for i in ll:
        if type(i) == set:
            onlysets(i)
        else:
            if i.isnumeric():
                print(i)

class lisst:
    def __init__(self,l):
        import logging
        logging.basicConfig(filename="lisst.log", level=10, format='%(levelname)s : %(asctime)s : %(name)s : %(message)s')
        logging.info("lisst module imported")
        self.l = l

    def onlynumeric(self):
        try:
            logging.info("accessing listtilllast function")
            listtilllast(self.l)
        except Exception as e:
            logging.exception(e)
        try:
            logging.info("accessing tupletilllast function")
            tupletilllast(self.l)
        except Exception as e:
            logging.exception(e)
        try:
            logging.info("accessing onlydict function")
            onlydict(self.l)
        except Exception as e:
            logging.exception(e)
        try:
            logging.info("accessing onlysets function")
            onlysets()
        except Exception as e:
            logging.exception(e)


    def reversee(self):
        try:
            logging.info("accessing reversee function")
            return self.l[-1:-(len(self.l)+1):-1]
        except Exception as e:
            logging.exception(e)

    def searchh(self,x):
        try:
            logging.info("accessing searchh function")
            return search(self.l,x)
        except Exception as e:
            logging.exception(e)

    def onlylist(self):
        try:
            logging.info("accessing onlylist function")
            for i in self.l:
                logging.info("i == %s",i)
                if type(i) == list:
                    logging.info("i == list found %s",i)
                    print(i)
        except Exception as e:
            logging.exception(e)

    def onlydict(self):
        try:
            logging.info("accessing onlydict function")
            for i in self.l:
                logging.info("i = %s",i)
                if type(i) == dict:
                    logging.info("i==dict found %s",i)
                    print(i)
        except Exception as e:
            logging.exception(e)

    def onlytuple(self):
        try:
            logging.info("accessing onlytuple function")
            for i in self.l:
                logging.info("i = %s", i)
                if type(i) == tuple:
                    logging.info("i==tuple found %s", i)
                    print(i)
        except Exception as e:
            logging.exception(e)

    def dicts(self, x):
        try:
            logging.info("accessing dicts function")
            for i in self.l:
                if type(i) == dict:
                    for j in i.keys():
                        if x == i[j]:
                            print(i[j])
                            break
                        else:
                            print('nhi mila bhai')
                else:
                    if i == self.l[-1]:
                        print('dict kaha h isme')
        except Exception as e:
            logging.exception(e)

    def onlykeys(self):
        try:
            logging.info("accessing onlykeys function")
            lx = list()
            for i in self.l:
                if type(i) == dict:
                    lx.append(i.keys())
            return lx
        except Exception as e:
            logging.exception(e)

    def onlyvalues(self):
        try:
            logging.info("accessing onlyvalues function")
            lx = list()
            for i in self.l:
                if type(i) == dict:
                    for j in i.keys():
                        lx.append(i[j])
            return lx
        except Exception as e:
            logging.exception(e)

    def odds(self):
        try:
            logging.info("accessing odds function")
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int and j % 2 != 0:
                            print(j)
                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == int and key % 2 != 0:
                            print(key)
                        if type(val) == int and val % 2 != 0:
                            print(val)
        except Exception as e:
            logging.exception(e)

    def ineuron(self):
        try:
            logging.info("accessing ineuron function")
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == str and j == "ineuron":
                            print(j)
                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == str and key == "ineuron":
                            print(key)
                        if type(val) == str and val == "ineuron":
                            print(val)
        except Exception as e:
            logging.exception(e)

    def occurance(self):
        try:
            logging.info("accessing occurance function")
            count = 0
            for i in self.l:
                if type(i) == tuple or type(i) == list or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            count += j
                if type(i) == dict:
                    for key, val in i.items():
                        if type(key) == int:
                            count += key
                        if type(val) == int:
                            count += val
            print(count)
        except Exception as e:
            logging.exception(e)

    def onlystr(self):
        try:
            logging.info("accessing onlystr function")
            for i in self.l:
                if (type(i) == tuple or type(i) == list or type(i) == set):
                    for j in i:
                        if (type(j) == str):
                            print(j)
                if (type(i) == dict):
                    for key, val in i.items():
                        if (type(key) == str):
                            print(key)
                        if type(val) == str:
                            print(val)
        except Exception as e:
            logging.exception(e)

    def onlyalnum(self):
        try:
            logging.info("accessing onlyalnum function")
            for i in self.l:
                if (type(i) == tuple or type(i) == list or type(i) == set):
                    for j in i:
                        if (type(j) == str and j.isalnum()):
                            print(j)
                if (type(i) == dict):
                    for key, val in i.items():
                        if (type(key) == str and key.isalnum()):
                            print(key)
                        if type(val) == str and val.isalnum():
                            print(val)
        except Exception as e:
            logging.exception(e)

    def mult(self):
        try:
            logging.info("accessing mult function")
            for i in self.l:
                if (type(i) == tuple or type(i) == list or type(i) == set):
                    mul = 1
                    for j in i:
                        if (type(j) == int):
                            mul = mul * j
                    print(mul)
                if (type(i) == dict):
                    mul = 1
                    for key, val in i.items():
                        if type(val) == int:
                            mul = mul * val
                    print(mul)
        except Exception as e:
            logging.exception(e)

    def unwrap(self):
        try:
            logging.info("accessing unwrap function")
            newList1 = []
            for i in self.l:
                if (type(i) == tuple or type(i) == list or type(i) == set):
                    newList1.extend(i)
                if (type(i) == dict):
                    for key, val in i.items():
                        newList1.append(key)
                        newList1.append(val)
            print(newList1)
            print(self.l)
        except Exception as e:
            logging.exception(e)

class pattern:
    def __init__(self,s):
        import logging
        logging.basicConfig(filename="patttern.log", level=10, format='%(levelname)s : %(asctime)s : %(name)s : %(message)s')
        self.s = s

    def p1(self,n):
        try:
            logging.info("accessing p1 function")
            for i in range(n):
                for j in range(0, i + 1):
                    print(str(self.s), end=" ")
                print()
        except Exception as e:
            logging.exception(e)

    def p2(self,n):
        try:
            logging.info("accessing p2 function")
            for i in range(n - 1):
                for j in range(i, n):
                    print(" "*len(self.s), end=" ")
                for j in range(i - 1):
                    print(str(self.s), end=" ")
                for j in range(i + 1):
                    print(str(self.s), end=" ")
                print()
            for i in range(n):
                for j in range(i):
                    print(" "*len(self.s), end=" ")
                for j in range(i, n - 3):
                    print(str(self.s), end=" ")
                for j in range(i, n):
                    print(str(self.s), end=" ")
                print()
        except Exception as e:
            logging.exception(e)