from common import *
from auth import SecureHeader


class SingleProductHandler(tornado.web.RequestHandler):
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
                productId = ObjectId(self.request.arguments['id'][0].decode())
            except:
                code = 9403
                status = False
                message = "Invalid Id"
                raise Exception
            proFind = products.find_one({"_id": productId})
            if proFind:
                proFind['_id'] = str(proFind['_id'])
                proFind['addedBy'] = ""
                accFind = users.find_one(
                    {
                        "_id": ObjectId(proFind['accountId'])
                    }
                )
                if accFind:
                    proFind['addedBy'] = accFind['firstName'] + \
                        " " + accFind['lastName']
                if proFind['image'] != None:
                    proFind['image'] = uploadUrl + proFind['image']
                result.append(proFind)
            if len(result):
                code = 200
                status = True
                message = "Product Info"
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
