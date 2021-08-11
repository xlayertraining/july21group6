from common import *


class SearchNewsHandler(tornado.web.RequestHandler):
    async def get(self):
        code = 4000
        status = False
        message = ""
        result = []
        if True:
            try:
                try:
                    search = self.request.arguments['search'][0].decode()
                except:
                    code = 8943
                    status = False
                    message = "Please enter search keyword"
                    raise Exception
                newsapiUrl = "https://newsapi.org/v2/everything?q=" + search + \
                    "&sortBy=publishedAt&apiKey=7f6c2f7fdf2d4d82b5d5c87fe36b985e"
                # To call 3rd party api within python using requests library
                newsResponse = requests.get(url=newsapiUrl)
                newsJson = json.loads(newsResponse.text)
                for i in newsJson['articles']:
                    v = {
                        "author": i['author'],
                        "title": i['title'],
                        "description": i['description'],
                        "url": i['url'],
                        "publishedAt": i['publishedAt'],
                        "content": i['content'],
                        "urlToImage": i['urlToImage']
                    }
                    result.append(v)
            except:
                code = 9043
                status = False
                message = "Could not search"
                raise Exception
            search_history.insert_one({
                "accountId": self.accountId,
                "keyword": search,
                "result": result
            }
            )
            code = 2000
            status = True
            message = "News result"
        else:
            status = False
            # self.set_status(400)
            if not len(message):
                code = 5010
                message = 'Internal Error, Please Contact the Support Team.'
        response = {
            'code': code,
            'status': status,
            'message': message
        }
        try:
            response['result'] = result
            self.write(response)
            self.finish()
            return
        except Exception as e:
            status = False
            code = 5011
            message = 'Internal Error, Please Contact the Support Team.'
            response = {
                'code': code,
                'status': status,
                'message': message
            }
            self.write(response)
            self.finish()
            return
