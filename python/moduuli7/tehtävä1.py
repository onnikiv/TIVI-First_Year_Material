vuoden_ajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kysytty_kk_numero = int(input("Anna kuukauden numero (1-12):\n "))

vuoden_aika = vuoden_ajat[kysytty_kk_numero - 1]
print(f"{kysytty_kk_numero} kuukausi on vuodenaikaa: {vuoden_aika}")
