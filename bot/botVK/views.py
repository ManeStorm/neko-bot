from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3
import database

session = vk.Session(access_token="")
vkAPI = vk.API(session)

@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    print(body)

    if body == { "type": "confirmation", "group_id": 194135900 }:
        return HttpResponse("cce81b0c")

    if body["type"] == "message_new":

        msg = body["object"]["message"]["text"]
        payload = body["object"]["message"]["payload"]
        userID = body["object"]["message"]["from_id"]
        userInfo = vkAPI.users.get(user_ids = userID, v=5.103)[0]
        answ = ""
        attach = ""

        if payload == """{"command":"start"}""":
            keyboardStart(request, userID)

        # if msg[:5] == "teach":
        #     pos = msg.find("?")
        #     newMsg = msg[6:pos].replace(" ", "")
        #     newAnsw = msg[pos+1:]
        #     database.insert("answer", ["msg","answ"], [newMsg, newAnsw])
        #     answ = "Я запомнила вашу команду '{0}', хозяин".format(newMsg)

        # for i in database.get("answer"):
        #     if msg == i["msg"]:
        #         answ = i["answ"]
        #         break
        #     else:
        #         answ = "Простите, но я не знаю такой команды, хозяин, используйте 'commands' |или же научите меня, используя команду 'teach', вот пример: команда ? ответ|, ня (teach НЕ РАБОТАЕТ)"

        sendAnswer(userID, answ, attach)

    return HttpResponse("ok")

def sendAnswer(userID, answ = "", attach = "", keyboard = ""):
	vkAPI.messages.send(user_id = userID, message = answ, attachment=attach, keyboard = keyboard, random_id = random.randint(1, 99999999999999999), v=5.103)

def keyboardStart(request, userID):
    answ = "Здравствуйте, хозяин! Кто Вы для моего создателя?"
    keyboard = json.dumps({
        "one_time": True,

        "buttons":[[
            {
                "action": {
                    "type":"text",
                    "label":"Создатель",
                    "payload": """{"command":creator"}"""
                },
                "color":"negative"
            }
        ]]
    })

    sendAnswer(userID, answ, keyboard = keyboard)