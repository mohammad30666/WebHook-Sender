
banner = """

               ___________________________________ 
              | created by:                       |
              |       mohammad30666               |
              |                                   |
              |                                   |
              |   my github:                      |
              | https://github.com/mohammad30666  |
              |___________________________________|
"""





import requests
import time 
print(banner)
print("my discord id mohammad30666#0719")
time.sleep (2)
target = input ('Enter WebHook>>> ')
gh = input ('Enter WebHook Name>>> ')
Avatar = input ('WebHook Avatar url>>> ')
Message = input ('Message>>> ')

url =target


time.sleep (0.2)
pyload =  {"content": Message , "username": gh , "avatar_url": Avatar }
w = requests.post(url, data=pyload)
print('Message sendd ' + Message)


time.sleep (2)
while True:
    Message = input ('Message>>> ')

    url =target


    time.sleep (0.2)
    pyload =  {"content": Message , "username": gh , "avatar_url": Avatar }
    w = requests.post(url, data=pyload)
    print('Message sendd ' + Message)
