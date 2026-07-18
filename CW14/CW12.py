from PIL import Image

# Excepciones personalizadas 
class DimensionInconsistenteError(Exception):
    pass

class FormatoCSVIncorrectoError(Exception):
    pass

try:
    config = {}
    
    # CASO 2: No existe config.txt
    try:
        file = open("config.txt", "r")
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo config.txt")
        
    lines = file.readlines()
    for line in lines:
        if not line.strip(): 
            continue
        parameter, value = line.strip().split("=")
        config[parameter] = float(value) if "." in value else int(value)
    file.close()

    print(config)

    # CASO 3: No existe mandelbrot.csv
    try:
        archivo = open("mandelbrot.csv", "r")
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo mandelbrot.csv")
        
    lineas = archivo.readlines()
    archivo.close()

    # NO OLVIDAR QUITAR ENCABEZADOS
    if len(lineas) > 0:
        lineas.pop(0)

    # DESEMPAQUETAR VARIABLES
    max_iter = config["max_iter"]
    ancho = config["ancho"]
    alto = config["alto"]

    # CASO 1: Modo "L" (escala de grises)
    img = Image.new("L", (ancho, alto))

    for linea in lineas:
        # CASO 5: Fila de mandelbrot.csv mal formada
        try:
            partes = linea.strip().split(",")
            if len(partes) != 3:
                raise ValueError("Cantidad incorrecta de columnas")
                
            row, column, iterations = partes
            iterations = int(iterations)
            row = int(row)
            column = int(column)
        except ValueError:
            raise FormatoCSVIncorrectoError("El archivo mandelbrot.csv está mal formado.")
        
        # Lógica de brillo según el caso de prueba 1
        if iterations == max_iter:
            brillo = 0
        else:
            brillo = int((iterations / max_iter) * 255)
            
        # CASO 4: Coordenada fuera del tamaño de la imagen
        try:
            img.putpixel((column, row), brillo)
        except IndexError:
            raise DimensionInconsistenteError("El csv no es consistente con el ancho/alto del config.txt.")
    
    # En modo L se guarda directo sin convertir a RGB, aunque es opcional.
    img.save("mandelbrot.png")
    print("DONE")

except FileNotFoundError as e:
    print(e)
except DimensionInconsistenteError as e:
    print(e)
except FormatoCSVIncorrectoError as e:
    print(e)
except Exception as e:
    print("Ocurrió un error inesperado al visualizar el fractal.")