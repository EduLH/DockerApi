import jwt
import datetime
from flask import json, Response


class Auth:

    @staticmethod
    def generate_token(email):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'sub': email
            }
            return jwt.encode(
                payload,
                'uma_chave_muito_secreta',
                'HS256'
            ).decode("utf-8")
        except Exception as e:
            return Response(
                mimetype="application/json",
                response=json.dumps({'token_generate_error': e}),
                status=400
            )

    @staticmethod
    def decode_token(token):
        re = {'data': {}, 'error': {}}
        try:
            payload = jwt.decode(token, 'uma_chave_muito_secreta')
            re['data'] = {'user_info': payload['sub']}
            return re
        except jwt.ExpiredSignatureError as e1:
            re['error'] = {'message': 'token expirado, por favor faca login'}
            return re
        except jwt.InvalidTokenError:
            re['error'] = {'message': 'Token invalido, por favor tente novamente com um novo token'}
            return re

