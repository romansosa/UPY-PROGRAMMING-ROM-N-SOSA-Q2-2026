# Excepciones personalizadas (Reglas de negocio)
class TerminacionInvalidaError(Exception):
    pass

class VerboInvalidoError(Exception):
    pass

# Required structures
pronouns = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]

endings = {
    "ar" : ["o", "as", "a", "amos", "ais", "an"],
    "er" : ["o", "es", "e", "emos", "eis", "en"],
    "ir" : ["o", "es", "e", "imos", "is", "en"],
}

try:
    # INPUT
    verb = input("Escribe un verbo en español (ar/er/ir): ").strip().lower()

    # Validaciones de entrada
    if not verb:
        raise VerboInvalidoError("No escribiste ningún verbo.")
        
    if not verb.isalpha():
        raise VerboInvalidoError("El verbo ingresado no es válido (solo debe contener letras).")
        
    if len(verb) < 2:
        raise VerboInvalidoError("El texto ingresado es demasiado corto para ser un verbo.")

    stem = verb[:-2] # Get the stem
    ending = verb[-2:] # Get the ending

    # Regla de negocio: Terminación válida
    if ending not in endings:
        raise TerminacionInvalidaError("El verbo debe terminar estrictamente en 'ar', 'er' o 'ir'.")

    # PROCESS
    conjugations = endings[ending]

    # OUTPUT
    for index, pronoun in enumerate(pronouns):
        termination = conjugations[index]
        print(f"{pronoun} {stem}{termination}")


except VerboInvalidoError as e:
    print(e)
except TerminacionInvalidaError as e:
    print(e)
except Exception:
    print("Ocurrió un error inesperado al intentar conjugar el verbo.")