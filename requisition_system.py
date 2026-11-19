requisition_counter = 0
all_requisitions = []


class Requisition:
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        requisition_counter = requisition_counter + 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = requisition_counter + 10000
        self.item_names = []
        self.item_prices = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        all_requisitions.append(self)

    def add_requisition(self, item_names, item_prices):
        self.item_names = []
        self.item_prices = []
        self.total = 0

        if len(item_names) != len(item_prices):
            print("Each item needs a name and a price")
            return self.total

        for i in range(len(item_prices)):
            if item_prices[i] <= 0:
                print("Item " + item_names[i] + " skipped: price must be more than $0")
            else:
                self.item_names.append(item_names[i])
                self.item_prices.append(item_prices[i])
                self.total = self.total + item_prices[i]

        return self.total

    def approve_requisition(self):
        if self.status != "Pending":
            print(f"Requisition {self.requisition_id} is already {self.status}")
        elif self.total == 0:
            print(f"Requisition {self.requisition_id} has no valid items")
        elif self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

        return self.status

    def respond_to_requisition(self, response):
        if self.status != "Pending":
            print(f"Requisition {self.requisition_id} is already {self.status}")
        elif self.total == 0:
            print(f"Requisition {self.requisition_id} has no valid items")
        elif response == "Approved":
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        elif response == "Not approved":
            self.status = "Not approved"
        else:
            print("Response must be 'Approved' or 'Not approved'")

        return self.status

    def show_requisition(self):
        if self.total == int(self.total):
            total_text = str(int(self.total))
        else:
            total_text = f"{self.total:.2f}"

        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${total_text}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")
        print("")

    def display_requisitions(self):
        print("Displaying the Requisitions")
        print("")
        for requisition in all_requisitions:
            requisition.show_requisition()

    def requisition_statistics(self):
        submitted = len(all_requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in all_requisitions:
            if requisition.status == "Approved":
                approved = approved + 1
            elif requisition.status == "Pending":
                pending = pending + 1
            elif requisition.status == "Not approved":
                not_approved = not_approved + 1

        print("Displaying the Requisition Statistics")
        print("")
        print(f"The total number of requisitions submitted: {submitted}")
        print(f"The total number of approved requisitions: {approved}")
        print(f"The total number of pending requisitions: {pending}")
        print(f"The total number of not approved requisitions: {not_approved}")
        print("")

        return submitted, approved, pending, not_approved