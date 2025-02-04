import user

register = user.Register()

print("MENU")
print("1. Agregar Usuario")
print("2. Listar Usuarios")
print("3. Editar Usuario")
print("4. borrar Usuario")
print("5. Salir")

option = int(input("Digite una opcion"))

while(option != 5):
    match option:
        case 1:
            name = input("Digite su nombre")
            id = int(input("Digite su id"))
            nota = input("Digite la Nota")
            curso = input("Digite el curso")
            Student = user.Student(name,id,nota,curso)
            register.addUser(Student)   
        case 2:
            register.listUsers()
        case 3:
            target = int(input("Digite el ID del usuario para editar."))
            register.editUser(target)
        case 4:
            target = int(input("Digite el ID del usuario para borrar."))
            register.removeUser(target)
        case 5:
            print("Saliendo del programa")
            break
        case _:
            print("Opcion invalida.")
    option = int(input("Digite una opcion"))