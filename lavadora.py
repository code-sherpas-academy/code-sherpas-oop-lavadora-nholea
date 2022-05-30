class Lavadora():
    total_ropa = 0
    is_active = False
    detergente = False
    suavizante = False

    def __init__(self, marca, modelo, capacidad):
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def introducir_ropa(self):
        if self.total_ropa < self.capacidad:
            self.total_ropa += 1
            return "Se ha incrementado 1kg el peso de la ropa"
        else:
            return "Capacidad máxima alcanzada"

    def sacar_ropa(self):
        if self.total_ropa !=0:
            self.total_ropa -=1
            return "Se ha reducido 1kg el peso de la ropa"

    def encender(self):
        self.is_active = True

    def apagar(self):
        self.is_active = False

    def agregar_detergente(self):
        self.detergente = True

    def agregar_suavizante(self):
        self.suavizante = False

    def programa_lavado(self, programa):
        programas = ["rápido", "normal", "delicado"]
        if programa in programas:
            return programa
        return "Programa seleccionado es erróneo"

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.capacidad}"

        

if __name__ == "__main__":
    lavadora = Lavadora("Miele", "WCA020 WCS Active", 7)
    print(lavadora.marca)
    print(lavadora.modelo)
    print(lavadora.capacidad)
    print(lavadora.introducir_ropa())
    print(lavadora.introducir_ropa())
    print(lavadora.introducir_ropa())
    print(lavadora.introducir_ropa())
    print(lavadora.sacar_ropa())
    print(lavadora.sacar_ropa())
    print(lavadora.total_ropa)
    print(lavadora.programa_lavado("delicado"))
    lavadora.encender()
    print(lavadora.is_active)


        
        