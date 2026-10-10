#NICOLA STORNELLI ORTIZ
#GRUPO   (213022B_2204)
#INGENIRIA DE IA Y CIENCIA DE DATOS
#CODIGO FUENTE : AUTORIA PROPIA 

import sys

# Definir la constante IVA
IVA = 0.19

def main():
    print("--- SISTEMA DE CÁLCULO DE PRECIO DE PRODUCTOS ---")
    
    # Solicitar el precio base del producto con validación de errores
    try:
        precio_base = float(input("Ingrese el precio base del producto: "))
    except ValueError:
        print("Error: Debe ingresar un valor numérico válido.")
        sys.exit()
        
    # Validar si el precio es menor o igual a 0
    if precio_base <= 0:
        print("Error: El precio base debe ser mayor a cero.")
        sys.exit()
        
    # Solicitar el código de categoría
    print("\nSeleccione la categoría del producto:")
    print("1. Producto básico (No paga IVA)")
    print("2. Producto estándar (Paga IVA del 19%)")
    print("3. Producto de lujo (Paga IVA del 19% + recargo del 5%)")
    
    categoria = input("Ingrese el código de la categoría (1, 2 o 3): ")
    
    # Calcular y asignar el valor final según la categoría
    if categoria == "1":
        valor_final = precio_base
        detalle = "Producto básico (0% impuesto)"
    elif categoria == "2":
        valor_final = precio_base * (1 + IVA)
        detalle = "Producto estándar (19% IVA)"
    elif categoria == "3":
        recargo = 0.05
        valor_final = precio_base * (1 + IVA + recargo)
        detalle = "Producto de lujo (19% IVA + 5% recargo)"
    else:
        print("Error: Código de categoría inválido.")
        sys.exit()
        
    # Mostrar los resultados en pantalla
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"Categoría elegida: {detalle}")
    print(f"Precio base: ${precio_base:,.2f}")
    print(f"Valor final a pagar: ${valor_final:,.2f}")

if __name__ == "__main__":
    main()