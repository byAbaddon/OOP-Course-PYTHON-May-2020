class Programmer:
    def __init__(self, name : str, language : str, skills : int):
        self.name = name
        self.language = language
        self.skills = skills


    def watch_course(self, course_name, language, skills_earned):
        if language in self.language:
            self.skills += skills_earned
            return f'{self.name} watched {course_name}'
        return  f'{self.name} does not know {language}'   
    
    def change_language(self, new_language, skills_needed):
        if self.skills >= skills_needed and self.language != new_language:
           previous_language = self.language
           self.language = new_language 
           return f'{self.name} switched from {previous_language} to {new_language}'
        
        if  self.skills >= skills_needed and self.language == new_language:
            return f'{self.name} already knows {self.language}'
        
        if self.skills < skills_needed:
            return f'{self.name} needs {abs(self.skills - skills_needed)} more skills'


