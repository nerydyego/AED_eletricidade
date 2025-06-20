import pandas as pd

def drop_duplicados(dataframe: pd.DataFrame):
    """ 
    Remove os dados duplicados do DataFrame.

    Parâmetros:
        dataframe (pd.DataFrame): DataFrame a ser tratado.

    Retorno:
        pd.DataFrame: DataFrame sem duplicatas.
    """
    dataframe.drop_duplicates(inplace=True)
    return dataframe

def limpa_dados_NAN(dataframe: pd.DataFrame):
    dataframe.dropna(inplace=True)
    return dataframe