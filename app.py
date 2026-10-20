from math import isinf
import streamlit as st
import streamlit.components.v1 as components
from grafo import LOCAIS, RUAS, criar_grafo, dijkstra
from visualizacao import desenhar_grafo

st.set_page_config(page_title='Rotas da cidade | CP5', page_icon='📍', layout='centered')
st.caption('CP5 • DYNAMIC PROGRAMMING • GRAFOS PONDERADOS')
st.title('A menor rota pela cidade')
st.write('Escolha dois pontos e encontre a menor distância com o algoritmo de Dijkstra.')

with st.expander('Desafio adicional: alterar ou desativar uma rua'):
    usar_edicao = st.checkbox('Aplicar alteração ao mapa', value=False)
    indice = st.selectbox('Rua', range(len(RUAS)), format_func=lambda i: f'{RUAS[i][0]} ↔ {RUAS[i][1]} ({RUAS[i][2]} km)')
    novo_peso = st.number_input('Nova distância (km)', min_value=0.0, value=float(RUAS[indice][2]), step=0.5)
    desativar = st.checkbox('Desativar temporariamente a rua')

ruas = list(RUAS)
if usar_edicao:
    a, b, _ = ruas[indice]
    if desativar:
        ruas.pop(indice)
    else:
        ruas[indice] = (a, b, novo_peso)
grafo = criar_grafo(ruas)
rotulo = lambda codigo: f'{codigo} — {LOCAIS[codigo]}'
with st.form('rota'):
    esquerda, direita = st.columns(2)
    origem = esquerda.selectbox('Origem', list(LOCAIS), format_func=rotulo)
    destino = direita.selectbox('Destino', list(LOCAIS), index=6, format_func=rotulo)
    calcular = st.form_submit_button('Calcular menor rota', type='primary', use_container_width=True)

assinatura = (origem, destino, tuple(ruas))
if calcular:
    if origem == destino:
        st.session_state.pop('resultado', None)
        st.warning('Escolha pontos diferentes para calcular uma rota.')
    else:
        distancia, caminho = dijkstra(grafo, origem, destino)
        st.session_state['resultado'] = (assinatura, distancia, caminho)

resultado = st.session_state.get('resultado')
caminho = []
if resultado and resultado[0] == assinatura:
    _, distancia, caminho = resultado
    if isinf(distancia):
        st.error('Não existe caminho entre os pontos selecionados.')
    else:
        c1, c2 = st.columns([1, 2])
        c1.metric('Distância total', f'{distancia:g} km')
        c2.metric('Caminho encontrado', ' → '.join(caminho))
elif resultado:
    st.info('O mapa ou os pontos mudaram. Calcule novamente para atualizar a rota.')

components.html(desenhar_grafo(grafo, caminho), height=390)
st.caption('Traço verde: caminho mínimo • Traço cinza: demais ruas • Distâncias em km')
if usar_edicao and resultado and resultado[0] == assinatura and caminho:
    original, _ = dijkstra(criar_grafo(), origem, destino)
    st.write(f'No mapa original, a menor distância era {original:g} km. Após a alteração, é {distancia:g} km. Dijkstra reavalia os custos disponíveis; uma rua mais longa ou removida pode mudar a melhor rota.')
with st.expander('Como o algoritmo encontra a rota?'):
    st.write('A origem começa com distância zero e os demais pontos com infinito. Uma fila de prioridade escolhe o menor custo conhecido. A cada rua, o algoritmo verifica se existe uma distância melhor e guarda o predecessor. No final, os predecessores reconstroem o caminho.')
    st.dataframe([{'Origem': a, 'Destino': b, 'Distância (km)': p} for a, b, p in ruas], hide_index=True, use_container_width=True)
st.divider()
st.caption('Vitor Rampazzi Franco • RM 562270 | Daniel Brito • RM 566236 | Gustavo Borsato • RM 564621')
