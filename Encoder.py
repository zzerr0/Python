#PROGRAMMING AN ENCODER

message = input("Enter Your Message \n")
print("Following is the unicode encryption for your message")
for i in message:
  print(ord(i),end = " ")
