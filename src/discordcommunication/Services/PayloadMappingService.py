from math import ceil

class PayloadMappingService:
    def __init__(self, config):
        self.Config = config

    def Map(self,content):
        count = content["count"]
        payload = []
        diferencial = ceil(count / 10)
        for index in range(diferencial):
            print(f'entrou {index}')
            baseContent = f'{index+1} de {diferencial} - Existem {count} notícias sobre o app {content["appid"]} na data de {content["date"]}'
            indexBase = (10*index)
            if(indexBase == 0):
                times = 10
            else:
                times = count - indexBase
            newsList = []
            for indexInterno in range(0,times):
                newsItem = content["newsitems"][indexBase+indexInterno]
                news = {
                    "description": f'Publicado em: {newsItem["news_date"]}',
                    "url": newsItem["url"],
                    "title": newsItem["title"],
                    }
                newsList.append(news)
            newsObject = {"content": baseContent, "username": "GamesInfo"}
            newsObject["embeds"] = newsList
            print(f'tamanho da lista {len(newsList)}')
            payload.append(newsObject)
        return payload
