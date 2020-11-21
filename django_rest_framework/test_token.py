import requests #pip install requests

# TOKEN ='02968b1075d75cc4562219c9ac0f778e499018b5'
JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2Vybm"
 "FtZSI6InVzZXIyIiwiZXhwIjoxNjA1OTY2MzU0LCJlbWFpbCI6IiJ9.JCbDKVh9BA"
  "H2PoWwaERx9sUMqIjGSy1TNt-QUeDrj_4"

)

headers = {

    # 'Authorization': f'Token {TOKEN}', #Token 인증
    
    'Authorization': f'JWT {JWT_TOKEN}',  #JWT 인증
}
res = requests.get('http://localhost:8000/post/1/',headers=headers)

print(res.json())

