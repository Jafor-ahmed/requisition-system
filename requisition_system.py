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