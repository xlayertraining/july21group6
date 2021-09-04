from common import *
from auth import SecureHeader


class MyProductHandler(tornado.web.RequestHandler):

    def options(self):
        self.write({})

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
            productList = products.find({"accountId": account_id})
            async for i in productList:
                i['_id'] = str(i['_id'])
                if i['image'] != None:
                    i['image'] = uploadUrl + i['image']
                result.append(i)
            if len(result):
                code = 200
                status = True
                message = "List of products"
            else:
                code = 404
                status = False
                message = "No products found"
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
