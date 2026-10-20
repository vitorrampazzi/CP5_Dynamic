from grafo import LOCAIS

POSICOES = {
    'A': (80, 205), 'B': (250, 70), 'C': (530, 70),
    'D': (350, 205), 'E': (165, 350), 'F': (530, 350),
    'G': (720, 205),
}


def desenhar_grafo(grafo, caminho=None):
    caminho = caminho or []
    destaque = {frozenset((a, b)) for a, b in zip(caminho, caminho[1:])}
    trechos = []
    for a, vizinhos in grafo.items():
        for b, peso in vizinhos.items():
            if a >= b:
                continue
            x1, y1 = POSICOES[a]
            x2, y2 = POSICOES[b]
            ativo = frozenset((a, b)) in destaque
            cor, largura = ('#087f68', 7) if ativo else ('#a9b9c6', 3)
            trechos.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{cor}" stroke-width="{largura}"/>')
    
    for a, vizinhos in grafo.items():
        for b, peso in vizinhos.items():
            if a >= b:
                continue
            x1, y1 = POSICOES[a]
            x2, y2 = POSICOES[b]
            x, y = (x1+x2)/2, (y1+y2)/2
            ativo = frozenset((a, b)) in destaque
            cor = '#087f68' if ativo else '#455769'
            trechos.append(f'<rect x="{x-17}" y="{y-14}" width="34" height="28" rx="8" fill="#f4f7fa"/><text x="{x}" y="{y+5}" text-anchor="middle" fill="{cor}" font-size="17" font-weight="700">{peso:g}</text>')
    for vertice, (x, y) in POSICOES.items():
        cor = '#087f68' if vertice in caminho else '#20394d'
        trechos.append(f'<circle cx="{x}" cy="{y}" r="25" fill="{cor}"/><text x="{x}" y="{y+7}" text-anchor="middle" fill="white" font-size="21" font-weight="700">{vertice}</text>')
        if vertice in ('A', 'G'):
            trechos.append(f'<text x="{x}" y="{y+48}" text-anchor="middle" fill="#455769" font-size="15">{LOCAIS[vertice]}</text>')
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 410" role="img" aria-label="Grafo da cidade; pesos em quilômetros" style="width:100%;font-family:Arial;background:#f4f7fa;border-radius:16px">'+''.join(trechos)+'</svg>'
