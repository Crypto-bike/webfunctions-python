import requests

def main(event):
      code = event.get("code")
      backend_url = 'https://dev.back-ng.crypto-bike.game/account/verifyMail/' + code + '/'
      response = requests(backend_url)
      if (response.status_code == 200):
            with open('success.html', 'r') as f:
                  html_string = f.read()
                  return {"body": html_string}
      else:
            with open('error.html', 'r') as f:
                  html_string = f.read()
                  return {"body": html_string}

      
