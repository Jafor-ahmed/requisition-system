from requisition_system import Requisition

req1 = Requisition("03/04/2024", "FN19", "John Paul")
req1.add_requisition([["Pens", 150], ["Notebooks", 300]])
req1.approve_requisition()

req2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
req2.add_requisition([["Laptop stand", 400], ["Monitor", 600]])
req2.approve_requisition()

req3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
req3.add_requisition([["Printer", 2500], ["Toner", 1000]])
req3.approve_requisition()

req4 = Requisition("03/05/2024", "FN02", "Catlin White")
req4.add_requisition([["Desk lamp", 90], ["Chair", 400]])
req4.approve_requisition()

req5 = Requisition("10/05/2024", "FN07", "Sam Lee")
req5.add_requisition([["Keyboard", 200], ["Mouse", 300]])
req5.approve_requisition()

req6 = Requisition("12/05/2024", "FN11", "Aroha Smith")
req6.add_requisition([["Stapler", 10.50], ["Tape", 15], ["Sticker", -5]])
req6.approve_requisition()

print("Before manager responses")
print("")
Requisition.display_requisitions()
Requisition.requisition_statistics()

print("Manager responses")
req3.respond_to_requisition("Not approved")
req5.respond_to_requisition("Approved")
req1.respond_to_requisition("Approved")
req2.respond_to_requisition("Maybe")
print("")

print("After manager responses")
print("")
Requisition.display_requisitions()
Requisition.requisition_statistics()