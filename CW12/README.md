## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-07-03

Propósito: Redactar el README.md

Prompt utilizado:
Actualiza el README.md para que explique la Classwork #12 - The Mandelbrot Set
Vence hoy a las 23:59•
Se cierra hoy a las 23:59
UNIT 3
Instrucciones
Instructions

Inside your repository UPY-PROGRAMMING-NAME-LAST_NAME-Q2-2026, create a folder named exactly:

Classwork-12-The-Mandelbrot-Set

That folder must contain the following three files:

PPP.txt — your complete pseudocode following class rules: plain English, ← for assignment, # for comments, no Python syntax.
Flowchart.png — your flowchart exported as an image, covering the iteration flow for each method and the decision flow for the three modes.
mandelbrot_set_vis.py — your working Python program with # INPUT, # PROCESS, and # OUTPUT comments.
Once your folder is complete, commit and push to your main branch with the following commit message:
Add Classwork 12 - The Mandelbrot Set

Submit the link of your repository through Teams.

Rubric

PPP.txt (complete, correct pseudocode)3Flowchart.png (iteration + decision flows)3mandelbrot_set_vis.py (working program)3AI use declaration1Total10

Respuesta en crudo (raw):
¡Claro que sí! Siguiendo el mismo formato de tus entregas anteriores y tomando en cuenta que en la Classwork 12 se utiliza la librería PIL para procesar el CSV y visualizar el fractal, he redactado la actualización para tu `README.md`.

Puedes copiar y pegar el siguiente bloque al final de tu archivo `README.md` (o en la carpeta `Classwork-12-The-Mandelbrot-Set`):

```markdown
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

```

5. The program will process the CSV data and generate a new image file named `mandelbrot.png` in the same directory.

## Submission Checklist & Rubric (10 Total Points)

* [ ] **3 pts**: `PPP.txt` is complete and formatted correctly.
* [ ] **3 pts**: `Flowchart.png` is exported as an image (ensure it is a `.png` and not a `.jpeg`).
* [ ] **3 pts**: `mandelbrot_set_vis.py` runs properly with necessary comments.
* [ ] **1 pt**: AI Use Declaration included.
* [ ] **Commit message exact match**: `Add Classwork 12 - The Mandelbrot Set`

## AI Use Declaration

* **Nombre del estudiante:** Román Alonso Sosa Fiesco
* **IA utilizada:** Gemini
* **Fecha de uso:** 2026-07-03
* **Propósito:** Redactar y dar formato a la explicación técnica del proyecto en el README.md basándose en los requerimientos de la rúbrica y las instrucciones de visualización de datos con PIL.

```

### 💡 Nota importante para tu entrega:
Asegúrate de que tu código fuente en esta entrega se llame **`mandelbrot_set_vis.py`** (diferente al `mandelbrot_set_math.py` de la semana pasada) y de que el commit message sea exactamente `"Add Classwork 12 - The Mandelbrot Set"`. ¡Mucho éxito con la entrega!

```
