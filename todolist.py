# def practice(num_one, num_two):
#     answer = num_one + num_two
#     return answer
my_list = []
answer = ""

while (True):
    def user_input(question):
        answer = input(question)
        return(answer)

# user_input("What's is your task?")

    def add_answer(task):
        my_list.append(task)
        print(my_list)

    add_answer(user_input("What's is your task?"))