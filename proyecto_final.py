class Votacion:
    def __init__(self):
        self.candidatos = {}
        self.votantes = {}

    def registrar_candidato(self, cedula, nombre):
        if cedula not in self.candidatos:
            self.candidatos[cedula] = {"nombre": nombre, "votos": 0}
            print(f"Se ha registrado al candidato {nombre}.")
        else:
            print("Este candidato ya está registrado.")

    def listar_candidatos(self):
        print("Candidatos registrados:")
        for cedula, candidato in self.candidatos.items():
            print(f"Cédula: {cedula}, Nombre: {candidato['nombre']}")

    def votar(self, cedula, candidato_cedula):
        if cedula not in self.votantes:
            if candidato_cedula in self.candidatos:
                self.candidatos[candidato_cedula]["votos"] += 1
                self.votantes[cedula] = {"voto": candidato_cedula}
                print("¡Voto registrado con éxito!")
            else:
                print("Candidato no encontrado.")
        else:
            print("Ya has votado antes.")

    def ver_propuestas(self, cedula):
        candidato_cedula = self.votantes.get(cedula, {}).get("voto")
        if candidato_cedula:
            candidato = self.candidatos[candidato_cedula]
            print(f"Propuestas del candidato {candidato['nombre']} (Cédula: {candidato_cedula}):")
            # acá se agregan las propuestas.
        else:
            print("Primero debes votar por un candidato.")


votacion = Votacion()

while True:
    print("\nOpciones:")
    print("1. Registrar Candidato")
    print("2. Listar Candidatos")
    print("3. Votar")
    print("4. Ver Propuestas de Candidato")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        cedula = input("Ingrese la cédula del candidato: ")
        nombre = input("Ingrese el nombre del candidato: ")
        votacion.registrar_candidato(cedula, nombre)
    elif opcion == "2":
        votacion.listar_candidatos()
    elif opcion == "3":
        cedula = input("Ingrese su cédula: ")
        candidato_cedula = input("Ingrese la cédula del candidato al que desea votar: ")
        votacion.votar(cedula, candidato_cedula)
    elif opcion == "4":
        cedula = input("Ingrese su cédula para ver las propuestas del candidato seleccionado: ")
        votacion.ver_propuestas(cedula)
    elif opcion == "5":
        print("¡Gracias por participar en las votaciones!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")