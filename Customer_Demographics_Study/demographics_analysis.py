import pandas as pd
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv("customer_data.csv")

# Basic Information
print("\nCustomer Dataset Overview")
print(data.head())

print("\nTotal Customers:", len(data))

# Gender Distribution
gender_count = data["Gender"].value_counts()

print("\nGender Distribution:")
print(gender_count)

# City Distribution
city_count = data["City"].value_counts()

print("\nCustomers by City:")
print(city_count)

# Average Age
avg_age = data["Age"].mean()
print("\nAverage Age:", round(avg_age, 2))

# Bar Chart - Customers by City
plt.figure(figsize=(6,4))
city_count.plot(kind="bar")
plt.title("Customers by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.show()

# Pie Chart - Gender Distribution
plt.figure(figsize=(5,5))
plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct="%1.1f%%"
)
plt.title("Customer Gender Distribution")
plt.show()