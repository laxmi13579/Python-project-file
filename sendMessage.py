import fbchat 
from getpass import getpass 
# username = "laxmi.yadav.370515@facebook.com"
# password = "predestination@2"
# username = "kushwahasubhadra@gmail.com"
# password = "luvislife"
client = fbchat.Client("laxmi.yadav.370515@facebook.com", "predestination@2") 
no_of_friends = int(input("Number of friends: ")) 
for i in range(no_of_friends): 
    # name = str(input("Name: ")) 
    name = "jenny sinha"
    friends = client.searchForUsers(name)  # return a list of names 
    friend = friends[0] 
    # msg = str(input("Message: ")) 
    msg = "miss you"
    sent = client.sendMessage(msg, thread_id=friend.uid) 
    if sent: 
        print("Message sent successfully!") 
