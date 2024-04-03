def corrigir_arquivo(dados_errados, dados_corrigidos, substituicoes):
    with open(dados_errados, 'r') as f:
        texto = f.read()

    for termo, substituto in substituicoes.items():
        texto = texto.replace(termo, substituto)

    with open(dados_corrigidos, 'w') as f:
        f.write(texto)

# Defina as substituições desejadas como um dicionário
substituicoes = {
    '[top_artists]': 'TOP_ARTISTS',
    '[Artist]': 'ARTIST',
    '[Track Name]': 'TRACK_NAME',
    '[Popularity]': 'POPULARITY',
    '[Duration (ms)]': 'DURATION_MS',
    '[Track ID]': 'TRACK_ID',
    # Adicione mais substituições conforme necessário
}

# Nome dos arquivos de entrada e saída
dados_errados = 'C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Visualização de Dados e Introdução a SQL/TPs/AT/scriptDeCorrecao/dados_errados.txt'
dados_corrigidos = 'C:/Users/gribe/OneDrive/Documentos/Codes/INFNET/2024.1/Visualização de Dados e Introdução a SQL/TPs/AT/scriptDeCorrecao/dados_corrigidos.txt'

# Chama a função para corrigir o arquivo
corrigir_arquivo(dados_errados, dados_corrigidos, substituicoes)

print("Arquivo corrigido criado com sucesso!")
