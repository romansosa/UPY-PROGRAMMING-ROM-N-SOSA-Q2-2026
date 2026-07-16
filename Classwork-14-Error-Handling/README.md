## AI Use Declaration
Nombre del estudiante: Román Alonso Sosa Fiesco

IA utilizada: Gemini

Fecha de uso: 2026-07-03

Propósito: Redactar el README.md

Prompt utilizado:
Actualiza el md para incluir lo de la classwork 14

Respuesta en crudo (raw):
Aquí tienes la sección redactada para la Classwork 14, manteniendo la misma estructura y estilo en inglés para las descripciones técnicas que has usado en tus entregas anteriores, y con la declaración de uso de IA actualizada al día de hoy.

Puedes copiar y pegar este bloque directamente al final de tu archivo `README.md`:

```markdown
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

3. Try deliberately triggering errors (e.g., grading a non-existent student, deleting `config.txt`, or corrupting `mandelbrot.csv`) to observe the clean error messages instead of standard Traceback crashes.

## Submission Checklist & Rubric

* [ ] **cw10.py** correctly implements `try/except` and custom exceptions.
* [ ] **CW11.py** correctly implements `try/except` and custom exceptions.
* [ ] **CW12.py** correctly implements `try/except` and custom exceptions.
* [ ] AI Use Declaration included.
* [ ] **Commit message exact match**: `Add Classwork 14 - Error Handling`

---

## AI Use Declaration

* **Nombre del estudiante:** Román Alonso Sosa Fiesco
* **IA utilizada:** Gemini
* **Fecha de uso:** 2026-07-15
* **Propósito:** Redactar y dar formato a la explicación técnica del proyecto de manejo de errores en el README.md basándose en los tres scripts refactorizados de la Classwork 14.

```

```