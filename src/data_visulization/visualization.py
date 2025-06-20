import pandas as pd

def visuliza_duplicados(dataframe: pd.DataFrame):
    """ 
    Função responsável por mostrar os dados duplicados do dataframe.
    
    Parâmetros
    ___
    dados: um dataframe

    Retorno
    ___
    Return: lista os registros em duplicidade
    """
    duplicados = dataframe.duplicated().sum()
    print(f' Existem {duplicados} Dados duplicados')
    filtro_duplicados = dataframe.duplicated()
    return dataframe[filtro_duplicados]


def visuliza_dados_NaN(dataFrame: pd.DataFrame):
    """ 
    lista todos os registros que possuem dados faltantes do dataframe.
    
    Parâmetros
    ___
    dados: um dataframe

    Retorno
    ___
    Return: lista os registros com dados faltantes
    """
    return dataFrame.isna()
    