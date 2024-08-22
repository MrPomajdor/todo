class Board:
    def __init__(self) -> None:
        self.text = ""
        self.tasks: list[Task] = []

class Task:
    class Status:
        todo = (0," ")
        doing = (1,"D")
        done = (2,"✓")
    
    def __init__(self) -> None:
        self.name = ""
        self.status = Task.Status.todo
