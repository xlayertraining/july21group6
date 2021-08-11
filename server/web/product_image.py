from common import *


class ProductImageHandler(tornado.web.RequestHandler):
    async def post(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            try:
                image = self.request.files['image'][0]
                # content_type, body in binary raw, file name will be received in image. Files received at self.request.files
            except:
                code = 8943
                status = False
                message = "File not uploaded"
                raise Exception
            try:
                productId = ObjectId(
                    self.request.arguments['productId'][0].decode())
                # productId to determine which product image is being uploaded. Using this
                # entry we will update one field with filename in the entry for product in database.
            except:
                code = 8043
                status = False
                message = "Invalid Product Id"
                raise Exception

            fileType = image['content_type']
            fileType = mimetypes.guess_extension(
                fileType,
                strict=True
            )
            if fileType not in [".png", ".jpeg", ".jpg"]:
                code = 4389
                status = False
                message = "File Type not supported"
                raise Exception
            unixTime = int(time.time())
            fileName = imgPath + "/" + \
                str(unixTime) + fileType
            imageRaw = image['body']
            try:
                fh = open(fileName, 'wb')
                fh.write(imageRaw)
                fh.close()
            except:
                code = 8943
                status = False
                message = "Error in uploading file"
                raise Exception
            products.update_one(
                {
                    "_id": productId
                },
                {
                    "$push": {
                        "image": fileName
                    }
                }
            )
            code = 2000
            status = True
            message = "Product Image has been uploaded"
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

    async def get(self):
        code = 4000
        status = False
        message = ""
        result = []
        try:
            productList = products.find({})
            async for i in productList:
                i['_id'] = str(i['_id'])
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
                code = 8493
                status = False
                message = "Invalid product Id"
                raise Exception

            try:
                imageIndex = int(self.request.arguments['imageIndex'][0])
            except:
                code = 8043
                status = False
                message = "Please select the image to delete"
                raise Exception
            proFind = await products.find_one({"_id": productId})
            if proFind == None:
                code = 9043
                status = False
                message = "Product not found"
                raise Exception
            # To check if valid imageIndex is given
            if imageIndex > len(proFind['image']) - 1:
                code = 9032
                status = False
                message = "Invalid Image"
                raise Exception
            del proFind['image'][imageIndex]  # --> del proFind['image'][1]
            proUpdate = products.update_one(
                {
                    "_id": productId
                },
                {
                    '$set': {
                        "image": proFind['image']
                    }
                }
            )
            code = 2000
            status = True
            message = "Product image has been removed"
        except:
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
