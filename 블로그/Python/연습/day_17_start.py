class User:
    
    def __init__(self, user_id, username):
        # initialise attributes / create starting value for attribute
        # called everytime class is called
        
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Alex")
# 밑의 코드와 같다
# user_1.id = "001"
# user_1.username = "Alex"
user_2 = User("002", "Yang")

user_1.follow(user_2)

print(user_1.following)
print(user_2.following)
print(user_1.followers)
print(user_2.followers)