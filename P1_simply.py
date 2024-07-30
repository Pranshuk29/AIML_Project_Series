import aiml

kernel=aiml.Kernel() #this is the brain library behind AI chatbots 
kernel.learn("P1_std_startup.xml")
# kernel.respond("LOAD AIML B")
print("Welcome to AI Chatbot!")

while True:
    input_ques=input("User: ")
    if input_ques.lower() == 'exit':
        print("Adios Amigo!") #Spanish for Goodbye, my Friend
        break
    response=kernel.respond(input_ques)
    if response=='':
        response="I'm having trouble understanding. Could you please rephrase?"
        
    print("Bot: ",response)