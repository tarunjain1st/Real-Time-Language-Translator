import requests
import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url=' '                         # the url from ibm watson text to speech api services
key=' '                         # the key from ibm watson text to speech api services
authenticator = IAMAuthenticator(key)
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url(url)
def lang_list():
    dic={
        'key':' ',              # get key from yandex translation api
        'ui':'en'
        }
    url='https://translate.yandex.net/api/v1.5/tr.json/getLangs'
    a=requests.get(url=url, params=dic)
    t=json.loads(a.text)
    print(type(t))
    print(t)
    t['langs']
    t=json.dumps(t, indent=2)


def detect(text):
    dic={
        'key':' ',               # get key from yandex translation api
        'text':''
        }
    dic['text']=text
    url='https://translate.yandex.net/api/v1.5/tr.json/detect'
    a=requests.get(url=url, params=dic)
    t=a.json()
    print(t['lang'])


def translate(text, convert):
    dic={
        'key':' ',               # get key from yandex translation api
        'ui':'en',
        'text':'',
        'lang':''
        }
    dic['text']=text
    dic['lang']=convert

    url='https://translate.yandex.net/api/v1.5/tr.json/translate'
    a=requests.get(url=url, params=dic)
    txt=a.json()
    print(a.text)
    t=json.dumps(txt['text'])
    print(t)
    return(txt['text'][0])


translate('hello everyone, this is a translation system meant for education purpose','en-hi')
