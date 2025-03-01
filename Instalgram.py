from instabot import Bot
bot = Bot()
print("Hey Dear User, login your account !!")
#login Code
bot.login(username = input("Enter Username : "),password = input("Enter Password : "))

task = input("Enter the task (follow, upload photo, unfollow, message, Followers list, Followint list): ").lower()

if task == "follow":
# To follow Someone    
    bot.follow(input("Enter Account ID Which you want to follow: "))

if task == "upload photo":
# To upload Photo 
    bot.upload_photo(input("Paste the path of image in .py form: "), caption=input("Enter Caption: "))

if task == "unfollow":
# To unfollow Someone
    bot.unfollow(input("Enter Account ID: "))

if task == "message":
# To Send message
    bot.send_message(input("message"), [input("1st Account", "2nd Account")])

if task == "Followers list":
# Information about followers
    followers = bot.get_user_followers("User_Account_ID")
    for follower in followers:
        print(bot.get_user_info(follower))

if task == "Following List":
# Information about following
    following = bot.get_user_following("User_Account_ID")
    for user in following:
        print(bot.get_user_info(user))

