#Este componente se encarga exclusivamente de la ingesta, limpieza y validación de datos.
#Es el motor de datos
import pandas as pd
class IngestorDatos:
    """Componente independiente para la ingesta y validación de datos comerciales"""
    def __init__(self):
        pass

    def cargar_datos(self, archivo) -> pd.DataFrame:
        """Carga un archivo y valida que con la interfaz requerida"""

        # El bloque try, se usa junto con except para manejar errores
        # y excepciones de forma controlada, evitando que el código
        # se rompa abruptamente al suceder un error, definiendo
        # acciones alternativas.
        try:
            df = pd.read_csv(archivo, sep=None, engine='python', encoding='utf-8-sig')
            #Usamos a sep=None y el motor de 'python' para q Pandas detecte automaticamente si el archivo usa 
            #comas(,), puntos y comas (;), o tabuladores(\t)

            #Validamos el contrato de la interfaz (columnas requeridas)
            columnas_requeridas = {'fecha', 'producto', 'cantidad', 'precio_unitario'}
            if not columnas_requeridas.issubset(df .columns):
                raise ValueError(f"El archivo no cumple con el contrato. Columnas requeridas:{columnas_requeridas}")
            
            #Limpieza y conversión de tipos de datos
            df['fecha'] = pd.to_datetime(df['fecha'])
            df['total_venta'] = df['cantidad'] = df['precio_unitario']
            return df 
        except Exception as e:
            raise IOError(Si todo no funciono)
               
              
            
            