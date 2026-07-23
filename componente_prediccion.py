#Componente automatico que realiza los cálculos de la estimación del invertario futuro.ç
import pandas as pd 
import numpy as np

#Crear la clase principal del motor de predicción
class MotorPrediccion:
    """Componente analítico para estimar la demanda futura del inventario"""
    def __init__(self, incremento_simulado=0.15):
        self.incremento = incremento_simulado

    def predecir_demanda(self, df_historico: pd.DataFrame) -> pd.DataFrame:
        """
        Toma datos históricos y estima el stock necesario para el próximo mes.
        Lógica del componente aislada del UT.
        """
        if df_historico.empty:
            return pd.DataFrame()
        
        # Agrupamos por producto
        ventas_promedio = df_historico.groupby('producto')['cantidad'].mean().reset_index()

        #Aplicamos la formula matematica de stock sugerido (Demanda + Margen de seguridad)
        ventas_promedio['stock_sugerido'] = np.ceil(ventas_promedio['cantidad'] * (1 + self.incremento)).astype(int)
        ventas_promedio.rename(columns={'cantidad': 'promedio_historico'}, inplace=True)
        return round(ventas_promedio, 2)