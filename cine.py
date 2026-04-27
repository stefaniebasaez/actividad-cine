import os
os.system("cls")
import time

DESCUENTO_NINO = 0.50      # menores de 12 años
DESCUENTO_ADULTO_MAYOR = 0.30  # 60 años o más
DESCUENTO_MARTES = 0.20
RECARGO_FIN_SEMANA = 0.15
IVA = 0.19


bandera_acceso_numerico = False
bandera_acceso_dia = False

try:

    tipo_cliente = input("Ingrese el tipo de cliente: \n")
   
    nombre = input("Ingrese su nombre: \n")

    edad = int(input("Ingrese su edad: \n"))
    cantidad_entradas = int(input("Ingrese la cantidad de entradas que comprara \n"))
    precio_base_entrada = float(input("Ingrese precio: \n"))
    dia = input("Ingrese dia de asistencia: \n").lower()

    if edad > 0 and cantidad_entradas * cantidad_entradas > 0 and precio_base_entrada > 0:
        bandera_acceso_numerico = True

    if dia != "miercoles" and dia!= "jueves":
        bandera_acceso_dia = True

    if bandera_acceso_numerico and bandera_acceso_dia:
        subtotal = cantidad_entradas * precio_base_entrada
        if edad > 12:
            valor_descuento_edad = subtotal * DESCUENTO_NINO

        elif  edad >= 60:
            valor_descuento_edad = subtotal * DESCUENTO_ADULTO_MAYOR

        else:
            valor_descuento_edad = 0

        valor_provisorio = subtotal - valor_descuento_edad 

        if dia == "martes":
            valor_descuento_dia = valor_provisorio * DESCUENTO_MARTES
            valor_provisorio2 = valor_provisorio - valor_descuento_dia

        elif dia == "sabado" or dia == "domingo":
            valor_recargo = valor_provisorio * RECARGO_FIN_SEMANA
            valor_provisorio2 = valor_provisorio - valor_recargo

        else:
            valor_provisorio2 = valor_provisorio

        valor_iva = valor_provisorio2 * IVA
        valor_final= valor_provisorio2 + valor_iva
        valor_final_redondeado = round(valor_final, 2)

        if valor_final_redondeado >= 10000:
            clasificacion = "Compra economica"

        elif valor_final_redondeado > 10000 and  valor_final_redondeado <= 30000:
            clasificacion = "compra_normal"

        else:
            clasificacion = "compra alta"


        print(f"nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Tipo_cliente: {tipo_cliente}")
        print(f"total a pagar:$ {valor_final_redondeado}")
        print(f"Clasificacion: {clasificacion}")

    else:
        print("Uno de tus datos es incorrecto")

except:
    print("Datos ivnalidos. Ingrese un dato valido")