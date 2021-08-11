from common import *


class SignInHandler(tornado.web.RequestHandler):
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
            # Fields will be firstName, lastName, phoneNumber, emailAddress and password sent from front end.
            try:
                # if in case no variable named firstName was sent, this will be None(null)
                email = jsonBody.get('email')
                if email == None:
                    raise Exception
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if(re.match(regex, email)) == None:
                    raise Exception
                email = email.lower()
            except:
                code = 9033
                status = False
                message = "Please submit valid email address"
                raise Exception

            userFind = await users.find_one({"email": email})
            if userFind == None:
                code = 9032
                status = False
                message = "Email is not registered"
                raise Exception
            try:
                password = jsonBody.get('password')
                if password == None or password == "":
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please enter valid password"
                raise Exception

            userFind = await users.find_one({
                "email": email,
                "password": password
            })

            if userFind == None:
                code = 4004
                status = False
                message = "Password is incorrect for the registered email address"
                raise Exception
            else:
                userFind = await users.find_one({
                    "email": email,
                    "password": password
                })
                userAccountId = str(userFind['_id'])
                encoded_jwt = jwt.encode(
                    {"key": userAccountId}, "icfai", algorithm="HS256")
                result.append({"Authorization": encoded_jwt})
                code = 2000
                status = True
                message = "Sign-in successful! Welcome"
        except:
            status = False
            # self.set_status(400)
            if not len(message):
                template = 'Exception: {0}. Argument: {1!r}'
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
