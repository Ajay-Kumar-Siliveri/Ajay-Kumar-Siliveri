print("How many kilometers did you walk today?")
kms = input("Enter Kms to convert in miles:")
miles = round(float(kms)/1.60934, 2)
print(f"your {kms}km walk was {miles}mi")
