from common import *


class SecureHeader(tornado.web.RequestHandler):
    async def decrypt(handler):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            Authorization = handler.request.headers['Authorization'].split()
            firstPart = Authorization[0]
            secondPart = Authorization[1]
            if firstPart != "Bearer":
                raise Exception
            userAccountId = jwt.decode(
                secondPart, "icfai", algorithms=["HS256"])
            accFind = await users.find_one(
                {
                    "_id": ObjectId(userAccountId['key'])
                }
            )
            if accFind == None:
                raise Exception
            else:
                print("Got")
        except:
            code = 7483
            status = False
            message = "Invalid Authorization"
            raise Exception
        response = {
            'code': code,
            'status': status,
            'message': message,
            'result': result
        }
        handler.write(response)
        handler.finish()
