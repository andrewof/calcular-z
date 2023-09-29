import scipy.stats as stats

def calcular_Z():
    valor = input('Digite el percentil: ')
    valor_z = 0

    if valor.isdigit():
        percentil_entero = int(valor)
        valor_z = stats.norm.ppf(percentil_entero / 100)
    else:
        try:
            percentil_decimal = float(valor)
            valor_z = stats.norm.ppf(percentil_decimal)
        except ValueError:
            print('Ha ocurrido un error al intentar calcular el valor de z')
    return valor_z
            

if __name__ == '__main__':
    print(calcular_Z())