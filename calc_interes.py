# Calculadora interes compuesto

tipo_interes = int(input("Tipo de interes anual: "))
años = int(input("Años: "))
capital_inicial = int(input("Capital inicial: "))
aportacion_anual = int(input("Aportación anual: "))

capital = capital_inicial + aportacion_anual
operacion_interes = tipo_interes / 100 + 1
año = 0

while año != años:
    interes_anual = capital * operacion_interes - capital
    capital += interes_anual + aportacion_anual
    año += 1
    #print(f"Interes año {año}: " + str(int(interes_anual)))

print("Intereses totales " + str(int(capital - capital_inicial)))
print("Capital total: " + str(int(capital - aportacion_anual)))