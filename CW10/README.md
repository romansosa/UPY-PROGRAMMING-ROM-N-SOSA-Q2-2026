## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-06-26

Propósito: Redactar el README.md

Prompt utilizado:
Actualiza el README.md para que explique la classwork 10 
Classwork #10 - School Management System
Vence hoy a las 23:59•
Se cierra hoy a las 23:59
UNIT 3
Instrucciones
Instructions

Inside your repository UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026, create a folder named exactly:

Classwork-10-School-Management-System

That folder must contain the following three files:

PPP.txt — your complete pseudocode following class rules: plain English, ← for assignment, # for comments, no Python syntax.
Flowchart.png — your flowchart exported as an image, covering the iteration flow for each method and the decision flow for the three modes.
school_management_system.py — your working Python program with # INPUT, # PROCESS, and # OUTPUT comments.
Once your folder is complete, commit and push to your main branch with the following commit message:
Add Classwork 10 - School Management System

Submit the link of your repository through Teams.

Rubric

PPP.txt (complete, correct pseudocode)3Flowchart.png (iteration + decision flows)3school_management_system.py (working program)3AI use declaration1Total10

Respuesta en crudo (raw):

¡Claro que sí! Aquí tienes una propuesta de contenido para tu `README.md`. Está diseñado para cumplir con los requisitos de la rúbrica y explicar claramente el propósito del proyecto, su estructura y el uso de la IA.

Puedes copiar y pegar este bloque directamente en tu archivo `README.md` dentro de la carpeta `Classwork-10-School-Management-System`:

```markdown
# Classwork 10 - School Management System 🏫

## Description
This project is a Python-based console application that simulates a simple school login and management system. The program features a role-based access control system (RBAC) with three distinct user roles:
* **Student:** Can view their own approved and pending subjects.
* **Teacher:** Can view all students and edit/update their grades.
* **Coordinator:** Has read-only access to view lists of teachers, subjects, and all student records.

The project demonstrates the fundamental use of Python data structures—specifically **lists, tuples, dictionaries, and sets**—along with control flow structures (`while` loops, `if/elif/else`), all implemented without the use of custom functions (`def`).

## Project Structure
This folder contains the following required files:

* `PPP.txt`: The complete Pseudocode Programming Process (PPP) detailing the logic, iteration flow, and decisions in plain English.
* `Flowchart.png`: A visual flowchart diagram mapping out the login authentication loop and the distinct decision trees for each user role.
* `school_management_system.py`: The main working Python program, neatly organized with `# INPUT`, `# PROCESS`, and `# OUTPUT` comments. *(Note: Make sure to rename your `cw10.py` to this exact name before pushing!).*

## How to Run
1. Ensure you have Python installed on your system.
2. Open your terminal or Git Bash.
3. Navigate to the `Classwork-10-School-Management-System` directory.
4. Run the script using the following command:
   ```bash
   python school_management_system.py

```

5. Log in using the predefined credentials (e.g., User: `jperez`, Password: `1234` for a student role).

## AI Use Declaration

*Include a brief statement here about how you used AI for this assignment. For example:*

> "I used AI tools (like ChatGPT/Gemini) to help troubleshoot specific syntax errors, understand the implementation of sets for the 'aprobadas' logic, and format this README. All core logic and pseudocode were originally structured by me."

```

### 💡 Un recordatorio rápido para tu entrega:
Noté que el archivo de código que subiste se llama `cw10.py`, pero las instrucciones de tu profesor dicen explícitamente que debe llamarse **`school_management_system.py`**. ¡No olvides renombrarlo antes de hacer el `git commit` para asegurar todos tus puntos de la rúbrica!

```