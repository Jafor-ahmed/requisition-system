from requisition_system import Requisition, all_requisitions

while True:
    requisition = Requisition()
    requisition.enter_requisition()
    print("")
    requisition.show_requisition()

    answer = input("Add another requisition (yes/no): ")
    print("")
    if answer.lower() != "yes":
        break

for current in all_requisitions:
    if current.status == "Pending":
        print("Manager response needed")
        current.show_requisition()
        response = input("Type Approved or Not approved (press Enter to keep Pending): ")
        print("")
        if response != "":
            current.respond_to_requisition(response)

requisition.display_requisitions()
requisition.requisition_statistics()