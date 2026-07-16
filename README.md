# UPY-PROGRAMMING-ROM-N-SOSA-Q2-2026
Repositorio de trabajo de la materia de Programación de la UPY y agregado el CW07: Cálculo de dígito verificador
Programación 
# Declaraciones de IA
Todas las declaraciones de IA se encuentran en las carpetas correspondientes de cada classwork
# Classwork 08 - Numerical Integration

## Description
This project implements an algorithm for dynamic numerical integration. It estimates the definite integral of a user-defined mathematical function $f(x)$ over a specified interval $[a, b]$. 

The program parses mathematical inputs (including $\pi$) and allows the user to calculate the area using one of four numerical methods:
* **LRM**: Left Riemann Method
* **RRM**: Right Riemann Method
* **MPM**: Midpoint Method
* **TRAP**: Trapezoidal Method

## Folder Structure
Located within the repository `UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-08-Numerical-Integration/`
* 📄 `PPP.txt`: Complete pseudocode written in plain English, utilizing `←` for assignments and `#` for comments without Python-specific syntax.
* 🖼️ `Flowchart.png`: Visual diagram covering the decision flow for the selected integration modes and the iteration flows.
* 🐍 `numerical_integration.py`: The working Python implementation, cleanly divided into `# INPUT`, `# PROCESS`, and `# OUTPUT` sections.

## How to Run
1. Navigate to the folder: `cd Classwork-08-Numerical-Integration`
2. Run the Python script: `python numerical_integration.py`
3. Follow the console prompts to input the left endpoint ($a$), right endpoint ($b$), the function $f(x)$, and the desired method (LRM/RRM/MPM/TRAP).

## Submission Checklist & Rubric (10 Total Points)
- [ ] **3 pts**: `PPP.txt` is complete and formatted correctly.
- [ ] **3 pts**: `Flowchart.png` is exported as an image (ensure it is a `.png` and not a `.jpeg`).
- [ ] **3 pts**: `numerical_integration.py` runs properly with necessary comments.
- [ ] **1 pt**: AI Use Declaration included.
- [ ] **Commit message exact match**: `Add Classwork 08 - Numerical Integration`

---

# Classwork 09 - Spanish Verb Conjugator

## Description
This project implements an algorithm to automatically conjugate regular Spanish verbs. It takes a verb ending in `-ar`, `-er`, or `-ir` in its infinitive form as input, extracts its stem, and outputs its present tense conjugations for the standard pronouns (Yo, Tú, Él, Nosotros, Vosotros, Ellos).

## Folder Structure
Located within the repository `UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-09-Spanish-Verb-Conjugator/`
* 📄 `PPP.txt`: Complete pseudocode written in plain English, utilizing `←` for assignments and `#` for comments without Python-specific syntax.
* 🖼️ `Flowchart.png`: Visual diagram covering the logical flow of the conjugation process based on verb endings.
* 🐍 `spanish_verb_conjugator.py`: The working Python implementation, cleanly divided into `# INPUT`, `# PROCESS`, and `# OUTPUT` sections.

## How to Run
1. Navigate to the folder: `cd Classwork-09-Spanish-Verb-Conjugator`
2. Run the Python script: `python spanish_verb_conjugator.py`
3. Follow the console prompt to input a regular Spanish verb (e.g., `programar`, `comer`, `vivir`).

## Submission Checklist & Rubric (10 Total Points)
- [ ] **3 pts**: `PPP.txt` is complete and formatted correctly.
- [ ] **3 pts**: `Flowchart.png` is exported as an image (ensure it is a `.png` and not a `.jpeg`).
- [ ] **3 pts**: `spanish_verb_conjugator.py` runs properly with necessary comments.
- [ ] **1 pt**: AI Use Declaration included.
- [ ] **Commit message exact match**: `Add Classwork 09 - Spanish Verb Conjugator`

---

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

---

# Classwork 11 - The Mandelbrot Set 🌌

## Description
This project implements an algorithm to calculate and generate data for the **Mandelbrot Set**. It maps a 2D grid of pixels to complex numbers on the complex plane and iterates the mathematical function $z_{n+1} = z_{n}^{2} + c$ (starting with $z_0 = 0$). 

The program determines whether each point belongs to the Mandelbrot set by checking if its magnitude escapes to infinity ($|z| > 2$) within a maximum number of iterations. The results (row, column, and number of iterations) are then exported into a CSV file (`mandelbrot.csv`) which can be used later to visualize the fractal.

## Folder Structure
Located within the repository `UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-11-The-Mandelbrot-Set/`
* 📄 `PPP.txt`: Complete pseudocode written in plain English, utilizing `←` for assignments and `#` for comments without Python-specific syntax.
* 🖼️ `Flowchart.png`: Visual diagram covering the iteration flow for each method and the decision flow for the modes.
* 🐍 `mandelbrot_set_math.py`: The working Python implementation, cleanly divided into `# INPUT`, `# PROCESS`, and `# OUTPUT` sections.

## How to Run
1. Open your terminal or Git Bash.
2. Navigate to the folder: `cd Classwork-11-The-Mandelbrot-Set`
3. Run the Python script:
   ```bash
   python mandelbrot_set_math.py

---

# Classwork 12 - The Mandelbrot Set Visualization 🌌🖼️

## Description
This project builds upon the mathematical calculations from Classwork 11 to generate a visual representation of the **Mandelbrot Set**. It reads the previously generated dataset (`mandelbrot.csv`) and uses the Python Imaging Library (PIL/Pillow) to map the iteration data into a 2D image.

The program converts the number of iterations it took for each complex number to escape into a grayscale brightness value (from `0`/black for points inside the set, to `255`/white for points that escaped quickly). The final output is a rendered image (`mandelbrot.png`) revealing the fractal's structure.

## Folder Structure
Located within the repository `UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-12-The-Mandelbrot-Set/`
* 📄 `PPP.txt`: Complete pseudocode written in plain English, utilizing `←` for assignments and `#` for comments without Python-specific syntax.
* 🖼️ `Flowchart.png`: Visual diagram covering the iteration flow for each method and the decision flow for the three modes.
* 🐍 `mandelbrot_set_vis.py`: The working Python implementation, cleanly divided into `# INPUT`, `# PROCESS`, and `# OUTPUT` sections.

## How to Run
1. Open your terminal or Git Bash.
2. Ensure you have the Pillow library installed by running: `pip install Pillow`
3. Navigate to the folder: `cd Classwork-12-The-Mandelbrot-Set`
4. Run the Python script:
   ```bash
   python mandelbrot_set_vis.py

---

# Classwork 13 - Error Handling 🛡️

## Description
This project focuses on implementing robust error handling and input validation in Python. It revisits three previous assignments (CW07, CW08, and CW09) to prevent runtime crashes by using `try...except` blocks.

The implementations handle standard Python exceptions (such as `ValueError`, `ZeroDivisionError`, and `NameError`) and introduce **Custom Exceptions** inherited from the base `Exception` class to enforce specific business rules, including:
* **CW07**: `DigitoApocrifo` for invalid validation digits.
* **CW08**: `LimitesInvertidosError` and `MetodoInvalidoError` for incorrect numerical integration parameters.
* **CW09**: `VerboInvalidoError` and `TerminacionInvalidaError` for incorrect Spanish verb formatting.

## Folder Structure
Located within the repository `UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-13-Error-Handling/`
* 🐍 `cw07.py`: The error-handled version of the Verification Digit Calculator.
* 🐍 `cw08.py`: The error-handled version of the Numerical Integration algorithm.
* 🐍 `cw09.py`: The error-handled version of the Spanish Verb Conjugator.

## How to Run
1. Navigate to the folder: `cd Classwork-13-Error-Handling`
2. Run any of the Python scripts: 
   ```bash
   python cw07.py
   python cw08.py
   python cw09.py

---

# Classwork 14 - Error Handling Part II 🛡️

## Description
This project continues the implementation of robust error handling and input validation in Python, focusing on complex data structures, file I/O operations, and image processing. It revisits three previous assignments (CW10, CW11, and CW12) to prevent runtime crashes by using `try...except` blocks.

The implementations handle standard Python exceptions (such as `FileNotFoundError`, `ValueError`, and `IndexError`) and introduce **Custom Exceptions** inherited from the base `Exception` class to enforce specific business rules, including:
* **CW10**: `UsuarioNoExisteError`, `MateriaNoExisteError`, and `CalificacionInvalidaError` for role-based grading validation.
* **CW11**: `ConfiguracionMalFormadaError` and `DimensionInvalidaError` for file reading and parameter parsing.
* **CW12**: `DimensionInconsistenteError` and `FormatoCSVIncorrectoError` for pixel mapping and CSV data rendering.

## Folder Structure
Located within the repository `UPY-PROGRAMMING-ROM-N-SOSA-Q2-2026`, this project strictly follows the required directory naming convention:

📁 `Classwork-14-Error-Handling/`
* 🐍 `cw10.py`: The error-handled version of the School Management System.
* 🐍 `CW11.py`: The error-handled version of the Mandelbrot Set math generator.
* 🐍 `CW12.py`: The error-handled version of the Mandelbrot Set visualization.

## How to Run
1. Navigate to the folder: `cd Classwork-14-Error-Handling`
2. Run any of the Python scripts: 
   ```bash
   python cw10.py
   python CW11.py
   python CW12.py   

```

             / .-
             |/,-'`
          _.-'''-._
        /` __   __ `\
   ___ ;__.--._.--.__;
  /  /\  ( O / \ O )  `\
  | _\/_  '-'   '-'   _/
 _|_|' |     (_)     |
/  __) |             |
|  __) |    .___.    |     .-.  _
| ___)';   /\.-./\   ;     | | / |
|~||/\ .\    `-`    /    __| |/ /_
| \_\/==;'._  -  _.'__  (_       _)
\  8      /\"""""/\   `\  `|  .'`
 '--8----.`-`\^/`-`.    \  |~~|
     8   |   /~\   |`\   \ |  |
     8   |   |\|   |  \   `y  |
     8   |   |\|   |   \      /
     8   |   |\|   |    '.__.'
     8   |___|\|___|
     8   |===\_/===|
```	
