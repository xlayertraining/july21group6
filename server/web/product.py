from common import *
from auth import SecureHeader


class ProductHandler(tornado.web.RequestHandler):
    async def post(self):
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
                    "accountId": account_id,
                    "whatsappNumber": whatsappNumber,
                    "image": None,
                    "sold": False
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

    async def put(self):
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
                jsonBody = json.loads(self.request.body.decode())
            except:
                code = 4732
                status = False
                message = "Invalid JSON Body"
                raise Exception
            try:
                productId = ObjectId(jsonBody['id'])
            except:
                code = 9043
                status = False
                message = "Invalid Id"
                raise Exception
            proFind = await products.find_one(
                {
                    "_id": productId,
                    "accountId": account_id
                }
            )
            if proFind == None:
                code = 7493
                status = False
                message = "Product not found"
                raise Exception
            try:
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

            try:
                sold = jsonBody['sold']
                if sold not in [True, False]:
                    raise Exception
            except:
                sold = False

            products.update_one(
                {
                    "_id": productId
                },
                {
                    "$set":
                    {
                        "productName": productName,
                        "price": price,
                        "description": description,
                        "details": details,
                        "accountId": account_id,
                        "whatsappNumber": whatsappNumber,
                        "sold": sold
                    }
                }
            )
            code = 5000
            status = True
            message = "Product has been successfully updated"
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
            account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
            if account_id == None:
                code = 8765
                status = False
                message = "You're not authorized"
                raise Exception
            productList = products.find({"sold": False})
            async for i in productList:
                i['_id'] = str(i['_id'])
                i['addedBy'] = ""
                accFind = users.find_one(
                    {
                        "_id": ObjectId(i['accountId'])
                    }
                )
                if accFind:
                    i['addedBy'] = accFind['firstName'] + \
                        " " + accFind['lastName']
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
            account_id = await SecureHeader.decrypt(self.request.headers["Authorization"])
            if account_id == None:
                code = 8765
                status = False
                message = "You're not authorized"
                raise Exception
            try:
                productId = ObjectId(
                    self.request.arguments['productId'][0].decode())
            except:
                code = 5489
                status = False
                message = "Invalid ID"
                raise Exception
            proFind = await products.find_one({"_id": productId, "accountId": account_id})
            if proFind == None:
                code = 4004
                status = False
                message = "Product not found"
                raise Exception
            await products.delete_one({"_id": productId, "accountId": account_id})
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
