from instabot import Bot
bot = Bot()
#login Code
bot.login(username = "User_Account_ID",password = "password")
# To follow Someone
bot.follow = ("Username which you want to follow")
# To upload Photo 
bot.upload_photo("path of photo in desktop", caption = "Ur Choice")
# To unfollow Someone
bot.unfollow("Account Name")
# To Send message
bot.send_message("message",["1st Account","2nd Account"])
# Information about followers
followers = bot.get_user_followers("User_Account_ID")
for follower in followers:
    print(bot.get_user_info(follower))
# Infomation about following
following = bot.get_user_following("User_Account_ID")
for following in following:
    print(bot.get_user_info(following))