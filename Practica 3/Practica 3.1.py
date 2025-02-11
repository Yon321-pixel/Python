class Conductor:
    def __init__(self, nombre, id_conductor):
        self.nombre = nombre
        self.id_conductor = id_conductor
        self.horarios = set()

    def asignar_horario(self, hora):
        if hora in self.horarios:
            return False
        self.horarios.add(hora)
        return True

class Bus:
    def __init__(self, id_bus):
        self.id_bus = id_bus
        self.ruta = None
        self.horarios = []
        self.conductor = None

    def asignar_ruta(self, ruta):
        self.ruta = ruta

    def registrar_horario(self, hora):
        if hora not in self.horarios:
            self.horarios.append(hora)
            return True
        return False

    def asignar_conductor(self, conductor):
        if any(hora in conductor.horarios for hora in self.horarios):
            return False
        self.conductor = conductor
        for hora in self.horarios:
            conductor.asignar_horario(hora)
        return True

class Admin:
    def __init__(self):
        self.buses = {}
        self.conductores = {}

    def agregar_bus(self, id_bus):
        if id_bus not in self.buses:
            self.buses[id_bus] = Bus(id_bus)
            return True
        return False

    def agregar_conductor(self, nombre, id_conductor):
        if id_conductor not in self.conductores:
            self.conductores[id_conductor] = Conductor(nombre, id_conductor)
            return True
        return False

    def mostrar_buses_asignados(self):
        for id_bus, bus in self.buses.items():
            if bus.conductor:
                horarios = ", ".join(bus.horarios) if bus.horarios else "Sin horarios"
                ruta = bus.ruta if bus.ruta else "Sin ruta asignada"
                print(f"Bus {id_bus} - Conductor: {bus.conductor.nombre}, Ruta: {ruta}, Horarios: {horarios}")
            else:
                print(f"Bus {id_bus} - Sin conductor asignado")

    def mostrar_menu(self):
        while True:
            print("\n1. Agregar Bus")
            print("2. Agregar Ruta a Bus")
            print("3. Registrar Horario a Bus")
            print("4. Agregar Conductor")
            print("5. Asignar Horario a Conductor")
            print("6. Asignar Bus a Conductor")
            print("7. Mostrar lista de buses asignados")
            print("8. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                id_bus = input("Ingrese ID del bus: ")
                if self.agregar_bus(id_bus):
                    print("Bus agregado correctamente.")
                else:
                    print("El bus ya existe.")
            elif opcion == "2":
                id_bus = input("Ingrese ID del bus: ")
                if id_bus in self.buses:
                    ruta = input("Ingrese la ruta: ")
                    self.buses[id_bus].asignar_ruta(ruta)
                    print("Ruta asignada correctamente.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "3":
                id_bus = input("Ingrese ID del bus: ")
                if id_bus in self.buses:
                    hora = input("Ingrese horario (HH:MM): ")
                    if self.buses[id_bus].registrar_horario(hora):
                        print("Horario registrado correctamente.")
                    else:
                        print("El horario ya está registrado para este bus.")
                else:
                    print("Bus no encontrado.")
            elif opcion == "4":
                id_conductor = input("Ingrese ID del conductor: ")
                nombre = input("Ingrese nombre del conductor: ")
                if self.agregar_conductor(nombre, id_conductor):
                    print("Conductor agregado correctamente.")
                else:
                    print("El conductor ya existe.")
            elif opcion == "5":
                id_conductor = input("Ingrese ID del conductor: ")
                if id_conductor in self.conductores:
                    hora = input("Ingrese horario (HH:MM): ")
                    if self.conductores[id_conductor].asignar_horario(hora):
                        print("Horario asignado correctamente.")
                    else:
                        print("El conductor ya tiene ese horario.")
                else:
                    print("Conductor no encontrado.")
            elif opcion == "6":
                id_bus = input("Ingrese ID del bus: ")
                id_conductor = input("Ingrese ID del conductor: ")
                if id_bus in self.buses and id_conductor in self.conductores:
                    if self.buses[id_bus].asignar_conductor(self.conductores[id_conductor]):
                        print("Conductor asignado correctamente al bus.")
                    else:
                        print("El conductor ya tiene un horario en conflicto.")
                else:
                    print("Bus o conductor no encontrado.")
            elif opcion == "7":
                self.mostrar_buses_asignados()
            elif opcion == "8":
                break
            else:
                print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    admin = Admin()
    admin.mostrar_menu()
