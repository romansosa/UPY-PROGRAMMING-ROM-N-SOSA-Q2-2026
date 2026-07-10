class DigitoApocrifo(Exception):
    pass


rol = input("Escribe el rol: ")
    

partes = rol.split("-")
if len(partes) != 2:
    print("No tiene el formato XXXXXXXXX-X")
else:
    rol_sin_digito, digito = partes
        
   
    if not rol_sin_digito.isdigit():
        print("Los digitos del rol deben ser numéricos")
    elif not digito.isdigit():
        print("El digito verificador debe ser numérico")
    else:
        
        inverso = rol_sin_digito[::-1]
        secuencia = [2, 3, 4, 5, 6, 7]
        suma = 0

        for index in range(len(inverso)):
            numero = int(inverso[index])
            suma += numero * secuencia[index % 6]

        resultado = suma % 11
        verificador = 11 - resultado

        
        try: 
            if int(digito) != verificador:
                
                raise DigitoApocrifo(f"El dígito verificador no conicide, se esperaba {verificador}")
            
           
            print(f"{rol_sin_digito}-{verificador}")
            
        except DigitoApocrifo as e:
            
            print(e)