import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Carregar o dataset
df = pd.read_csv('Life-Expectancy-Data-Averaged.csv')

# Gráfico 1: Evolução do IMC médio ao longo dos anos
fig_bmi = px.line(df,
                  x='Year',
                  y='BMI',
                  title='Evolução do IMC Médio ao Longo dos Anos',
                  labels={'BMI': 'IMC Médio', 'Year': 'Ano'})

# Gráfico 2: Relação entre magreza nas faixas etárias
fig_thinness = px.scatter(df,
                          x='Thinness_ten_nineteen_years',
                          y='Thinness_five_nine_years',
                          color='Region',
                          title='Relação entre Magreza (10-19 anos) e (5-9 anos)',
                          labels={'Thinness_ten_nineteen_years': 'Magreza (10-19 anos)',
                                  'Thinness_five_nine_years': 'Magreza (5-9 anos)'})

# Gráfico 3: Boxplot de IMC por região
fig_bmi_box = px.box(df,
                     x='Region',
                     y='BMI',
                     title='Distribuição do IMC por Região',
                     labels={'BMI': 'IMC', 'Region': 'Região'})

# Gráfico 4: Histograma de magreza
df_melted = df.melt(value_vars=['Thinness_ten_nineteen_years', 'Thinness_five_nine_years'],
                    var_name='Faixa Etária',
                    value_name='Percentual de Magreza')
fig_thinness_hist = px.histogram(df_melted,
                                 x='Percentual de Magreza',
                                 color='Faixa Etária',
                                 barmode='overlay',
                                 nbins=15,
                                 title='Distribuição do Percentual de Magreza por Faixa Etária',
                                 labels={'Percentual de Magreza': 'Magreza (%)', 'Faixa Etária': 'Faixa Etária'})

# Criar o aplicativo Dash
app = Dash(__name__)

# Layout do Dash
app.layout = html.Div([
    html.H1("Dashboard de Nutrição", style={'textAlign': 'center', 'marginBottom': '20px'}),
    html.Div([
        dcc.Graph(figure=fig_bmi, style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(figure=fig_thinness, style={'width': '48%', 'display': 'inline-block'})
    ]),
    html.Div([
        dcc.Graph(figure=fig_bmi_box, style={'width': '48%', 'display': 'inline-block'}),
        dcc.Graph(figure=fig_thinness_hist, style={'width': '48%', 'display': 'inline-block'})
    ])
])

# Executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
