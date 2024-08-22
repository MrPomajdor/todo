class Status:
    todo = 0
    doing = 1
    done = 2

class Board:
    def __init__(self) -> None:
        self.title = ""
        self.description = ""
        self.tasks: list[Task] = []
    def Serialize(self) -> dict:
        """Serializes the Board to a JSON"""

        return {"title":self.title,"description":self.description,"tasks":[x.Serialize() for x in self.tasks]}
    
    def Deserialize(self,d:dict):
        """Deserializes from a provided JSON save"""

        #Add deserialization error handling
        self.title = d.get("title","No name")
        self.description = d.get("description","No description")
        self.tasks = [Task().Deserialize(x) for x in d.get("tasks",[])]

        return self


class Task:
    def __init__(self) -> None:
        self.name = ""
        self.description = ""
        self.status = Status.todo

    def Serialize(self) -> dict:
        """Serializes the Task to a JSON"""

        return {"name":self.name,"status":self.status,"description":self.description}
    
    def Deserialize(self,d:dict):
        """Deserializes from a provided JSON and returns a Task object"""
        #Add deserialization error handling
        self.name = d.get("name","No name")
        self.status = d.get("status",0)
        self.description = d.get("description","No description")
        
        return self

