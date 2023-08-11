import requests

def main(event):
      code = event.get("code", "null")
      response = requests.get(url=f'https://dev.back-ng.crypto-bike.game/account/verifyMail/{code}')
      if (response.status_code == 200):
            with open('success.html', 'r') as file:
                  html_string = file.read()
                  return {"body": f'{html_string}'}
      else:
            with open('error.html', 'r') as file:
                  html_string = file.read()
                  return {"body": f'{html_string}'}
