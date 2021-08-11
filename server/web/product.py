from common import *


class ProductHandler(tornado.web.RequestHandler):
    async def post(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            try:
                jsonBody = json.loads(self.request.body.decode())
            except:
                code = 4732
                status = False
                message = "Invalid JSON Body"
                raise Exception
            # Fields will be Product Name, Price, Description, Details, Whatsapp Number
            try:
                # if in case no variable named firstName was sent, this will be None(null)
                productName = jsonBody.get('productName')
                if productName == None:
                    raise Exception
                if len(productName) < 3 or len(productName) > 50:
                    raise Exception
                productName = productName.title()
            except:
                code = 9033
                status = False
                message = "Please submit valid product name(3-20 characters)"
                raise Exception

            try:
                price = int(jsonBody['price'])
                if price <= 0:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid price"
                raise Exception

            try:
                description = jsonBody.get('description')
                if description == None:
                    raise Exception
                if len(description) < 10 or len(description) > 150:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid description(10-150 characters)"
                raise Exception

            try:
                details = jsonBody.get('details')
                if details == None:
                    raise Exception
                if len(details) < 10 or len(details) > 150:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid details(10-150 characters)"
                raise Exception

            try:
                whatsappNumber = int(jsonBody['whatsappNumber'])
                if len(str(whatsappNumber)) != 10:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid whatsapp number(10 digits)"
                raise Exception

            products.insert_one(
                {
                    "productName": productName,
                    "price": price,
                    "description": description,
                    "details": details,
                    "whatsappNumber": whatsappNumber,
                    "image": None
                }
            )
            code = 5000
            status = True
            message = "Product has been successfully Added"
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

    async def get(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            productList = products.find({})
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

    async def delete(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            try:
                productId = ObjectId(
                    self.request.arguments['productId'][0].decode())
            except:
                code = 5489
                status = False
                message = "Invalid ID"
                raise Exception
            products.delete_one({"_id": productId})
            code = 200
            status = True
            message = "Product has been deleted"
        except Exception as e:
            status = False
            # self.set_status(400)
            if not len(message):
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
