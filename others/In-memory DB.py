"""
The program was written in python3 (If you are using python2, you need to change
query = input.split() to query = raw_input.split())

The methods in myDB is case-insensitive

The program handles several invalid input cases, and it just do not execute
these queries

You hust need run this script or run solution function.
"""
# Time: O(1) for simple set, get, unset, numequalto method
# Space: O(n)
# For transaction, we only consider set and unset methods (because only set 
# and unset methods changes the data in the database)
# For every set or unset query in a transaction, we store an inversed query in a stack
# When rollback is called, we executed the inversed query
# When commit is called, we just clean the stack

class MyDB():
    #lookup is for unset, set, get methods and count is for numequalto method
    def __init__(self):
        self.lookup = {}
        self.count = {}

    def set(self, name, value):
        self.unset(name)
        self.lookup[name] = value
        if value not in self.count:
            self.count[value] = 0
        self.count[value] += 1

    def get(self, name):
        if name in self.lookup:
            return self.lookup[name]
        return None

    def unset(self, name):
        if name in self.lookup:
            oldValue = self.lookup[name]
            self.count[oldValue] -= 1
            if not self.count[oldValue]:
                self.count.pop(oldValue)
            self.lookup.pop(name)

    def numequalto(self, value):
        if value in self.count:
            return self.count[value]
        return 0

#ExecuteQuery function handles the query set, unset, get and numequalto query
def executeQuery(db, query):
    if query[0] == "set":
        db.set(query[1], query[2])
    elif query[0] == "get":
        return db.get(query[1])
    elif query[0] == "unset":
        db.unset(query[1])
    return db.numequalto(query[1])

#Judge if the input query is valid (according to the problem, it is an optional function)
def isValid(query):
    if query[0] == "set":
        if len(query) < 3:
            return False
        return True
    elif query[0] == "unset":
        if len(query) < 2:
            return False
        return True
    elif query[0] == "get":
        if len(query) < 2:
            return False
        return True
    elif query[0] == "numequalto":
        if len(query) < 2:
            return False
        return True
    return False

#Execute queries, main about dealing with the transcation queries    
def solution():
    db = MyDB()
#stack for transaction command
#flag to record if current command is in a transaction
    stack, flag = [], False
    while True:
        query = input().split()
        if not query:
            print("invaild input!")
            continue
        #Only the query is case-insentive, not the name and value.
        query[0] = query[0].lower()
        if query[0] == "end":
            break
        elif query[0] == "begin":
            stack.append("stop")
            flag = True
        elif query[0] == "rollback":
            if not stack:
                print("NO TRANSACTION")
            else:
                #Execute inversed query
                cur = stack.pop()
                while cur != "stop":
                    executeQuery(db, cur)
                    cur = stack.pop()
                if not stack:
                    flag = False
        elif query[0] == "commit":
            stack, flag = [], False
        elif isValid(query):
            #Store inversed query
            if flag and query[0] in ("set", "unset"):
                newQuery = ["get", query[1]]
                oldValue = executeQuery(db, newQuery)
                if oldValue is None:
                    stack.append(["unset", query[1]])
                else:
                    stack.append(["set", query[1], oldValue])
            #Execute query
            res = executeQuery(db, query)
            if query[0] == "get":
                if res is None:
                    print("NULL")
                else:
                    print(res)
            elif query[0] == "numequalto":
                print(res)
        else:
            print("invalid input!")
                
if __name__ == "__main__":
    solution()
