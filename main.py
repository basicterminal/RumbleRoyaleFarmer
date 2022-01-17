import discord, time, os
from discord.ext import commands

#----------#
# Rumble Royale Farmer
## Not as accurate as it is supposed to be because the api does not allow users to read message content with a selfbot.
## Therefore the bot is not that well at reacting to messages.
#----------#

reacted = []

bot = commands.Bot(
      self_bot = True,
      command_prefix = "rumble "
)

_reacted = 0
_failed  = 0

#-----------#

@bot.event
async def on_reaction_add(reaction, user):
      global _reacted
      global _failed 
     
      global reacted
      if reaction.message.author.bot == True:
         if reaction.message.id not in reacted:
            if reaction.emoji.name == "Swrds":
               try:
                  await reaction.message.add_reaction(reaction.emoji)
                  reacted += [reaction.message.id]
                  print (" [@] | {} | Joined Rumble Royale Event".format(reaction.message.channel.name))
               except Exception as E:
                  print (E)
            else:
                  print (" [@] | {} | Passed".format(reaction.emoji.name))
         else:
            print (" [@] | {} | Could not react to the last message".format(reaction.emoji.name))
      else:
            print (" [@] | Passed")
      
#----------------------#
bot.run("", bot = False)
             
