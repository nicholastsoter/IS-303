from FortniteBot import FortniteBot

bot1 = FortniteBot("George")
bot2 = FortniteBot("R2-D2")
bot3 = FortniteBot("Chat")

bot1.take_damage(5)
bot2.take_damage(20)

print(bot1.bot_name)
print(bot2.bot_name)
print(bot3.bot_name)
