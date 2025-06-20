import pandas as pd
import sys
sys.path.append('../')
import chardet

def visuliza_duplicados(dataframe: pd.DataFrame, subset=None) -> pd.DataFrame:
    """
    Mostra registros duplicados em um DataFrame.

    Parâmetros:
        dataframe (pd.DataFrame): O DataFrame a ser analisado.
        subset (list[str], opcional): Lista de colunas para considerar como chave da duplicidade.

    Retorno:
        pd.DataFrame: As linhas duplicadas encontradas.
    """
    duplicados = dataframe.duplicated(subset=subset)
    total = duplicados.sum()
    
    if total > 0:
        print(f'Existem {total} registros duplicados.')
    else:
        print('Nenhum registro duplicado encontrado.')
    
    return dataframe[duplicados]


def visuliza_dados_NaN(dataframe: pd.DataFrame):
    """ 
    lista todos os registros que possuem dados faltantes do dataframe.
    
    Parâmetros
    ___
    dados: um dataframe

    Retorno
    ___
    Return: lista os registros com dados faltantes
    """
    ausentes = dataframe.isna().sum()
    print(f'Foram detectado {ausentes} dados NaN')
    return dataframe.isna()
    
def tipo_encoding(caminho):
    """
    Ferramenta para uxiliar na identificação do encoding do dataset

    Parâmetro
    ---
    str: caminho do dataset 

    Retorno
    ---
    Return: o tipo de encoding
    """
    with open(caminho, 'rb') as f:
        result = chardet.detect(f.read(10000))  # Lê os primeiros 10k bytes

    print(result)