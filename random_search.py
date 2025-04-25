import random

hotel_list = [
    {"name": "Hotel A", "distance": 1.2, "price": 1200},
    {"name": "Hotel B", "distance": 3.5, "price": 950},
    {"name": "Hotel C", "distance": 0.8, "price": 1500},
    {"name": "Hotel D", "distance": 2.4, "price": 800},
    {"name": "Hotel E", "distance": 4.0, "price": 2000},
    {"name": "Hotel F", "distance": 5.5, "price": 1100},
    {"name": "Hotel G", "distance": 1.9, "price": 1300},
    {"name": "Hotel H", "distance": 6.2, "price": 900},
    {"name": "Hotel I", "distance": 0.5, "price": 1700},
    {"name": "Hotel J", "distance": 7.0, "price": 1150},
    {"name": "Hotel K", "distance": 3.1, "price": 1600},
    {"name": "Hotel L", "distance": 2.8, "price": 1400},
    {"name": "Hotel M", "distance": 8.5, "price": 750},
    {"name": "Hotel N", "distance": 4.7, "price": 1250},
    {"name": "Hotel O", "distance": 1.0, "price": 1900},
    {"name": "Hotel P", "distance": 5.9, "price": 1050},
    {"name": "Hotel Q", "distance": 2.0, "price": 1550},
    {"name": "Hotel R", "distance": 6.7, "price": 850},
    {"name": "Hotel S", "distance": 3.8, "price": 1350},
    {"name": "Hotel T", "distance": 0.9, "price": 1800}
]

def scale_list(my_list, feature_name):    
    d_max = my_list[0][feature_name]
    d_min  = d_max
    for i in range(1,len(my_list)):
        if my_list[i][feature_name]>d_max:
            d_max = my_list[i][feature_name]
        
        if my_list[i][feature_name]<d_min:
            d_min = my_list[i][feature_name]

    for i in range(len(my_list)):
        x = my_list[i][feature_name]
        new_x = (x - d_min) / (d_max - d_min)
        my_list[i][feature_name+"_normalized"] = new_x
           
    return hotel_list
    

def generate_score(mylist):
    for i in mylist:
        i["score"] = (i["distance_normalized"] + i["price_normalized"])/2
    return mylist
    


hotel_list = scale_list(hotel_list, "price")
hotel_list = scale_list(hotel_list, "distance")

hotel_list_with_score = generate_score(hotel_list)
print(hotel_list_with_score)


for i in range(5):
    hotel_index = random.randint(0,len(hotel_list)-1)
    print(hotel_list_with_score[hotel_index]["name"], hotel_list_with_score[hotel_index]["score"])

