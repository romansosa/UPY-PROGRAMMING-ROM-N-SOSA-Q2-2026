## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-07-

Propósito: Redactar el README.md

Prompt utilizado:
Actualiza el README.md para que explique la Classwork #11 - The Mandelbrot Set
Vence hoy a las 23:59•
Se cierra hoy a las 23:59
UNIT 3
Instrucciones
Instructions

Inside your repository UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026, create a folder named exactly:

Classwork-11-The-Mandelbrot-Set

That folder must contain the following three files:

PPP.txt — your complete pseudocode following class rules: plain English, ← for assignment, # for comments, no Python syntax.
Flowchart.png — your flowchart exported as an image, covering the iteration flow for each method and the decision flow for the three modes.
mandelbrot_set_math.py — your working Python program with # INPUT, # PROCESS, and # OUTPUT comments.
Once your folder is complete, commit and push to your main branch with the following commit message:
Add Classwork 11 - The Mandelbrot Set

Submit the link of your repository through Teams.

Rubric

PPP.txt (complete, correct pseudocode)3Flowchart.png (iteration + decision flows)3mandelbrot_set_math.py (working program)3AI use declaration1Total10

Respuesta en crudo (raw):

¡Claro que sí! Basándome en la estructura de tus anteriores entregas y en las instrucciones específicas para la Classwork 11, he redactado la actualización para tu `README.md`.

También incluí la descripción técnica basándome en el material de tu clase sobre el Conjunto de Mandelbrot (Mandelbrot Set), que genera el archivo CSV con las iteraciones.

Puedes copiar y pegar el siguiente bloque directamente en tu archivo `README.md` dentro de la carpeta `Classwork-11-The-Mandelbrot-Set`:

```markdown
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

```

4. The program will process the complex plane iterations and output a file named `mandelbrot.csv` in the same directory.

## Submission Checklist & Rubric (10 Total Points)

* [ ] **3 pts**: `PPP.txt` is complete and formatted correctly.
* [ ] **3 pts**: `Flowchart.png` is exported as an image (ensure it is a `.png` and not a `.jpeg`).
* [ ] **3 pts**: `mandelbrot_set_math.py` runs properly with necessary comments.
* [ ] **1 pt**: AI Use Declaration included.
* [ ] **Commit message exact match**: `Add Classwork 11 - The Mandelbrot Set`

## AI Use Declaration

* **Nombre del estudiante:** Román Alonso Sosa Fiesco
* **IA utilizada:** Gemini
* **Fecha de uso:** 2026-06-26
* **Propósito:** Redactar y dar formato a la explicación del proyecto en el README.md basándose en los requerimientos de la rúbrica.

```

### 💡 Recordatorio importante para tu entrega:
Al revisar los archivos en tu entorno, noté que tienes un archivo llamado `CW11.py`. Recuerda que las instrucciones exigen que el código fuente se llame exactamente **`mandelbrot_set_math.py`**. ¡No olvides renombrar tu archivo antes de hacer el `git commit` y subirlo a GitHub para asegurar tus puntos!

```