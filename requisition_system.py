requisition_counter = 0


class Requisition:
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        requisition_counter = requisition_counter + 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = requisition_counter + 10000
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.all_requisitions.append(self)

    def make_reference(self):
        return self.staff_id + str(self.requisition_id)[-3:]

    def add_requisition(self, items):
        self.total = 0
        for item in items:
            name = item[0]
            cost = item[1]
            if cost <= 0:
                print(f"Item '{name}' skipped: cost must be more than $0")
            else:
                self.total = self.total + cost
        return self.total

    def approve_requisition(self):
        if self.status != "Pending":
            print(f"Requisition {self.requisition_id} is already {self.status}")
        elif self.total <= 0:
            print(f"Requisition {self.requisition_id} has no valid items")
        elif self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.make_reference()
        return self.status