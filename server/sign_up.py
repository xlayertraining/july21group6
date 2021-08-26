from collections import namedtuple
from tornado.httputil import ResponseStartLine
from common import *


class SignUpHandler(tornado.web.RequestHandler):

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
                firstName = jsonBody.get('firstName')
                if firstName == None:
                    raise Exception
                if len(firstName) < 3 or len(firstName) > 20:
                    raise Exception
                firstName = firstName.title()
            except:
                code = 9033
                status = False
                message = "Please submit valid first name(3-20 characters)"
                raise Exception
            try:
                lastName = jsonBody.get('lastName')
                if lastName == None:
                    raise Exception
                if len(lastName) < 3 or len(lastName) > 20:
                    raise Exception
                lastName = lastName.title()
            except:
                code = 9033
                status = False
                message = "Please submit valid first name(3-20 characters)"
                raise Exception
            try:                
                phoneNumber = int(jsonBody['phoneNumber'])
                if len(str(phoneNumber)) != 10:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please submit valid phone number(10 digits)"
                raise Exception

            userFind = await users.find_one({
                "phoneNumber": phoneNumber
            })

            if userFind is not None:
                code = 8043
                status = False
                message = "Phone number is already registered"
                raise Exception

            email = jsonBody.get('emailAddress')
            if email == None or email == "":
                code = 9022
                status = False
                message = "Please enter valid email address"
                raise Exception
            '''
            else:
                # checking if email address if of valid format
                # Regular expression concept to check format of string in email
                #something    @ something    . something
                #regex = r'\b[a-A-Zz0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                #email = email.lower()
                #if(re.match(regex, email)) == None:
                #    code = 9032
                #    status = False
                #    message = "Invalid Email Format"
                #    raise Exception
            '''
            try:
                password = jsonBody.get('password')
                if len(password) > 15:
                    raise Exception
            except:
                code = 9033
                status = False
                message = "Please enter valid password (6-15 characters)"
                raise Exception

            rs = await users.insert_one(
                {
                    "firstName": firstName,
                    "lastName": lastName,
                    "phoneNumber": phoneNumber,
                    "email": email,
                    "password": password
                }
            )
            encoded_jwt = jwt.encode(
                {
                    "key": str(rs.inserted_id)
                },
                "icfai", algorithm="HS256"
            )

            if type(encoded_jwt) is bytes:                
                encoded_jwt = encoded_jwt.decode()            
            result.append({"Authorization": encoded_jwt})
            code = 2000
            status = True
            message = "Sign-up successful."

        except Exception as e:
            status = False
            # code = 5011
            # message = 'Internal Error, Please Contact the Support Team.'
            template = 'Exception: {0}. Argument: {1!r}'
            iMessage = template.format(type(e).__name__, e.args)
            # if not len(message):
            #     message = 'Internal Error, Please Contact the Support Team.'
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = exc_tb.tb_frame.f_code.co_filename
            print('EXC', iMessage)
            print('EX2', 'FILE: ' + str(fname) + ' LINE: ' + str(exc_tb.tb_lineno) + ' TYPE: ' + str(exc_type))

        response = {
            'code': code,
            'status': status,
            'message': message,
            'result': result
        }
        self.write(response)
        self.finish()
        return
