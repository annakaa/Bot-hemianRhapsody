# -*- coding: utf-8 -*-

import telebot
from findAudioLine import findAudioLine

token = '213638946:AAHFEQ7F4aP2K769j4UjP6d7TbGV1bnwrog'
cid = None

blockedUsers = []
knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
              'help': 'Gives you information about the available commands',
              'rihanna_on': 'Turns on Rihanna', 'rihanna_off': 'Turns off Rihanna',
}
RIHANNA={}

def findLine(message, cid):
  messageParts = message.strip().split()
  inwords = ' '.join(messageParts).upper()
  print inwords, cid
  rihanna = False
  if RIHANNA.has_key(cid):
    rihanna = RIHANNA[cid]
  [fullLine,audio] = findAudioLine(inwords, rihanna)
  if fullLine:
    print fullLine,audio
    bot.send_message(cid, fullLine)
    audiohandle = open(audio, 'rb')
    bot.send_audio(cid, audiohandle)
    
  else:
    print "not found"
    bot.send_message(cid, "Those words aren't in the song :-(")


def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text' and m.text not in ["/start","/help","/rihanna_on","/rihanna_off"] :
          findLine(m.text, m.chat.id)
                
                
bot = telebot.TeleBot(token)
bot.set_update_listener(listener)  # register listener 

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    RIHANNA[cid] = False
    welcomeMsg = "Welcome to Queen of Music. Please send me one or more words from Bohemian Rhapsody. To switch to Rihanna's Work, send me /rihanna_on . To switch back, send me /rihanna_off . Enjoy! "
    bot.send_message(cid, welcomeMsg)

# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

@bot.message_handler(commands=['rihanna_on'])
def command_rihanna_on(m):
  cid = m.chat.id
  RIHANNA[cid]=True

@bot.message_handler(commands=['rihanna_off'])
def command_rihanna_off(m):
  cid = m.chat.id
  RIHANNA[cid]=False

if __name__=="__main__":
  print "loaded"
  bot.polling()