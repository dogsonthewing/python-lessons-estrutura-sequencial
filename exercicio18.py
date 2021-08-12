velocidade_conexao = int(input('Digite a velocidade da sua conexão em Mb/s '))
tamanho_arquivo = int(input('Digite o tamanho do arquivo em MB '))
print('-------------------------------------------')

tempo_de_download = tamanho_arquivo / (velocidade_conexao / 8)
tempo_de_download = tempo_de_download / 60

print('Seu download vai demorar' , tempo_de_download , 'minutos para baixar completamente')