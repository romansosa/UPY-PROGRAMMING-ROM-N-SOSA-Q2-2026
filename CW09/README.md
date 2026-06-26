## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-06-25

Propósito: Redactar el README.md

Prompt utilizado:
Ayúdame a actualizar el README.md de mi repo de programación, es la classwork 09, este fue mi python, mi PPP y mi flowchart, estas fueron las instrucciones de las tareas, te adjunto el estado actual de mi README.md, quiero que conserves lo que ya esta y me ayudes a hacer el de classwork 09
# UPY-PROGRAMMING-ROM-N-SOSA-Q2-2026
Repositorio de trabajo de la materia de Programación de la UPY y agregado el CW07: Cálculo de dígito verificador
Programación 
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
## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-06-12

Propósito: Redactar el README.md

Prompt utilizado:

Considera las diapositivas en el notebook, las instrucciones de la tarea, el python, el ppp y el flowchart para crear un README.md actualizado 
Instructions

Inside your repository UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026, create a folder named exactly:
Classwork-08-Numerical-Integration

That folder must contain the following three files:
PPP.txt — your complete pseudocode following class rules: plain English, ← for assignment, # for comments, no Python syntax.
Flowchart.png — your flowchart exported as an image, covering the iteration flow for each method and the decision flow for the three modes.
numerical_integration.py — your working Python program with # INPUT, # PROCESS, and # OUTPUT comments.
Once your folder is complete, commit and push to your main branch with the following commit message:
Add Classwork 08 - Numerical Integration

Submit the link of your repository through Teams.

Rubric

PPP.txt (complete, correct pseudocode)3Flowchart.png (iteration + decision flows)3numerical_integration.py (working program)3AI use declaration1Total10
Archivos suministrados: El python, el PPP y el flowchart

Respuesta en crudo (raw):

Here is an updated `README.md` for your assignment, structured to help you track the project requirements and document your work.

I have also added a "Developer Notes" section at the bottom. Since you noted a bug in your `PPP.txt` and there is a typo in your `cw08.py` draft, I wanted to gently point them out so you can fix them before your final commit to `numerical_integration.py`!

---

```markdown
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
## AI Use Declaration
*(Student: Fill this out based on your university's AI policy, detailing how AI was used to assist with drafting, debugging, or generating this README).*

```

### 🛠️ Developer Notes (Bugs to fix before you submit):

Before you rename `cw08.py` to `numerical_integration.py` and push to your main branch, make sure to patch these two bugs currently present in your files:

1. **Endpoint Assignment Typo (`cw08.py`):**
In the `# INPUT` section for variable `b`, the `else` statement incorrectly assigns `a` to `b`:
```python
else:
    b = float(a) # <-- Change this to float(b)

```


2. **The TRAP Fallthrough Bug (`PPP.txt` & `cw08.py`):**
You correctly identified this in your `PPP.txt` with a `# BUG` comment! Currently, if the user selects "TRAP", the code calculates the trapezoidal area, but then completely falls through into the Riemann/Midpoint `for` loop at the bottom, compounding the `area` variable incorrectly.
* **The Fix:** You should wrap the final `for` loop in a conditional check (e.g., `if method in ["LRM", "RRM", "MPM"]:`) or use `if/elif/else` blocks throughout the `# PROCESS` section so the program only executes *one* integration loop per run.
```

             / .-
             |/,-'`
          _.-'''-._
        /` __   __ `\
   ___ ;__.--._.--.__;
  /  /\  ( O / \ O )  `\
  | _\/_  '-'   '-'   _/
 _|_|' |     (_)     |
/  __) |             |
|  __) |    .___.    |     .-.  _
| ___)';   /\.-./\   ;     | | / |
|~||/\ .\    `-`    /    __| |/ /_
| \_\/==;'._  -  _.'__  (_       _)
\  8      /\"""""/\   `\  `|  .'`
 '--8----.`-`\^/`-`.    \  |~~|
     8   |   /~\   |`\   \ |  |
     8   |   |\|   |  \   `y  |
     8   |   |\|   |   \      /
     8   |   |\|   |    '.__.'
     8   |___|\|___|
     8   |===\_/===|
``` 


Classwork #09 - Spanish Verb Conjugator
Vence hoy a las 23:59•
Se cierra hoy a las 23:59
UNIT 3
Instrucciones
Instructions

Inside your repository UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026, create a folder named exactly:

Classwork-09-Spanish-Verb-Conjugator

That folder must contain the following three files:

PPP.txt — your complete pseudocode following class rules: plain English, ← for assignment, # for comments, no Python syntax.
Flowchart.png — your flowchart exported as an image, covering the iteration flow for each method and the decision flow for the three modes.
spanish_verb_conjugator.py — your working Python program with # INPUT, # PROCESS, and # OUTPUT comments.
Once your folder is complete, commit and push to your main branch with the following commit message:
Add Classwork 09 - Spanish Verb Conjugator

Submit the link of your repository through Teams.

Rubric

PPP.txt (complete, correct pseudocode)3Flowchart.png (iteration + decision flows)3spanish_verb_conjugator.py (working program)3AI use declaration1Total10

Respuesta en crudo (raw):

¡Claro que sí! Aquí tienes el archivo `README.md` actualizado. He conservado toda la información anterior de la Classwork 08 y agregado la nueva sección para la Classwork 09 siguiendo el mismo formato ordenado.

También actualicé la sección de "AI Use Declaration" para que incluya un registro tanto para el CW08 como para el CW09 (con la fecha de hoy).

---

```markdown
# UPY-PROGRAMMING-ROM-N-SOSA-Q2-2026
Repositorio de trabajo de la materia de Programación de la UPY y agregado el CW07: Cálculo de dígito verificador
Programación 

---

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

## AI Use Declarations

### Classwork 08
**Nombre del estudiante:** Román Alonso Sosa Fiesco
**IA utilizada:** Gemini
**Fecha de uso:** 2026-06-12
**Propósito:** Redactar el README.md
**Prompt utilizado:** Considera las diapositivas en el notebook, las instrucciones de la tarea, el python, el ppp y el flowchart para crear un README.md actualizado.

### Classwork 09
**Nombre del estudiante:** Román Alonso Sosa Fiesco
**IA utilizada:** Gemini
**Fecha de uso:** 2026-06-25
**Propósito:** Actualizar el archivo README.md conservando los proyectos anteriores e integrando la documentación de la Classwork 09.
**Prompt utilizado:** Ayúdame a actualizar el README.md de mi repo de programación, es la classwork 09, este fue mi python, mi PPP y mi flowchart, estas fueron las instrucciones de las tareas, te adjunto el estado actual de mi README.md, quiero que conserves lo que ya esta y me ayudes a hacer el de classwork 09.

```

---

### 🛠️ Developer Notes (Detalles a corregir antes de tu commit):

Noté un par de detalles pequeñitos en tu código que vale la pena ajustar antes de que lo subas a GitHub para asegurar tus 10 puntos:

1. **Renombrar tu archivo Python:** Tu archivo actualmente se llama `cw09.py`, pero en las instrucciones de entrega exigen que el archivo se llame exactamente **`spanish_verb_conjugator.py`**.
2. **Acento en pronombre:** En tu lista de pronombres escribiste `"Èl"` (con acento grave/hacia la izquierda). En español lo correcto es usar el acento agudo: `"Él"`.
3. **Secciones de comentarios faltantes:** La rúbrica pide específicamente que el archivo en Python tenga los comentarios `# INPUT`, `# PROCESS` y `# OUTPUT`. Noté que en tu código incluyes el `# INPUT`, pero te faltó agregar textualmente los comentarios de `# PROCESS` (antes de sacar el *stem*) y `# OUTPUT` (antes del ciclo *for*). Agrégalos para no perder puntos de formato. ¡Tu lógica del código está impecable!
