from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "icaro"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
graph["icaro"] = []

def searchName(name, searchname):
    result = name == searchname
    return result

def search(startingname, searchname):
    searched = set()
    search_queue = deque()
    search_queue += graph[startingname]
    
    while search_queue:
        person = search_queue.popleft()
        found = searchName(person, searchname)

        if person in searched:
            continue

        if found:
            print (f"Found {searchname} in the graph!")
            return True
        
        else: 
            searched.add(person)
            search_queue += graph[person]

    print(f"{searchname} not found in the graph.")
    return False


search("you", "icaro")


def search2(startingname, searchname):
    searched = set()
    search_queue = deque()
    search_queue += graph[startingname]
    level = 0

    while search_queue:
        nodesatcurrentlevel = len(search_queue)
        for _ in range(nodesatcurrentlevel):
            person = search_queue.popleft()
            found = searchName(person, searchname)

            if person in searched:
                continue

            if found:
                print (f"Found {searchname} in the graph! At level {level}")
                return True
            
            else: 
                searched.add(person)
                search_queue += graph[person]
        level += 1

    
    print(f"{searchname} not found in the graph.")
    return False


search2("you", "icaro")

