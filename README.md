# CP5_Dynamic - Grafos e caminho mínimo com Dijkstra

## Integrantes

- Vitor Rampazzi Franco - RM 562270
- Daniel Brito - RM 566236
- Gustavo Borsato - RM 564621

## Executar

Requisito: Python 3.12 ou 3.13. Execução também verificada com Python 3.13 e Streamlit 1.66.0.
Abra um terminal nesta pasta e execute:

```sh
python -m venv .venv
```

Ative o ambiente no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```sh
source .venv/bin/activate
```

Instale e execute:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Acesse o endereço local exibido no terminal (normalmente http://localhost:8501).
A instalação inicial requer internet; a aplicação não utiliza APIs ou mapas externos.

## Arquivos

- app.py: controles e resultados em Streamlit.
- grafo.py: dados, lista de adjacências, Dijkstra com heapq e reconstrução.
- visualizacao.py: diagrama SVG com pesos e destaque do caminho.
- requirements.txt: dependências.

## Uso

Selecione origem e destino e clique em **Calcular menor rota**.
Pontos iguais recebem um aviso. Destinos desconectados recebem uma mensagem.
O desafio adicional permite modificar o peso ou remover uma rua temporariamente.
Após mudar o mapa, calcule novamente para atualizar o resultado.

As posições do desenho são esquemáticas: as distâncias são os pesos nas arestas,
não o comprimento visual dos traços. Ruas que se cruzam no desenho não criam
novos vértices.

## Executar no PyCharm

Abra o Terminal do PyCharm na pasta que contém `app.py`, selecione o ambiente
Python do projeto e execute:

```sh
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

O grafo é exibido no navegador. Execute pelo Streamlit; rodar `app.py` diretamente
como um arquivo Python comum gera avisos de `missing ScriptRunContext` e não inicia
a interface corretamente.

Rota de exemplo: A → D → G, com distância total de 5 km.
