import math

# Excepciones personalizadas (Reglas de negocio)
class LimitesInvertidosError(Exception):
    pass

class MetodoInvalidoError(Exception):
    pass

try:
    # INPUT A
    a_input = input("Escribe el límite izquierdo del intervalo (a): ")
    try:
        if "pi" in a_input:
            a = eval(a_input.replace("pi", str(math.pi)))
        else:
            a = float(a_input)
    except Exception:
        raise ValueError("El límite inferior debe ser numérico")

    # INPUT B
    b_input = input("Escribe el límite derecho del intervalo (b): ")
    try:
        if "pi" in b_input:
            b = eval(b_input.replace("pi", str(math.pi)))
        else:
            b = float(b_input)
    except Exception:
        raise ValueError("El límite superior debe ser numérico")

    # Regla de negocio: Límites invertidos (Caso 14)
    if a >= b:
        raise LimitesInvertidosError("El límite inferior debe ser menor que el límite superior")

    # INPUT F_X
    f_x = input("Escribe la función a integrar f(x): ").strip()
    
    # Validación de función vacía (Caso 10)
    if not f_x:
        raise ValueError("La función ingresada no es válida")
        
    # Validación de operador de potencia correcto (Caso 12)
    if "^" in f_x:
        raise ValueError("La función ingresada no es válida")

    # Validación de variable "x" (Caso 11)
    try:
        x = a
        # Se hace una prueba inicial de evaluación controlada
        eval(f_x)
    except NameError as e:
        if "name 'x'" not in str(e) and "math" not in str(e):
            raise ValueError("La función debe estar escrita en términos de x")
        else:
            raise ValueError("La función ingresada no es válida")
    except ZeroDivisionError:
        pass # Se permite aquí porque se atrapará punto por punto en el ciclo (Caso 13)
    except Exception:
        raise ValueError("La función ingresada no es válida")

    # INPUT METHOD
    method = input("Selecciona el método de integración (LRM/RRM/MPM/TM): ").strip().upper()
    
    # Validación de método (Caso 15)
    if method not in ["LRM", "RRM", "MPM", "TM"]:
        raise MetodoInvalidoError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")

    # PROCESS
    area = 0.0
    n = 1000
    h = (b - a) / n
    shift = 0
    constant = 0

    if method == "RRM":
        shift = 1
        
    if method == "MPM":
        constant = h / 2

    if method == "TM":
        shift = 1

    for i in range(0 + shift, n + shift):
        xi = a + i * h + constant
        
        x = xi
        try:
            height = eval(f_x)
        except ZeroDivisionError:
            raise ZeroDivisionError("La función no está definida en algún punto del intervalo")
            
        if method == "TM":
            area += 2 * height * h
        else:
            area += height * h
            
    if method == "TM":
        x = a
        try:
            fa = eval(f_x)
            x = b
            fb = eval(f_x)
        except ZeroDivisionError:
            raise ZeroDivisionError("La función no está definida en algún punto del intervalo")
        area = (area + (fa * h) + (fb * h)) / 2
        
    # OUTPUT (Ajustado a 3 decimales)
    print(f"La integración de {f_x} es {area:.3f}")


except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except LimitesInvertidosError as e:
    print(e)
except MetodoInvalidoError as e:
    print(e)
except Exception:
    print("La función ingresada no es válida")