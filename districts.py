dic = {
    "Telangana" : "Hyderabad",
    "Tamilnadu" : "Chennai",
    "Karnataka" : "Banglore",
    "Maharastra" : "Mumbai",
    "Assam" : "Dispur",
    "Bihar" : "Patna",
    "Goa" : "Panaji"
}

file1 = open("D:\One Drive Storage\OneDrive\Documents\Python Class(VS Code)\Ayesha Python\Edyoda\states.json","w")
data = json.dump(dic,file1)