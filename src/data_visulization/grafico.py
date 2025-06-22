import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def grafico_consumo_por_ano_estados(df, ano):
    data = ano
    df_filtro = df[df['ano'] == data]

    # Agrupa por região e soma o consumo
    df_agrupado = df_filtro.groupby('sigla_uf')['consumo'].sum().reset_index()

    # Cria gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_agrupado, x='sigla_uf', y='consumo', palette='Blues_d')
    plt.title(f'Consumo de energia por região - {data}')
    plt.xlabel('Região')
    plt.ylabel('Consumo (MWh)')
    plt.tight_layout()
    plt.show()

def grafico_consumo_por_ano_estados(df, ano):
    """
    Gera gráfico de barras com o consumo de energia por estado em um determinado ano.

    Parâmetros:
        df (pd.DataFrame): DataFrame com colunas 'ano', 'sigla_uf', 'consumo'
        ano (int): Ano desejado

    Retorno:
        None
    """
    # Filtra o ano
    df_filtro = df[df['ano'] == ano]

    # Agrupa por estado e soma o consumo
    df_agrupado = df_filtro.groupby('sigla_uf')['consumo'].sum().reset_index()

    # Cria gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_agrupado, x='sigla_uf', y='consumo', palette='Blues_d')
    plt.title(f'Consumo de energia por estado - {ano}')
    plt.xlabel('Estado')
    plt.ylabel('Consumo (MWh)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_consumo_por_estado(df, sigla_uf):
    """
    Gera gráfico de linha mostrando a evolução do consumo de energia por estado ao longo dos anos.

    Parâmetros:
        df (pd.DataFrame): DataFrame com colunas 'ano', 'sigla_uf' e 'consumo'
        sigla_uf (str): Sigla do estado (ex: 'SP', 'RJ')

    Retorno:
        None
    """
    # Padroniza a sigla recebida para comparação (evita erros com letras minúsculas)
    sigla_uf = sigla_uf.upper().strip()

    # Filtra o DataFrame pelo estado
    df_filtro = df[df['sigla_uf'] == sigla_uf]

    if df_filtro.empty:
        print(f"Nenhum dado encontrado para o estado '{sigla_uf}'.")
        return

    # Agrupa por ano e soma o consumo
    df_agrupado = df_filtro.groupby('ano')['consumo'].sum().reset_index()
    df_agrupado['ano'] = df_agrupado['ano'].astype(str)

    # Gráfico de linha
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_agrupado, x='ano', y='consumo', marker='o')
    plt.title(f'Evolução do consumo de energia - {sigla_uf}')
    plt.xlabel('Ano')
    plt.ylabel('Consumo (MWh)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def grafico_consumo_mensal_por_estado(df, sigla_uf, ano):
    """
    Gera gráfico de barras mostrando o consumo mensal de energia para um estado em um ano.

    Parâmetros:
        df (pd.DataFrame): DataFrame com colunas 'ano', 'mes', 'sigla_uf' e 'consumo'
        sigla_uf (str): Sigla do estado (ex: 'SP')
        ano (int): Ano desejado

    Retorno:
        None
    """
    sigla_uf = sigla_uf.upper().strip()
    
    # Filtra pelos parâmetros
    df_filtro = df[(df['sigla_uf'] == sigla_uf) & (df['ano'] == ano)]

    if df_filtro.empty:
        print(f"Nenhum dado encontrado para {sigla_uf} no ano {ano}.")
        return

    # Agrupa por mês
    df_mensal = df_filtro.groupby('mes')['consumo'].sum().reset_index()

    # Ordena os meses (se forem numéricos ou texto)
    if df_mensal['mes'].dtype == 'O':  # object (texto)
        ordem_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                       'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        df_mensal['mes'] = pd.Categorical(df_mensal['mes'], categories=ordem_meses, ordered=True)
    else:
        df_mensal = df_mensal.sort_values('mes')

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_mensal, x='mes', y='consumo', palette='Blues_d')
    plt.title(f'Consumo mensal de energia - {sigla_uf} ({ano})')
    plt.xlabel('Mês')
    plt.ylabel('Consumo (MWh)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_dispersao_consumo_anual(df):
    """
    Gera gráfico de dispersão do consumo anual por estado.

    Parâmetros:
        df (pd.DataFrame): DataFrame com colunas 'ano', 'sigla_uf' e 'consumo'

    Retorno:
        None
    """
    # Agrupa os dados por ano e estado
    df_agrupado = df.groupby(['ano', 'sigla_uf'])['consumo'].sum().reset_index()
    df_agrupado['ano'] = df_agrupado['ano'].astype(str)

    # Gráfico de dispersão
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df_agrupado, x='ano', y='consumo', hue='sigla_uf', palette='tab20', s=80)

    plt.title('Dispersão do consumo anual de energia por estado')
    plt.xlabel('Ano')
    plt.ylabel('Consumo total (MWh)')
    plt.legend(title='Estado', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()

def consumidores_por_regiao_ano(df: pd.DataFrame, ano_escolhido: int) -> None:
    """
    Gera um gráfico de barras mostrando o número total de consumidores por região para um ano específico.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo os dados com, pelo menos, as colunas 'ano', 'regiao' e 'numero_consumidores'.
    ano_escolhido : int
        Ano para o qual o gráfico será gerado.

    Retorno
    -------
    None
        Exibe um gráfico de barras com o número de consumidores por região no ano especificado.

    Exemplo de uso
    --------------
    consumidores_por_regiao_ano(df_final, 2010)
    """
    # Filtra o DataFrame para o ano escolhido
    df_ano = df[df['ano'] == ano_escolhido]

    if df_ano.empty:
        print(f"Nenhum dado encontrado para o ano {ano_escolhido}. Verifique o dataset.")
        return

    # Agrupa por região somando o número de consumidores
    df_agrupado = df_ano.groupby('regiao')['numero_consumidores'].sum().reset_index()

    # Cria o gráfico de barras
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(data=df_agrupado, x='regiao', y='numero_consumidores', palette='Set2')
    plt.title(f'Número de Consumidores por Região - Ano {ano_escolhido}')
    plt.xlabel('Região')
    plt.ylabel('Número de Consumidores')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adiciona os valores numéricos acima de cada barra
    for p in ax.patches:
        altura = p.get_height()
        ax.annotate(f'{int(altura):,}',  # Formata com separador de milhar
                    (p.get_x() + p.get_width() / 2, altura),
                    ha='center', va='bottom',
                    fontsize=10, color='black',
                    xytext=(0, 5),
                    textcoords='offset points')

    plt.tight_layout()
    plt.show()

def correlacao_consumo_consumidores_por_estado(df: pd.DataFrame, estado_escolhido: str) -> None:
    """
    Gera um gráfico de dispersão com linha de regressão mostrando a correlação entre
    número de consumidores e consumo total ao longo dos anos para um estado específico.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame com colunas 'estado', 'ano', 'numero_consumidores' e 'consumo'.
    estado_escolhido : str
        Nome do estado para o qual o gráfico será gerado.

    Retorno
    -------
    None
        Exibe o gráfico de dispersão com regressão.
    """
    # Filtra o dataframe pelo estado escolhido
    df_estado = df[df['estado'] == estado_escolhido]

    if df_estado.empty:
        print(f"Nenhum dado encontrado para o estado '{estado_escolhido}'. Verifique o nome e tente novamente.")
        return

    # Agrupa os dados por ano somando consumidores e consumo
    df_agrupado = df_estado.groupby('ano').agg({
        'numero_consumidores': 'sum',
        'consumo': 'sum'
    }).reset_index()

    plt.figure(figsize=(10, 6))
    sns.regplot(data=df_agrupado, x='numero_consumidores', y='consumo',
                scatter_kws={'s': 70, 'alpha': 0.7}, line_kws={'color': 'red'})

    plt.title(f'Correlação entre Número de Consumidores e Consumo Total por Ano\nEstado: {estado_escolhido}')
    plt.xlabel('Número Total de Consumidores')
    plt.ylabel('Consumo Total de Energia (MWh)')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()

def detectar_outliers_consumo_iqr(df: pd.DataFrame):
    """
    Detecta outliers no consumo por estado e ano usando o método do IQR.
    
    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo pelo menos as colunas: 'estado', 'ano' e 'consumo'.

    Retorno
    -------
    pd.DataFrame
        DataFrame contendo os registros identificados como outliers.
    """

    # Função auxiliar para identificar outliers em um grupo
    def outliers_por_grupo(grupo):
        Q1 = grupo['consumo'].quantile(0.25)
        Q3 = grupo['consumo'].quantile(0.75)
        IQR = Q3 - Q1
        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR
        # Filtra os outliers
        outliers = grupo[(grupo['consumo'] < limite_inferior) | (grupo['consumo'] > limite_superior)]
        return outliers

    # Aplica o filtro para cada grupo (estado + ano)
    outliers_df = df.groupby(['estado', 'ano']).apply(outliers_por_grupo).reset_index(drop=True)

    if outliers_df.empty:
        print("Nenhum outlier encontrado no dataset.")
    else:
        print(f"Foram encontrados {len(outliers_df)} outliers no consumo.")

    return outliers_df


def plotar_outliers_boxplot(df: pd.DataFrame, estado: str, ano: int):
    """
    Plota boxplot do consumo para um estado e ano específicos destacando outliers.
    
    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame com os dados.
    estado : str
        Estado a ser plotado.
    ano : int
        Ano a ser plotado.
    """
    df_filtrado = df[(df['estado'] == estado) & (df['ano'] == ano)]

    if df_filtrado.empty:
        print(f"Nenhum dado para o estado {estado} no ano {ano}.")
        return

    plt.figure(figsize=(6, 8))
    sns.boxplot(y=df_filtrado['consumo'], color='lightblue')
    plt.title(f'Consumo - Estado: {estado} | Ano: {ano}')
    plt.ylabel('Consumo (MWh)')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def top10_consumo_estados_ano(df: pd.DataFrame, ano_escolhido: int) -> pd.DataFrame:
    """
    Gera uma tabela e um gráfico de barras verticais dos 10 estados que mais consumiram energia em um ano específico.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo as colunas 'ano', 'estado' e 'consumo'.
    ano_escolhido : int
        Ano para filtrar os dados.

    Retorno
    -------
    pd.DataFrame
        DataFrame com os 10 estados com maior consumo no ano especificado.
    """

    # Filtra pelo ano
    df_ano = df[df['ano'] == ano_escolhido]

    if df_ano.empty:
        print(f"Nenhum dado encontrado para o ano {ano_escolhido}.")
        return None

    # Agrupa por estado e soma o consumo
    df_agrupado = df_ano.groupby('estado')['consumo'].sum().reset_index()

    # Ordena e seleciona top 10
    df_top10 = df_agrupado.sort_values(by='consumo', ascending=False).head(10)

    # Exibe a tabela no console
    print(f"\nTop 10 estados que mais consumiram energia em {ano_escolhido}:\n")
    print(df_top10)

    # Gráfico de barras verticais
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(data=df_top10, x='estado', y='consumo', palette='mako')
    plt.title(f'Top 10 Estados que Mais Consumiram Energia em {ano_escolhido}')
    plt.xlabel('Estado')
    plt.ylabel('Consumo Total (MWh)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Adiciona os valores no topo das barras
    for p in ax.patches:
        altura = p.get_height()
        ax.annotate(f'{int(altura):,}',
                    (p.get_x() + p.get_width() / 2, altura),
                    ha='center', va='bottom',
                    fontsize=9, color='black',
                    xytext=(0, 5),
                    textcoords='offset points')

    plt.tight_layout()
    plt.show()

    return df_top10

def mapa_calor_correlacao(df: pd.DataFrame):
    """
    Gera um mapa de calor (heatmap) da correlação entre variáveis numéricas do DataFrame.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame contendo colunas numéricas como 'consumo' e 'numero_consumidores'.

    Retorno
    -------
    None
        Exibe o heatmap.
    """
    # Seleciona apenas colunas numéricas
    colunas_numericas = df.select_dtypes(include=['int64', 'float64'])

    # Calcula a matriz de correlação
    matriz_correlacao = colunas_numericas.corr()

    # Gera o heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(matriz_correlacao, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Mapa de Calor da Correlação entre Variáveis Numéricas')
    plt.tight_layout()
    plt.show()