from math import ceil
import itertools

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
            #partList = content[:times]
            #for newsIndex in itertools.repeat((10*index),times):
            indexBase = (10*index)
            if(indexBase == 0):
                times = 10
            else:
                times = count - indexBase
            newsList = []
            for indexInterno in range(0,times):
                print(index)
                print(indexInterno)
                print(indexInterno+indexBase)
                newsItem = content["newsitems"][indexBase+indexInterno]
                print("xxxxxx")
                #print(newsItem["news_date"])
                #newsItems = content["newsitems"]
                news = {
                    #"description": f'Publicado em: {newsItems[newsIndex]["news_date"]}',
                    "description": f'Publicado em: {newsItem["news_date"]}',
                    #"url": newsItems[newsIndex]["url"],
                    "url": newsItem["url"],
                    #"title": newsItems[newsIndex]["title"],
                    "title": newsItem["title"],
                    }
                newsList.append(news)
            newsObject = {"content": baseContent, "username": "GamesInfo"}
            newsObject["embeds"] = newsList
            print(f'tamanho da lista {len(newsList)}')
            payload.append(newsObject)
        return payload
