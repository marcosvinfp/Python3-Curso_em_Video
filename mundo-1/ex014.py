temperatura_celsius = float(input('Informe a temperatura em °C: '))
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
temperatura_kelvin = temperatura_celsius + 273.15

print(f'A temperatura de {temperatura_celsius:.1f} °C corresponde a {temperatura_fahrenheit:.1f} °F e a {temperatura_kelvin:.1f} K!')
