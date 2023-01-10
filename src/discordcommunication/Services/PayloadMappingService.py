from math import ceil
import itertools

class PayloadMappingService:
    def __init__(self, config):
        self.Config = config

    def Map(self,content):
        newsList = []
        count = content["count"]

        payload = {}
        if count <= 10:
            baseContent = f'Existem {count} notícias sobre o app {content["appid"]} na data de {content["date"]}'
            for newsitem in content["newsitems"]:
                news = {
                    "description": f'Publicado em: {newsitem["news_date"]}',
                    "url": newsitem["url"],
                    "title": newsitem["title"],
                }
                newsList.append(news)
            payload = {"content": baseContent, "username": "GamesInfo"}
            payload["embeds"] = newsList
        else:
            payload = []
            diferencial = ceil(count / 10)
            times = 10
            for index in range(diferencial):
                print(f'Index {index}')
                baseContent = f'{index+1} de {diferencial} - Existem {count} notícias sobre o app {content["appid"]} na data de {content["date"]}'
                newsList = []
                for newsIndex in itertools.repeat((10*index),times):
                    newsItems = content["newsitems"]
                    news = {
                        "description": f'Publicado em: {newsItems[newsIndex]["news_date"]}',
                        "url": newsItems[newsIndex]["url"],
                        "title": newsItems[newsIndex]["title"],
                    }
                    newsList.append(news)
                times = count - (10 * (index + 1))
                newsObject = {"content": baseContent, "username": "GamesInfo"}
                newsObject["embeds"] = newsList
                payload.append(newsObject)
        return payload
