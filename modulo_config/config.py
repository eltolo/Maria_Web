import yaml

def cargar_configuracion(file_path="./Maria.yaml"):
    """
    Carga el archivo YAML y valida que las claves necesarias estén presentes.
    """
    try:
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)

        # Validar que las claves principales estén presentes
        modelos = ["llama3", "OpenAI"]
        claves_requeridas = ["inicial", "contexto", "temperatura", "max_tokens"]

        for modelo in modelos:
            if modelo not in config:
                print(f"ALERTA: El modelo {modelo} no está presente en el archivo YAML.")
            else:
                for clave in claves_requeridas:
                    if clave not in config[modelo]:
                        print(f"ALERTA: Falta la clave '{clave}' en el modelo {modelo}.")

        return config

    except yaml.YAMLError as e:
        print(f"Error al cargar el archivo YAML: {e}")
        return None
    except FileNotFoundError:
        print("Archivo YAML no encontrado.")
        return None


