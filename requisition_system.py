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

    def format_total(self):
        if self.total == int(self.total):
            return str(int(self.total))
        return f"{self.total:.2f}"

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

    def respond_to_requisition(self, response):
        if self.status != "Pending":
            print(f"Requisition {self.requisition_id} is already {self.status}")
        elif self.total <= 0:
            print(f"Requisition {self.requisition_id} has no valid items")
        elif response == "Approved":
            self.status = "Approved"
            self.approval_reference = self.make_reference()
        elif response == "Not approved":
            self.status = "Not approved"
        else:
            print("Response must be 'Approved' or 'Not approved'")
        return self.status

    def show_requisition(self):
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.format_total()}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")
        print("")

    @staticmethod
    def display_requisitions():
        print("Displaying the Requisitions")
        print("")
        for requisition in Requisition.all_requisitions:
            requisition.show_requisition()

    @staticmethod
    def requisition_statistics():
        submitted = len(Requisition.all_requisitions)
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in Requisition.all_requisitions:
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