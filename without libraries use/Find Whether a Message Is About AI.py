# message = "Do you teach me ai"

# ai_keywords = ["ai", "ml", "machine", "learning", "neural", "python", "data"]

# message_words = message.lower().split()

# found_keywords = []

# for word in message_words:
#     if word in ai_keywords:
#         found_keywords.append(word)

# if len(found_keywords) > 0:
#     print("This message is related to AI/ML")
#     print("Matched words:", found_keywords)
# else:
#     print("This message is not clearly related to AI/ML")
   
   
massage = "I am go compliting AI "
ai_keywords = ["ai","machine","learning","neural","data","python"]
massage_word = massage.lower().split()
found_keywords = []
for word in massage_word:
    if word in ai_keywords: 
        found_keywords.append(word)
if len(found_keywords) > 0:
    print("This massage is related to AI/ML")
    print("Matched words :",found_keywords)
else:
    print("This massage is not clearly related to AI/ML")               
    
    