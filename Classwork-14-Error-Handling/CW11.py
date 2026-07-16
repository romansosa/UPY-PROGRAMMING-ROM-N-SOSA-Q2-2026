# Excepciones personalizadas
class ConfiguracionMalFormadaError(Exception):
    pass

class DimensionInvalidaError(Exception):
    pass

try:
    config = {}
    
    # CASO 2: Archivo inexistente
    try:
        file = open("config.txt", "r")
    except FileNotFoundError:
        raise FileNotFoundError("No se encontró el archivo config.txt.")

    for line in file:
        line = line.strip()
        if not line:
            continue
            
        # CASO 3: Línea mal formada (sin '=')
        try:
            parameter, value = line.split("=")
        except ValueError:
            raise ConfiguracionMalFormadaError("El archivo de configuración está mal formado.")
            
        config[parameter] = float(value) if "." in value else int(value)
    file.close()

    # CASO 4: Faltan llaves requeridas
    requeridos = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]
    for req in requeridos:
        if req not in config:
            raise KeyError(f"Falta el parámetro '{req}' en config.txt.")

    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]

    # CASO 5: 'ancho' o 'alto' no son enteros
    if isinstance(width, float) or isinstance(height, float):
        raise DimensionInvalidaError("Los parámetros 'ancho' y 'alto' deben ser números enteros.")

    output = open("mandelbrot.csv", "w")
    output.write("row,column,iterations\n")

    for row in range(height):
        for column in range(width):
            real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)
            
            z = 0 + 0j
            iterations = 0
            
            while (abs(z) <= 2) and (iterations < max_iter):
                z = z * z + c
                iterations += 1
            
            output.write(f"{row},{column},{iterations}\n")
            
    output.close()
    print("Done")

except FileNotFoundError as e:
    print(e)
except ConfiguracionMalFormadaError as e:
    print(e)
except KeyError as e:
    print(e)
except DimensionInvalidaError as e:
    print(e)
except Exception as e:
    print("Ocurrió un error inesperado al procesar el conjunto de Mandelbrot.")