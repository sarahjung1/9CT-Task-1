import pandas as pd
import matplotlib.pyplot as plt


# Load CSV file
def load_data(filename):
    try:
        df = pd.read_csv(filename)
        print("CSV file loaded successfully.")
        return df

    except FileNotFoundError:
        print("File not found.")
        return None


# Line chart
def line_chart(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Year"], df["Total_fire_area"], marker="o")

    plt.title("Total Fire Area Over Time")
    plt.xlabel("Year")
    plt.ylabel("Total Fire Area")

    plt.grid(True)
    plt.show()


# Bar chart
def bar_chart(df):
    latest_year = df.iloc[-1]

    categories = [
        "Temperate Forest",
        "Tropical Savanna",
        "Arid Rangelands"
    ]

    values = [
        latest_year["Temperate_forest_area"],
        latest_year["Tropical_savanna_area"],
        latest_year["Arid_semi_arid_rangelands_area"]
    ]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, values)

    plt.title(f"Land Area Comparison ({int(latest_year['Year'])})")
    plt.ylabel("Area")

    plt.show()


# Pie chart
def pie_chart(df):
    latest_year = df.iloc[-1]

    labels = [
        "Temperate Forest",
        "Tropical Savanna",
        "Arid Rangelands"
    ]

    sizes = [
        latest_year["Temperate_forest_area"],
        latest_year["Tropical_savanna_area"],
        latest_year["Arid_semi_arid_rangelands_area"]
    ]

    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")

    plt.title(f"Fire Area Distribution ({int(latest_year['Year'])})")
    plt.show()


# Summary statistics
def summary_statistics(df):
    print("\nSummary Statistics")
    print("===================")

    average_fire = df["Total_fire_area"].mean()
    highest_fire = df["Total_fire_area"].max()
    lowest_fire = df["Total_fire_area"].min()

    highest_year = df.loc[df["Total_fire_area"].idxmax(), "Year"]
    lowest_year = df.loc[df["Total_fire_area"].idxmin(), "Year"]

    print(f"Average Total Fire Area: {average_fire:.2f}")
    print(f"Highest Fire Area: {highest_fire}")
    print(f"Year of Highest Fire Area: {highest_year}")
    print(f"Lowest Fire Area: {lowest_fire}")
    print(f"Year of Lowest Fire Area: {lowest_year}")