# from task import Task

class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task not in self.tasks:  
            self.tasks.append(new_task)
            return f'Task {new_task.details()} is added to the section'     
        return f'Task is already in the section {self.name}' 

    def complete_task(self, task_name):
        if task_name not in [x.name for x in self.tasks]:
            return f'Could not find task with the name {task_name}'
        result_task = [x for x in self.tasks if x.name == task_name][0]
        result_task.completed = True
        return f'Completed task {task_name}'

    def clean_section(self):
        count_completed_tasks = len([x for x in self.tasks if x.completed == True])
        self.task = [x for x in self.tasks if x.completed != True]
       
        return f'Cleared {count_completed_tasks} tasks.'
    
    def view_section(self):
        section = f'Section {self.name}:\n'
        return section  + '\n'.join([x.details() for x in self.tasks])

