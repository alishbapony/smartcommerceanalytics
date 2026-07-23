#este componente se encargara exclusivamente de la ingesta, limpieza y la validación de los datos.
#es el motor de datos
import pandas as pd
class IngestorDatos:
    """ Componente independiente para la ingesta y la validación de datos comerciales"""
    def __init__(self):
        pass

    def cargar_datos(self, archivo) -> pd.DataFrame:
        """Carga un archivo y valida que cumpla con la interfaz que requerida"""
        """EL bloque try, se usa junto con except para manejar errores
        y execpciones de forma controlada, evitando que el codigo
        se ropa abruptamente al suceder un error, definiendo acciones alternativas"""
        try:
            df = pd.read_csv(archivo, sep=None, engine='python', encoding='utf-8-sig')
            #usamos sep=none y el motor de 'python' para que puedas detecte
            #automaticamente si el archivo usa comas, puntos y comas o puntos o tabuladores
            
            #validamos el contrato de la interfaz
            columnas_requeridas = {'fecha', 'producto', 'cantidad', 'precio_unitario'}
            if not columnas_requeridas.issubset(df.columns):
                raise ValueError(f"El archivo no cumple con el contrato. Columnas requeridas:{columnas_requeridas}")

            #Limpieza conversion de tipos de datos
            df['fecha'] = pd.to_datetime(df['fecha'])
            df['total_venta'] = df['cantidad'] * df['precio_unitario']
            return df
        except Exception as e:
            raise IOError(f"Error al procesar  el componente de datos: {e}")