
class Nodo:
    def __init__(self, nombre, es_directorio=False):
        self.nombre = nombre
        self.es_directorio = es_directorio
        self.archivos = []  # Lista de archivos y subdirectorios
        self.contenido = ""  # Contenido del archivo si no es un directorio

class SistemaArchivos:
    def __init__(self):
        self.directorio_raiz = Nodo("/", es_directorio=True)  # Directorio raíz
        self.directorio_actual = self.directorio_raiz

    def ls(self):
        contenido = []
        for archivo in self.directorio_actual.archivos:
            contenido.append(archivo.nombre)
        return contenido

    def mkdir(self, nombre):
        nuevo_directorio = Nodo(nombre, es_directorio=True)
        self.directorio_actual.archivos.append(nuevo_directorio)

    def cd(self, nombre):
        if nombre == "..":
            if self.directorio_actual != self.directorio_raiz:
                self.directorio_actual = self.directorio_raiz
        else:
            for archivo in self.directorio_actual.archivos:
                if archivo.nombre == nombre and archivo.es_directorio:
                    self.directorio_actual = archivo
                    break

    def touch(self, nombre):
        nuevo_archivo = Nodo(nombre)
        self.directorio_actual.archivos.append(nuevo_archivo)


sistema_archivos = SistemaArchivos()


while True:
    comando = input(f"{sistema_archivos.directorio_actual.nombre}$ ")
    partes = comando.split()
    if partes[0] == "ls":
        print(sistema_archivos.ls())
    elif partes[0] == "mkdir":
        sistema_archivos.mkdir(partes[1])
    elif partes[0] == "cd":
        sistema_archivos.cd(partes[1])
    elif partes[0] == "touch":
        sistema_archivos.touch(partes[1])
    elif partes[0] == "exit":
        break
    else:
        print("Comando no reconocido")

print("Saliendo del simulador de sistema de archivos")
                                                             