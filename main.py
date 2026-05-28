import data_module as dm

df = None

while True:
    print("\n=================================")
    print(" Bushfire Data Analysis System")
    print("=================================")
    print("1. Load CSV File")
    print("2. View Dataset")
    print("3. Generate Line Chart")
    print("4. Generate Bar Chart")
    print("5. Generate Pie Chart")
    print("6. Show Summary Statistics")
    print("7. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        filename = input("Enter CSV file name: ")
        df = dm.load_data(filename)

    elif choice == "2":
        if df is not None:
            print(df)
        else:
            print("Please load a CSV file first.")

    elif choice == "3":
        if df is not None:
            dm.line_chart(df)
        else:
            print("Please load a CSV file first.")

    elif choice == "4":
        if df is not None:
            dm.bar_chart(df)
        else:
            print("Please load a CSV file first.")

    elif choice == "5":
        if df is not None:
            dm.pie_chart(df)
        else:
            print("Please load a CSV file first.")

    elif choice == "6":

        if df is not None:
            dm.summary_statistics(df)
        else:
            print("Please load a CSV file first.")

    elif choice == "7":
        print("Program closed.")
        break

    else:
        print("Invalid option. Please try again.")