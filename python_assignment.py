class FlightTable:
    def __init__(self):
        self.data = []
    
    def add_entry(self, p_id, process, start_time, priority):
        self.data.append({'P_ID': p_id, 'Process': process, 'Start Time': start_time, 'Priority': priority})
    
    def print_table(self):
        print("Flight Table:")
        print("{:<5} {:<10} {:<15} {}".format('P_ID', 'Process', 'Start Time (ms)', 'Priority'))
        for entry in self.data:
            print("{:<5} {:<10} {:<15} {}".format(entry['P_ID'], entry['Process'], entry['Start Time'], entry['Priority']))
    
    def sort_by_p_id(self):
        self.data.sort(key=lambda entry: entry['P_ID'])
    
    def sort_by_start_time(self):
        self.data.sort(key=lambda entry: entry['Start Time'])
    
    def sort_by_priority(self):
        priority_order = {'High': 3, 'MID': 2, 'Low': 1}  # Define custom order
        self.data.sort(key=lambda entry: priority_order[entry['Priority']], reverse=True)


def main():
    flight_table = FlightTable()
    
    flight_table.add_entry('P1', 'VSCode', 100, 'MID')
    flight_table.add_entry('P23', 'Eclipse', 234, 'MID')
    flight_table.add_entry('P93', 'Chrome', 189, 'High')
    flight_table.add_entry('P42', 'JDK', 9, 'High')
    flight_table.add_entry('P9', 'CMD', 7, 'High')
    flight_table.add_entry('P87', 'NotePad', 23, 'Low')
    
    while True:
        print("\nSorting Options:")
        print("1. Sort by P_ID\n2. Sort by Start Time\n3. Sort by Priority\n4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            flight_table.sort_by_p_id()
            flight_table.print_table()
        elif choice == 2:
            flight_table.sort_by_start_time()
            flight_table.print_table()
        elif choice == 3:
            flight_table.sort_by_priority()
            flight_table.print_table()
        elif choice == 4:
            print("Exiting...")

            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

    
