from requisition_system import Requisition

requisition1 = Requisition("03/04/2024", "FN19", "John Paul")
requisition1.add_requisition(["Pens", "Notebooks"], [150, 300])
requisition1.approve_requisition()

requisition2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
requisition2.add_requisition(["Laptop"], [1000])
requisition2.approve_requisition()

requisition3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
requisition3.add_requisition(["Printer", "Toner"], [2500, 1000])
requisition3.approve_requisition()

requisition4 = Requisition("03/05/2024", "FN02", "Catlin White")
requisition4.add_requisition(["Desk lamp", "Chair"], [90, 400])
requisition4.approve_requisition()

requisition5 = Requisition("10/05/2024", "FN17", "Kabir Khan")
requisition5.add_requisition(["Keyboard", "Mouse"], [200, 300])
requisition5.approve_requisition()

requisition6 = Requisition("12/05/2024", "FN11", "Nibas Mohanta")
requisition6.add_requisition(["Stapler", "Tape", "Sticker"], [10.50, 15, -5])
requisition6.approve_requisition()

print("")
print("Before manager responses")
print("")
requisition1.display_requisitions()
requisition1.requisition_statistics()

print("Manager responses")
requisition3.respond_to_requisition("Not approved")
requisition5.respond_to_requisition("Approved")
requisition1.respond_to_requisition("Approved")
requisition2.respond_to_requisition("Maybe")

print("")
print("After manager responses")
print("")
requisition1.display_requisitions()
requisition1.requisition_statistics()