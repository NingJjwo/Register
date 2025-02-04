class Person:
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
        
class Student(Person):
    
    def __init__(self,name,id,subject,note):
        super().__init__(name,id)
        self.subject = subject
        self.note = note
        
class Register:
    
    def __init__(self):
            self.students = []

    def addUser(self,User):
            self.students.append(User)
        
    def listUsers(self):
        if len(self.students) == 0:
            print("La lista esta vacia")
        for estudiante in self.students:
            print(vars(estudiante))
    
    def editUser(self, student_id):
        
        if not student_id in self.students:
            print("Error: El usuario con esa ID no existe.")
        else:
            new_name = input("Digite el nuevo nombre")
            new_subject = input("Digite la nueva materia")
            new_note = input("Digite la nueva nota")
            
            self.student.id == student_id
            self.student.name = new_name
            self.student.subject = new_subject
            self.student.note = new_note

    def removeUser(self,student_id):
        for student in self.students:
            if(student.id == student_id):
                self.students.remove(student)