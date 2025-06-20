import matplotlib.pyplot as plt
import seaborn as sns

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

