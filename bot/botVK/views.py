from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
import json
import vk
import random
import sqlite3
import database

session = vk.Session(access_token="5dba33399e121aa9b74f8e574ee0cd310f6a87451dcdc4581e7822c1fe18fe6c9a3f97d8f2f83bca4ecff")
vkAPI = vk.API(session)

@csrf_exempt
def bot(request):
    body = json.loads(request.body)
    print(body)

    if body == { "type": "confirmation", "group_id": 194135900 }:
        return HttpResponse("d6f88a56")

    if body["type"] == "message_new":

        msg = body["object"]["message"]["text"]
        userID = body["object"]["message"]["from_id"]
        answ = ""
        attach = ""

        if msg[:5] == "teach":
            pos = msg.find("?")
            newMsg = msg[6:pos].replace(" ", "")
            newAnsw = msg[pos+1:]
            database.insert("answer", ["msg","answ"], [newMsg, newAnsw])
            answ = "Я запомнила вашу команду '{0}', хозяин".format(newMsg)

        for i in database.get("answer"):
            if msg == i["msg"]:
                answ = i["answ"]
                break
            else:
                answ = "Простите, но я не знаю такой команды, хозяин, используйте 'commands' или же научите меня, используя команду 'teach' (команда ? ответ), ня"

            
        # if body["object"]["message"]["text"] == "Привет":
        #     msg = "Добро пожаловать! Чего желаете, хозяин?"
        #     vkAPI.messages.send(user_id = userID, message = msg, random_id = random.randint(1, 99999999999999999), v=5.103)

        # elif body["object"]["message"]["text"] == "Админ":
        #     msg = "Гл. Администратор - https://vk.com/manestorm"
        #     vkAPI.messages.send(user_id = userID, message = msg, random_id = random.randint(1, 99999999999999999), v=5.103)

        # elif body["object"]["message"]["text"] == "Как дела?":
        #     msg = "Всё за~мур~чательно!"
        #     vkAPI.messages.send(user_id = userID, message = msg, random_id = random.randint(1, 99999999999999999), v=5.103)

        # elif body["object"]["message"]["text"] == "commands":
        #     msg = "Вот мои команды: Привет, Админ, Как дела?, commands"
        #     vkAPI.messages.send(user_id = userID, message = msg, random_id = random.randint(1, 99999999999999999), v=5.103)

        sendAnswer(userID, answ, attach)

    return HttpResponse("ok")

def sendAnswer(userID, answ = "", attach = ""):
	vkAPI.messages.send(user_id = userID, message = answ, attachment=attach, random_id = random.randint(1, 99999999999999999), v=5.103)