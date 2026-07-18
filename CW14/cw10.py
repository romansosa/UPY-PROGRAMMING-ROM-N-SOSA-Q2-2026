
# Excepciones personalizadas 
class UsuarioNoExisteError(Exception):
    pass

class MateriaNoExisteError(Exception):
    pass

class CalificacionInvalidaError(Exception):
    pass

# Required Structures
users = {
    'jperez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Juan Pérez'
    },
    'dromo':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Daniela Romo'
    },
    'mjuarez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Mauricio Juárez'
    },
    'mlopez':	{
        'password': '1234',
        'rol': 'student',
        'name': 'María López'
    },
    'euc':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Ernesto Uc'
    },
    'cbalam':	{
        'password': '1234',
        'rol': 'student',
        'name': 'Carlos Balam'
    },
    'jpedrozo':	{
        'password': '1234',
        'rol': 'professor',
        'name': 'Jorge Pedrozo'
    },
    'dgamboa':	{
        'password': '1234',
        'rol': 'coordinator',
        'name': 'Didier Gamboa'
    }
}
 
subjects = (
    "Discrete Mathematics",
    "Programming",
    "English II",
    "Differential Calculus",
    "Probability and Statistics",
    "Computer and Server Architecture",
    "Socio-Emotional Skills and Conflict Management"
)
 
notes = {
    'jperez': {
        'Discrete Mathematics': 8.5,
        'Programming': 9.2,
        'English II': 9.0,
        'Differential Calculus': 7.8,
        'Probability and Statistics': 8.3,
        'Computer and Server Architecture': 6.8,
        'Socio-Emotional Skills and Conflict Management': 9.5
    },
    'dromo': {
        'Discrete Mathematics': 9.0,
        'Programming': 6.7,
        'English II': 9.4,
        'Differential Calculus': 6.2,
        'Probability and Statistics': 9.1,
        'Computer and Server Architecture': 6.5,
        'Socio-Emotional Skills and Conflict Management': 9.8
    },
    'mjuarez': {
        'Discrete Mathematics': 7.5,
        'Programming': 8.0,
        'English II': 8.5,
        'Differential Calculus': 7.0,
        'Probability and Statistics': 7.8,
        'Computer and Server Architecture': 6.2,
        'Socio-Emotional Skills and Conflict Management': 8.9
    },
    'mlopez': {
        'Discrete Mathematics': 9.5,
        'Programming': 9.8,
        'English II': 9.2,
        'Differential Calculus': 9.0,
        'Probability and Statistics': 9.6,
        'Computer and Server Architecture': 9.4,
        'Socio-Emotional Skills and Conflict Management': 10.0
    },
    'euc': {
        'Discrete Mathematics': 8.2,
        'Programming': 6.9,
        'English II': 8.8,
        'Differential Calculus': 6.0,
        'Probability and Statistics': 6.4,
        'Computer and Server Architecture': 8.1,
        'Socio-Emotional Skills and Conflict Management': 9.0
    },
    'cbalam': {
        'Discrete Mathematics': 8.8,
        'Programming': 9.0,
        'English II': 8.5,
        'Differential Calculus': 6.6,
        'Probability and Statistics': 8.9,
        'Computer and Server Architecture': 8.7,
        'Socio-Emotional Skills and Conflict Management': 9.2
    }
}

# Acceso 
log_in = False
current_user = ""

while not log_in:
    username = input("User: ")
    password = input("Password: ")
    
    if username in users and users[username]["password"] == password:
        log_in = True
        current_user = username
    else:
        print("Wrong user/password!")
        
# Identificación        
user_info = users[current_user]
role = user_info["rol"]
name = user_info["name"]

print(f"Bienvenid@!, {name} ({role})")

# Filtrado por rol
# Estudiante
if role == "student":
    print("=======================================")
    print(" School Report")
    print("=======================================")
    
    approved = set()
    pending = set()
    
    for subj in subjects:
        grade = notes[current_user][subj]
        
        if grade >= 7.0:
            print(f"{subj:<32} : {grade}")
            
        if grade >= 7.0:
            approved.add(subj)
        else:
            pending.add(subj)
            
    print(f"\nApproved: {approved}")
    print(f"Pending : {pending}")

# Maestro
elif role == "professor":
    while True:
        print("=======================================")
        print(" Students")
        print("=======================================")
        for u, info in users.items():
            if info["rol"] == "student":
                print(f"User: {u:<8} | Student: {info['name']}")
        print()
        
        student_to_grade = input("Student to grade (username): ")
        
        if student_to_grade.lower() == "stop":
            break
            
        try:
            # Validación de usuario existente y rol de estudiante
            if student_to_grade not in users or users[student_to_grade]["rol"] != "student":
                raise UsuarioNoExisteError("Ese usuario no existe")
                
            print("\n=======================================")
            print(" Subjects")
            print("=======================================")
            for subj in subjects:
                print(subj)
            print()
            
            subject_to_grade = input("Subject to grade: ")
            
            # Validación de existencia de la materia
            if subject_to_grade not in subjects:
                raise MateriaNoExisteError("Esa materia no existe")
                
            new_grade = input("New grade: ")
            
            # Validación de tipo (debe ser numérico) y límite/rango (0 a 10)
            try:
                new_grade_float = float(new_grade)
            except ValueError:
                raise CalificacionInvalidaError("La calificación debe ser un número válido.")
                
            if new_grade_float < 0.0 or new_grade_float > 10.0:
                raise CalificacionInvalidaError("La calificación debe estar entre 0 y 10.")
            
            old_grade = notes[student_to_grade][subject_to_grade]
            print("\nDo you confirm (yes/no)?")
            print(f"{subject_to_grade}: {old_grade} ==> {new_grade_float}")
            confirm = input()
            
            # Confirmación
            if confirm.lower() == "yes":
                notes[student_to_grade][subject_to_grade] = new_grade_float
                print("\nGrade updated!")
                print(notes[student_to_grade])
                print()
            else:
                break 
                
        # Captura e impresión de los errores sin detener por completo el programa
        except UsuarioNoExisteError as e:
            print(e)
        except MateriaNoExisteError as e:
            print(e)
        except CalificacionInvalidaError as e:
            print(e)

# Coordinador
elif role == "coordinator":
    print("\n=======================================")
    print(" Professors")
    print("=======================================")
    for u, info in users.items():
        if info["rol"] == "professor":
            print(f"User: {u:<8} | Professor: {info['name']}")
            
    print("\n=======================================")
    print(" Students")
    print("=======================================")
    for u, info in users.items():
        if info['rol'] == "student":
            print(f"User: {u:<8} | Student: {info['name']}")
            
    print("\n=======================================")
    print(" Records")
    print("=======================================")
    
    student_users = [u for u, info in users.items() if info["rol"] == "student"]
    
    header = f"{'SUBJECTS':<16} | " + " | ".join(f"{u:<6}" for u in student_users)
    print(header)
    print("-" * len(header))
    for subj in subjects:
        
        subj_trunc = subj[:13] 
        row = f"{subj_trunc:<16} | "
        
        grades = []
        for u in student_users:
            grades.append(f"{notes[u][subj]:<6}")
            
        row += " | ".join(grades)
        print(row)