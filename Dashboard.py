# tentativa 

#### Importando os pacotes: 


from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template



# Importando os dados necessários 

custeio_sem_extrativismo = pd.read_excel('https://github.com/jpeconomia/Dados-de-Cr-dito-Rural/raw/main/Custeio%20sem%20extrativismo.xlsx')

investimento_lavoura_permanente = pd.read_excel('https://github.com/jpeconomia/Dados-de-Cr-dito-Rural/raw/main/Investimento%20lavoura%20permanente.xlsx')

custeio_para_extrativismo = pd.read_excel('https://github.com/jpeconomia/Dados-de-Cr-dito-Rural/raw/main/Custeio%20com%20extrativismo.xlsx')

# Espécies selecionadas: 

especies = ['MADEIRA',
            'SERINGUEIRA',
            'CACAU',
            'ERVA-MATE',
            'COCO',
            'DENDÊ',
            'CAJU',
            'AÇAÍ',
            'CARNAÚBA',
            'PUPUNHA',
            'URUCUM',
            'ACEROLA',
            'CEDRO',
            'COCO-DA-BAIA',
            'GRAVIOLA',
            'GUARANÁ',
            'CUPUAÇU',
            'CARAMBOLA',
            'CAJÁ',
            'AGAVE (SISAL)',
            'CASTANHA-DO-BRASIL',
            'TAPEREBÁ',
            'MURICI',
            'ANDIROBA',
            'PARICÁ',
            'ARAUCÁRIA']


# Iniciar aplicativo 

m1 = {'display': 'inline-block','width':'50%'}


dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL, dbc_css])
load_figure_template('JOURNAL')

server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = dbc.Container([
    
    html.H1(children = 'Crédito Rural'),
    
    html.H3(children = 'Dados sobre crédito de custeio e de investimento fornecidos pelo SICOR.'),
    
    html.H5(children = 'Para os dados de Custeio, o extrativismo foi excluído e, para os de investimento, foram considerados os dados de crédito para lavoura perene'),
    
    html.H5(children = 'Lista de Gráficos:'),
    
    html.P(children = 'Gráfico 1: Custeio total e regiões'),
    
    html.P(children = 'Gráfico 2: Investimento total e regiões'),
    
    html.P(children = 'Gráfico 3: Custeio por produtos e regiões'),
    
    html.P(children = 'Gráfico 4: Investimento por produtos e regiões'),
    
    html.P(children = 'Gráfico 5: Custeio total por estado'),
    
    html.P(children = 'Gráfico 6: Investimento total por estado'),
    
    html.P(children = 'Gráfico 7: Custeio por produto e por estado'),
    
    html.P(children = 'Gráfico 8: Investimento por produto e por estado'),
    
    html.P(children = 'Gráfico 9: Custeio por produto ao longo dos anos'),
    
    html.P(children = 'Gráfico 10: Investimento por produto ao longo dos anos'),
    
    html.P(children = 'Gráfico 11: Custeio e programas por estados'),
    
    html.P(children = 'Gráfico 12: Investimento e programas por estados'),
    
    html.P(children = 'Gráfico 13: Custeio e fontes de recursos por estados'),
    
    html.P(children = 'Gráfico 14: Investimento e fontes de recursos'),
    
    html.P(children = 'Gráfico 15: Custeio e produtos para região e ano'),
    
    html.P(children = 'Gráfico 16: Investimento e produtos para região e ano'),
    
    html.P(children = 'Gráfico 17: Custeio e produtos para UF e ano'),
    
    html.P(children = 'Gráfico 18: Investimento e produtos para UF e ano'),
    
    html.H5(children = 'Gráficos para o extrativismo:'),
    
    html.P(children = 'Gráfico 19: Para os estados e por produto'),
    
    html.P(children = 'Gráfico 20: Por produto e por programa'),
    
    html.P(children = 'Gráfico 21: Por produto e por fonte de financiamento'),
    
    html.H5(children = 'Lista de produtos:'),
    
    html.P(children = ', '.join([i.title() for i in especies])),
    
    
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 1', style = m1),
        
        html.H5(children = 'Gráfico 2', style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-1',
                     options = list(range(2013,2024)),
                     value = 2022,
                     style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-2',
                     options = list(range(2013,2024)),
                     value = 2023,
                     style = m1), 
        
        dcc.Graph(id = 'grafico-1',
                  style = m1),
        
        dcc.Graph(id = 'grafico-2',
                  style = m1)
        
        
    ]),
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 3', style = m1),
        
        html.H5(children = 'Gráfico 4', style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-3',
                     options = list(range(2013,2024)),
                     value = 2022,
                     style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-4',
                     options = list(range(2013,2024)),
                     value = 2022,
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-3',
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True,
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-4',
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True,
                     style = m1),
        
        dcc.Graph(id = 'grafico-3',
                  style = m1),
        
        dcc.Graph(id = 'grafico-4', 
                  style = m1)
        
    ]), 
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 5', style = m1),
        
        html.H5(children = 'Gráfico 6', style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-5',
                     options = list(range(2013,2024)), 
                     value = 2022,
                     style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-6',
                     options = list(range(2013,2024)),
                     value = 2023,
                     style = m1),
        
        dcc.Graph(id = 'grafico-5',
                  style = m1),
        
        dcc.Graph(id = 'grafico-6',
                  style = m1)
        
        
        
    ]),
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 7', style = m1),
        
        html.H5(children = 'Gráfico 8', style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-7',
                     options = list(range(2013,2024)), 
                     value = 2023,
                     style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-8', 
                     options = list(range(2013,2024)), 
                     value = 2023, 
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-7', 
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True,
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-8',
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True,
                     style = m1),
        
        dcc.Graph(id = 'grafico-7',
                  style = m1),
        
        dcc.Graph(id = 'grafico-8',
                  style = m1)
        
    ]),
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 9', style = m1),
        
        html.H5(children = 'Gráfico 10', style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-9',
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True, 
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-10',
                     options = [i.title() for i in especies],
                     value = 'Cacau',
                     multi = True, 
                     style = m1),
        
        dcc.Graph(id = 'grafico-9', 
                  style = m1),
        
        dcc.Graph(id = 'grafico-10', 
                  style = m1)
                      
    ]),
    
    html.Div(children = [
        
        html.H5(children = 'Gráfico 11', style = m1),
        
        html.H5(children = 'Gráfico 12', style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-11',
                     options = list(range(2013,2024)),
                     value = 2023,
                     style = m1),
        
        dcc.Dropdown(id = 'anos-grafico-12',
                     options = list(range(2013,2024)),
                     value = 2023,
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-11',
                     options = [i.title() for i in especies],
                     value = 'Cacau', 
                     style = m1),
        
        dcc.Dropdown(id = 'produtos-grafico-12',
                     options = [i.title() for i in especies],
                     value = 'Cacau', 
                     style = m1),
        
        dcc.Graph(id = 'grafico-11',
                  style = m1),
        
        dcc.Graph(id = 'grafico-12',
                  style = m1)
        
    ]),
    
    html.H5(children = 'Gráfico 13'),
    
    dcc.Dropdown(id = 'anos-grafico-13',
                     options = list(range(2013,2024)),
                     value = 2023,
                     style = m1),
    
    dcc.Dropdown(id = 'produtos-grafico-13',
                 options = [i.title() for i in especies],
                 value = 'Cacau', 
                 style = m1),
    
    dcc.Graph(id = 'grafico-13',
              ),
    
    
    html.H5(children = 'Gráfico 14'),

        
    dcc.Dropdown(id = 'anos-grafico-14',
                 options = list(range(2013,2024)),
                 value = 2023,
                 style = m1),

    dcc.Dropdown(id = 'produtos-grafico-14',
                 options = [i.title() for i in especies],
                 value = 'Cacau', 
                 style = m1),

    dcc.Graph(id = 'grafico-14',
              ),
    
    html.H5(children = 'Gráfico 15'),
    
    dcc.Dropdown(id = 'anos-grafico-15',
                 options = list(range(2013,2024)),
                 value = 2023,
                 style = m1),
    
    dcc.Dropdown(id = 'regioes-grafico-15',
                 options = [i.title() for i in custeio_sem_extrativismo['nomeRegiao'].unique()],
                 value = 'Norte',
                 style = m1),
    
    dcc.Graph(id = 'grafico-15'),
    
    html.H5(children = 'Gráfico 16'),
    
    dcc.Dropdown(id = 'anos-grafico-16',
                 options = list(range(2013,2024)),
                 value = 2023,
                 style = m1),
    
    dcc.Dropdown(id = 'regioes-grafico-16',
                 options = [i.title() for i in custeio_sem_extrativismo['nomeRegiao'].unique()],
                 value = 'Norte',
                 style = m1),
    
    dcc.Graph(id = 'grafico-16'),
    
    html.H5(children = 'Gráfico 17'),
    
    dcc.Dropdown(id = 'anos-grafico-17',
                 options = list(range(2013,2024)),
                 value = 2023,
                 style = m1),
    
    dcc.Dropdown(id = 'estados-grafico-17',
                 options = list(custeio_sem_extrativismo['nomeUF'].unique()),
                 value = 'PA',
                 style = m1),
    
    dcc.Graph(id = 'grafico-17'),
    
    html.H5(children = 'Gráfico 18'),
    
    dcc.Dropdown(id = 'anos-grafico-18',
                 options = list(range(2013,2024)),
                 value = 2023,
                 style = m1),
    
    dcc.Dropdown(id = 'estados-grafico-18',
                 options = list(custeio_sem_extrativismo['nomeUF'].unique()),
                 value = 'PA',
                 style = m1),
    
    dcc.Graph(id = 'grafico-18'),
    
    html.H5(children = 'Gráfico 19'),
    
    dcc.Dropdown(id = 'anos-grafico-19',
                 options = list(range(2013,2024)),
                 value = 2022),
    
    dcc.Graph(id = 'grafico-19'),
    
    html.H5(children = 'Gráfico 20'),
    
    dcc.Dropdown(id = 'anos-grafico-20',
                 options = list(range(2013,2024)), 
                 value = 2023),
    
    dcc.Graph(id = 'grafico-20'),
    
    html.H5(children = 'Gráfico 21'),
    
    dcc.Dropdown(id = 'anos-grafico-21',
                  options = list(range(2013,2024)),
                  value = 2023),
    
    dcc.Graph(id = 'grafico-21')




], className="dbc" )


# Gráfico 1 

@app.callback(
    Output('grafico-1','figure'),
    Input('anos-grafico-1','value')
)

def grafico_1(ano): 
    
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeRegiao','VlCusteio']].groupby('nomeRegiao', as_index = False).sum()
    
    a = a.sort_values(by = 'VlCusteio')
    
    a['nomeRegiao'] = a['nomeRegiao'].str.title()

    fig = px.bar(a, 
                 x = 'nomeRegiao', 
                 y = 'VlCusteio', 
                 title = f'Custeio sem extrativismo em {ano}',
                 labels = {'VlCusteio':'Valores em R$','nomeRegiao':''})

    return fig 

# Gráfico 2 

@app.callback(
    Output('grafico-2','figure'),
    Input('anos-grafico-2','value')
)

def grafico_2(ano): 
    
    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeRegiao','VlCusteio']].groupby('nomeRegiao', as_index = False).sum()

    a['nomeRegiao'] = a['nomeRegiao'].str.title()
    
    a = a.sort_values(by = 'VlCusteio')

    fig = px.bar(a, 
                 x = 'nomeRegiao', 
                 y = 'VlCusteio', 
                 title = f'Investimento para modalidade lavoura permanente em {ano}',
                 labels = {'VlCusteio':'Valor em R$','nomeRegiao':''})

    return fig 

# Gráfico 3 

@app.callback(
    Output('grafico-3','figure'),
    Input('anos-grafico-3','value'),
    Input('produtos-grafico-3','value')
)

def grafico_3(ano,prod):

    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a = a[['nomeRegiao','nomeProduto','VlCusteio']].groupby(['nomeRegiao','nomeProduto'], as_index = False).sum()

    a = a.pivot(index = 'nomeRegiao', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    a['nomeRegiao'] = a['nomeRegiao'].str.title() 

    fig = px.bar(a, 
                 x = 'nomeRegiao',
                 y = prod,
                 labels = {'value':'Valores em R$','nomeRegiao':''},
                 title = f'Custeio em {ano} e Regiões')
    
    return fig

# Gráfico 4 

@app.callback(
    Output('grafico-4','figure'),
    Input('anos-grafico-4','value'),
    Input('produtos-grafico-4','value')
)

def grafico_4(ano,prod): 
    

    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a = a[['nomeRegiao','nomeProduto','VlCusteio']].groupby(['nomeRegiao','nomeProduto'], as_index = False).sum()

    a = a.pivot(index = 'nomeRegiao', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    a['nomeRegiao'] = a['nomeRegiao'].str.title() 

    fig = px.bar(a, 
                 x = 'nomeRegiao',
                 y = prod,
                 labels = {'value':'Valores em R$','nomeRegiao':''},
                 title = f'Investimento em {ano} e Regiões')
    
    return fig 

# Gráfico 5

@app.callback(
    Output('grafico-5','figure'),
    Input('anos-grafico-5','value')
)

def grafico_5(ano):

    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeUF','VlCusteio']].groupby('nomeUF', as_index = False).sum() 

    a = a.sort_values(by = 'VlCusteio')

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = 'VlCusteio',
                 title = f'Contratos de custeio por estado em {ano}',
                 labels = {'VlCusteio':'Valores em R$','nomeUF':''})
    
    return fig 

# Gráfico 6 

@app.callback(
    Output('grafico-6','figure'),
    Input('anos-grafico-6','value')
)

def grafico_6(ano):

    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeUF','VlCusteio']].groupby('nomeUF', as_index = False).sum() 

    a = a.sort_values(by = 'VlCusteio')

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = 'VlCusteio',
                 title = f'Contratos de Investimento por estado em {ano}',
                 labels = {'VlCusteio':'Valores em R$','nomeUF':''})
    
    return fig 

# Gráfico 7 

@app.callback(
    Output('grafico-7','figure'),
    Input('anos-grafico-7','value'),
    Input('produtos-grafico-7','value')
)

def grafico_7(ano,prod): 
    
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeUF','nomeProduto','VlCusteio']].groupby(['nomeUF','nomeProduto'], as_index = False).sum() 

    a = a.pivot(index = 'nomeUF', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = prod,
                 title = f'Contratos de custeio por estado em {ano}',
                 labels = {'value':'Valores em R$','nomeUF':'','variable':'Produto'})
    
    return fig 

@app.callback(
    Output('grafico-8','figure'),
    Input('anos-grafico-8','value'),
    Input('produtos-grafico-8','value')
)

def grafico_8(ano,prod): 
    
    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeUF','nomeProduto','VlCusteio']].groupby(['nomeUF','nomeProduto'], as_index = False).sum() 

    a = a.pivot(index = 'nomeUF', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = prod,
                 title = f'Investimento por estado em {ano}',
                 labels = {'value':'Valores em R$','nomeUF':'','variable':'Produto'})
    
    return fig 

# Gráfico 9 

@app.callback(
    Output('grafico-9','figure'),
    Input('produtos-grafico-9','value')
)

def grafico_9(prod): 
      
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','AnoEmissao','VlCusteio']].groupby(['nomeProduto','AnoEmissao'], as_index = False).sum()

    a = a.pivot(index = 'AnoEmissao', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'AnoEmissao',
                 y = prod,
                 title = 'Contratos de custeio ao longo dos anos',
                 labels = {'value':'Valores em R$','AnoEmissao':'','variable':'Produto'})

    return fig 


# gráfico 10 

@app.callback(
    Output('grafico-10','figure'),
    Input('produtos-grafico-10','value')
)

def grafico_10(prod): 
    
    a = investimento_lavoura_permanente[investimento_lavoura_permanente['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','AnoEmissao','VlCusteio']].groupby(['nomeProduto','AnoEmissao'], as_index = False).sum()

    a = a.pivot(index = 'AnoEmissao', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'AnoEmissao',
                 y = prod,
                 title = 'Contratos de investimento ao longo dos anos',
                 labels = {'value':'Valores em R$','AnoEmissao':'','variable':'Produto'})

    return fig 

# Gráfico 11 

@app.callback(
    Output('grafico-11','figure'),
    Input('anos-grafico-11','value'),
    Input('produtos-grafico-11','value')
)

def grafico_11(ano,prod):
    
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano] 

    a = a[a['nomeProduto'] == prod] 

    a = a[['nomeUF','cdPrograma','VlCusteio']].groupby(['nomeUF','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = list(a.columns),
                 title = f'Custeio para {prod} em {ano}',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Programas'})
    
    return fig

# Gráfico 12 

@app.callback(
    Output('grafico-12','figure'),
    Input('anos-grafico-12','value'),
    Input('produtos-grafico-12','value')
)

def grafico_12(ano,prod):
    
    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano] 

    a = a[a['nomeProduto'] == prod] 

    a = a[['nomeUF','cdPrograma','VlCusteio']].groupby(['nomeUF','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = list(a.columns),
                 title = f'Investimento para {prod} em {ano} e programas',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Programas'})
    
    return fig

# Gráfico 13

@app.callback(
    Output('grafico-13','figure'),
    Input('anos-grafico-13','value'),
    Input('produtos-grafico-13','value')
)

def grafico_13(ano,prod): 
    

    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano] 

    a = a[a['nomeProduto'] == prod] 

    a = a[['nomeUF','cdFonteRecurso','VlCusteio']].groupby(['nomeUF','cdFonteRecurso'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'cdFonteRecurso', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = list(a.columns),
                 title = f'Custeio para {prod} em {ano} e fontes',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Fontes'},
                 color_discrete_sequence = px.colors.qualitative.Dark24)

    return fig

# Gráfico 14 

@app.callback(
    Output('grafico-14','figure'),
    Input('anos-grafico-14','value'),
    Input('produtos-grafico-14','value')
)

def grafico_14(ano,prod): 
    

    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano] 

    a = a[a['nomeProduto'] == prod] 

    a = a[['nomeUF','cdFonteRecurso','VlCusteio']].groupby(['nomeUF','cdFonteRecurso'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'cdFonteRecurso', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF',
                 y = list(a.columns),
                 title = f'Investimento para {prod} em {ano} e fontes',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Fontes'},
                 color_discrete_sequence = px.colors.qualitative.Dark24)

    return fig

# Gráfico 15

@app.callback(
    Output('grafico-15','figure'),
    Input('anos-grafico-15','value'),
    Input('regioes-grafico-15','value')
)


def grafico_15(ano, regiao):
        
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a['nomeRegiao'] = a['nomeRegiao'].str.title()

    a = a[a['nomeRegiao'] == regiao]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','cdPrograma','VlCusteio']].groupby(['nomeProduto','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeProduto',
                 y = list(a.columns),
                 title = f'Contratos de custeio na região {regiao} em {ano}',
                 labels = {'value':'Valor em R$','variable':'Programa','nomeProduto':''})
    
    return fig 

# Gráfico 16 

@app.callback(
    Output('grafico-16','figure'),
    Input('anos-grafico-16','value'),
    Input('regioes-grafico-16','value')
)

def grafico_16(ano,regiao): 
    

    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a['nomeRegiao'] = a['nomeRegiao'].str.title()

    a = a[a['nomeRegiao'] == regiao]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','cdPrograma','VlCusteio']].groupby(['nomeProduto','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeProduto',
                 y = list(a.columns),
                 title = f'Contratos de investimento na região {regiao} em {ano}',
                 labels = {'value':'Valor em R$','variable':'Programa','nomeProduto':''})
    
    return fig

# Gráfico 17 

@app.callback(
    Output('grafico-17','figure'),
    Input('anos-grafico-17','value'),
    Input('estados-grafico-17','value')
)

def grafico_17(ano,UF): 
        
    a = custeio_sem_extrativismo[custeio_sem_extrativismo['AnoEmissao'] == ano]

    a = a[a['nomeUF'] == UF]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','cdPrograma','VlCusteio']].groupby(['nomeProduto','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeProduto',
                 y = list(a.columns),
                 title = f'Contratos de custeio em {ano}',
                 labels = {'value':'Valor em R$','variable':'Programa','nomeProduto':''})
    
    return fig 

# Gráfico 18 

@app.callback(
    Output('grafico-18','figure'),
    Input('anos-grafico-18','value'),
    Input('estados-grafico-18','value')
)

def grafico_18(ano,UF): 
        
    a = investimento_lavoura_permanente[investimento_lavoura_permanente['AnoEmissao'] == ano]

    a = a[a['nomeUF'] == UF]

    a = a[a['nomeProduto'].isin([i.title() for i in especies])]

    a = a[['nomeProduto','cdPrograma','VlCusteio']].groupby(['nomeProduto','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeProduto',
                 y = list(a.columns),
                 title = f'Contratos de investimento em {ano}',
                 labels = {'value':'Valor em R$','variable':'Programa','nomeProduto':''})
    
    return fig 

# Gráfico 19 

@app.callback(
    Output('grafico-19','figure'),
    Input('anos-grafico-19','value')
)

def grafico_19(ano): 
       
    a = custeio_para_extrativismo[custeio_para_extrativismo['AnoEmissao'] == ano]

    a = a[['nomeProduto','nomeUF','VlCusteio']].groupby(['nomeProduto','nomeUF'], as_index = False).sum()

    a = a.pivot(index = 'nomeUF', columns = 'nomeProduto', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeUF', 
                 y = list(a.columns),
                 title = f'Extrativismo em {ano} por estado',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Produto'})
    
    return fig 

# Gráfico 20 

@app.callback(
    Output('grafico-20','figure'),
    Input('anos-grafico-20','value')
)

def grafico_20(ano): 
    
    a = custeio_para_extrativismo[custeio_para_extrativismo['AnoEmissao'] == ano]

    a = a[['nomeProduto','cdPrograma','VlCusteio']].groupby(['nomeProduto','cdPrograma'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdPrograma', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
             x = 'nomeProduto', 
             y = list(a.columns),
             title = f'Extrativismo em {ano} por programa',
             labels = {'nomeUF':'','value':'Valores em R$','variable':'Produto','nomeProduto':''})
    
    return fig 

# Gráfico 21 

@app.callback(
    Output('grafico-21','figure'),
    Input('anos-grafico-21','value')
)

def grafico_21(ano): 
    
    a = custeio_para_extrativismo[custeio_para_extrativismo['AnoEmissao'] == ano]

    a = a[['nomeProduto','cdFonteRecurso','VlCusteio']].groupby(['nomeProduto','cdFonteRecurso'], as_index = False).sum()

    a = a.pivot(index = 'nomeProduto', columns = 'cdFonteRecurso', values = 'VlCusteio').reset_index()

    fig = px.bar(a, 
                 x = 'nomeProduto', 
                 y = list(a.columns),
                 title = f'Extrativismo em {ano} por fonte de recurso',
                 labels = {'nomeUF':'','value':'Valores em R$','variable':'Produto','nomeProduto':''})
    
    return fig 




if __name__ == '__main__':
    app.run(debug=False,
           port = 8020)







