import random
responses={"hello":["Hi"],"how are you":["fine"]}
def get_response(user_input):
    if user_input.lower()in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "IM sorry"
def main():
    print("wlecome")
    while True:
        user_input=input("ypu")
        if user_input.lower()=='bye':
            print(get_response(user_input))
            break
        else:
            print("Chat:",get_response(user_input))
if __name__ =="__main__":
    main()
