import matplotlib.pyplot as plt
food_paragraph = "Plants as a food source are divided into  legumes, grains and nuts.[36] Where plants fall within these categories can vary, with botanically described fruits such as the tomato, squash, pepper and eggplant or seeds like peas commonly considered vegetables.[37] Food is a fruit if the part eaten is derived from the reproductive tissue, so seeds, nuts and grains are technically fruit.[38][39] From a culinary perspective, fruits are generally considered the remains of botanically described fruits after grains, nuts, seeds and fruits used as vegetables are removed.[40] Grains can be defined as seeds that humans eat or harvest, with cereal grains (oats, wheat, rice, corn, barley, rye, sorghum and millet) belonging to the Poaceae (grass) family[41] and pulses coming from the Fabaceae (legume) family.[42] Whole grains are foods that contain all the elements of the original seed (bran, germ, and endosperm).[43] Nuts are dry fruits, distinguishable by their woody shell.[40]"
cinema_paragraph = "Hindi cinema was experiencing thematic stagnation,[85] dominated by musical romance films.[86] Screenwriter duo Salim–Javed (Salim Khan and Javed Akhtar) revitalised the industry.[85] They established the genre of gritty, violent, Bombay underworld crime films with Zanjeer (1973) and Deewaar (1975).[87][88] They reinterpreted the rural themes of Mother India and Gunga Jumna in an urban context reflecting 1970s India,[85][89] channelling the growing discontent and disillusionment among the masses,[85] unprecedented growth of slums[90] and urban poverty, corruption and crime,[91] as well as anti-establishment themes.[92] This resulted in their creation of the angry young man, personified by Amitabh Bachchan,[92] who reinterpreted Kumar's performance in Gunga Jumna[85][89] and gave a voice to the urban poor.[90] The women on the other hand were shown as ones who have adopted western values and outfits especially by heroines like Parveen Babi (who was featured on the cover of Time magazine for a story on Bollywood's success) and Zeenat Aman.By the mid-1970s, Bachchan's position as a lead actor was solidified by crime-action films Zanjeer and Sholay (1975)."
food = [
    "tomato",
    "pea",
    "nut",
    "grain",
    "vegetable",
    "seed",
    "fruit"
]
cinema = [
    "deewar",
    "ganga yamuna",
    "sholay",
    "zeenat aman",
    "zanjeer",
    "parveen babi",
]
message_text= food_paragraph.lower()
found_keywords = []
for word in food:
    count = message_text.count(word.lower())
    if count > 0:
        found_keywords.append((word, count))

if len(found_keywords) > 0:
    print("This message is related to Food")
    print("Matched words:", found_keywords)
    
else:
    print("This message is not clearly related to Food")
    

cinema_text=cinema_paragraph.lower()
found_word = []
for word in cinema:
    count = cinema_text.count(word.lower())
    if count > 0:
        found_word.append((word, count))

if len(found_word) > 0:
    print("This message is related to Cinema")
    print("Matched words:", found_word)
else:
    print("This message is not clearly related to Cinema")
    

food_words = [word for word, count in found_keywords]
food_counts = [count for word, count in found_keywords]

cinema_words = [word for word, count in found_word]
cinema_counts = [count for word, count in found_word]
plt.bar(food_words, food_counts, alpha=0.7, label="Food")
plt.bar(cinema_words, cinema_counts, alpha=0.7, label="Cinema")
plt.xlabel("Keywords")
plt.ylabel("Counts")
plt.title("Food vs Cinema Keywords")

plt.legend()
plt.show()