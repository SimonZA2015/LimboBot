import json
import re
import urllib

from assets import tokens


class tools():
    def getInfo(bot, idTelegram, type):
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
                for i in range(len(data[3][type])):
                    bot.send_photo(idTelegram, data[3][type][i][0], data[3][type][i][1])
        except Exception as e:
            print('BOT> Error in tools.py{getInfo}: ', e)

    def addInfo(type,image, text):
        with open('data.json') as data_file:
            data = json.load(data_file)
            data[3][type].append([image, text])
            data_file.close()
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)


    def sendAll(bot, text):
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
                listUser = data[0]
                errorSend = 0
                agreeSend = 0
                for i in range(len(listUser)):
                    try:
                        if not(listUser[i] == tokens.userAdminChat):
                            bot.send_message(listUser[i], text)
                            agreeSend += 1
                    except:
                        errorSend += 1
                bot.send_message(tokens.userAdminChat, 'Отправил удачно:' + str(agreeSend) + "\nНе удачно:" + str(errorSend))
        except Exception as e:
            print('BOT> Error in tools.py{sendAll}: ', e)


    def sendPhotoAll(bot, image, text):
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
                listUser = data[0]
                errorSend = 0
                agreeSend = 0
                for i in range(len(listUser)):
                    try:
                        if not(listUser[i] == tokens.userAdminChat):
                            bot.send_photo(listUser[i], image, text)
                            agreeSend += 1
                    except:
                        errorSend += 1
                bot.send_message(tokens.userAdminChat, 'Отправил удачно:' + str(agreeSend) + "\nНе удачно:" + str(errorSend))
        except Exception as e:
            print('BOT> Error in tools.py{sendAll}: ', e)



    def getIdTokens(token):
        with open('data.json') as data_file:
            data = json.load(data_file)
            index = data[2].index(token)
            data_file.close()
            return index

    def getPosUser(user):
        with open('data.json') as data_file:
            data = json.load(data_file)
            index = data[0].index(user)
            data_file.close()
            return index

    def saveId(idTelegram, username):
        # Добавление акк в массив
        try:
            print(idTelegram, '> /start')
            with open('data.json') as data_file:
                data = json.load(data_file)
                ids = data[0]
                try:
                    i = ids.index(idTelegram)
                    print('BOT> tools.js: index user=', i)
                except:
                    data[0].append(idTelegram)
                    print('BOT> tools.js:'+ str(idTelegram) + '(' + username + ') Added to ids')
                    d = []
                    for i in range(len(data[2])):
                        d.append([])

                    data[1].append(d)
                    with open('data.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                # Если акк не в массиве то добавляем его


        except Exception as e:
            print('BOT> Error in tools.py{saveId}: ', e)

    def setValue(idTelegram, key, value):
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
                try:
                    data[1][tools.getPosUser(idTelegram)][tools.getIdTokens(key)] = value
                except:
                    #Если нету значения в данном масиве, то добавляем
                    data[1][tools.getPosUser(idTelegram)][tools.getIdTokens(key)].append(value)
                data_file.close()
                with open('data.json', 'w') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    f.close()
                    return True
        except Exception as e:
            print('BOT> error in tool.py{setValue}: ', e)
            return False

    def loginBase(command, username, password):
        try:
            import pymysql
            dbNAme = tokens.dbBase
            userDb = username.split('@', 1)[0]
            con = pymysql.connect(
                host="denishik.ru",
                user=dbNAme.split('_', 1)[0] + '_' + userDb,
                password=password,
                db=dbNAme
            )
            select_users = command
            cursor = con.cursor()
            cursor.execute(select_users)
            return cursor.fetchall()
        except Exception as e:
            print('BOT> error in tool.py{loginBase}: ', e)

    def updateIpBase(username, password, ip, id):
        import pymysql
        dbNAme = tokens.dbBase
        userDb = username.split('@', 1)[0]
        con = pymysql.connect(
            host="denishik.ru",
            user=dbNAme.split('_', 1)[0] + '_' + userDb,
            password=password,
            db=dbNAme,
            autocommit =True
        )
        select_users = "UPDATE `users` SET `ips` = ('%s') WHERE `users`.`id` = ('%s')"
        print(select_users)
        cursor = con.cursor()
        cursor.execute(select_users % (ip + ',', id))
        return cursor.fetchall()

    def get_ip(self):
        import socket
        h_name = socket.gethostname()
        IP_addres = socket.gethostbyname(h_name)
        print("Host Name is:" + h_name)
        print("Computer IP Address is:" + IP_addres)
        return IP_addres

    def clear_ips(username, password, id):
        import pymysql
        dbNAme = tokens.dbBase
        userDb = username.split('@', 1)[0]
        con = pymysql.connect(
            host="denishik.ru",
            user=dbNAme.split('_', 1)[0] + '_' + userDb,
            password=password,
            db=dbNAme,
            autocommit=True
        )
        select_users = "UPDATE `users` SET `ips` = (' ') WHERE `users`.`id` = ('%s')"
        print(select_users)
        cursor = con.cursor()
        cursor.execute(select_users % (id))
        return cursor.fetchall()

    def getValue(idTelegram, key):
        try:
            with open('data.json') as data_file:
                data = json.load(data_file)
                result = data[1][tools.getPosUser(idTelegram)][tools.getIdTokens(key)]
                return result
        except Exception as e:
            print('BOT> error in tool.py{getValue}: ', e)
            return False
