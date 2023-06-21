import csv

with open("voterslist.csv", "w", newline="") as data_list:
    column_details = ["Name", "Age", "Voting-Eligibility"]
    user_data = []
    num = int(input("Enter the Number of Persons You Need to Enter: "))
    
    for i in range(1, num + 1):
        print(f"Person {i}:")
        name = input("Enter Person Name: ")
        age = int(input("Enter Person Age: "))
        if age > 17:
            eligibility = "Eligible"
        else:
            eligibility = "Not Eligible"
        update = {"Name": name, "Age": age, "Voting-Eligibility": eligibility}
        user_data.append(update)
    
    print(user_data)
    
    writer = csv.DictWriter(data_list, fieldnames=column_details)
    writer.writeheader()
    
    for row in user_data:
        writer.writerow(row)
    
    print("Data written to the file.")
