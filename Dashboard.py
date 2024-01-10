### Importando os pacotes: 


from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import plotly.offline as pyo



# Importando os dados necessários 

custeio_sem_extrativismo = pd.read_excel('https://github.com/jpeconomia/Dados-de-Cr-dito-Rural/raw/main/Custeio%20sem%20extrativismo.xlsx')

investimento_lavoura_permanente = pd.read_excel('https://github.com/jpeconomia/Dados-de-Cr-dito-Rural/raw/main/Investimento%20lavoura%20permanente.xlsx')

# geojson para os gráficos de mapa

path = "C:\\Users\\joaop\\Documents\\Dados de Conjuntura\\Dados Crédito Rural\\estados_brasil.geojson"
with open(path) as arquivo: 
    mapa = json.load(arquivo)
for feature in mapa['features']:
    feature['id'] = feature['properties']['sigla']

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
              )



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





if __name__ == '__main__':
    app.run(debug=False,
           port = 8020)





