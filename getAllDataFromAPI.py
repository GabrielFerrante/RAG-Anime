from processData.AnimeRequest import getAnimes,getPersonagensAnimes, getEpisodiosAnimes


def main():
    print('Adiquirindo animes...')
    getAnimes()
    print('Adiquirindo personagens')
    getPersonagensAnimes()
    print('Adquirindo listas de episódios')
    getEpisodiosAnimes()
    print('Lendo o mangá One Piece')

main()