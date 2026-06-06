import pandas as pd 

data = {
    "Name":["karan", "anhay","tarun", "shaurya", "anuj", "Yash","KARTIKYA"],
    "course":["data science","data science","data science","aiml","aiml","aiml","aiml"],
    "marks":[67, 78, 98, 88,49,95,77]
}

df = pd.DataFrame(data)

print(" COURSE DATA:")
print(df)

print("AVERAGE MARKS IN COURSES")
print(df.groupby("course")["marks"].mean())

print(" TOTAL MARKS :")
print(df.groupby("course")["marks"].sum())

print("NO OF STIDENTS ENROOLL IN COURSES:")
print(df.groupby("course")["Name"].count())





