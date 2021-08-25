from common import *
from auth import SecureHeader


class ProductSearchHandler(tornado.web.RequestHandler):
    async def get(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
            if account_id == None:
                code = 8765
                status = False
                message = "You're not authorized"
                raise Exception
            try:
                try:
                    keyword = self.request.arguments['keyword'][0].decode()
                except:
                    code = 8943
                    status = False
                    message = "Please enter search keyword"
                    raise Exception
                searchResult = products.find(
                    {
                        "productName": {
                            "$regex": keyword,
                            "$options": "i"
                        }
                    }
                )
                async for i in searchResult:
                    i['_id'] = str(i['_id'])
                    result.append(i)
                if len(result):
                    code = 2000
                    status = True
                    message = "Products Found"
                else:
                    code = 4004
                    status = False
                    message = "No Products Found"
            except:
                code = 9043
                status = False
                message = "Could not search"
                raise Exception
            code = 2000
            status = True
            message = "News result"
        except Exception as e:
            status = False
            # self.set_status(400)
            if not len(message):
                template = 'Exception: {0}. Argument: {1!r}'
                code = 5010
                iMessage = template.format(type(e).__name__, e.args)
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
