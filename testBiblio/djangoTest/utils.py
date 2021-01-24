from django.contrib.auth import authenticate
import json
import jwt
import requests

#Permet de créer un user Django et de retourner son username
def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username

#Fonction permettant de vérifier et décoder le Token permettant l'authentification Auth0 account
def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'.format('django-vuejs.natachouille.com')).json()
    public_key = None
    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format('django-vuejs.natachouille.com')
    return jwt.decode(token, public_key, audience='https://django-vuejs.natachouille.com', issuer=issuer, algorithms=['RS256'])