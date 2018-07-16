#coding=UTF-8

from tuling import MyTulingRobot

if __name__ == "__main__":
    tetu = MyTulingRobot()

    # cntlm proxy set
    tetu.set_proxy("http", "127.0.0.1:3128")

    response = tetu.talk("who are you？")
    print(response)
