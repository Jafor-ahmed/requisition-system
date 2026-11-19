from requisition_system import Requisition

requisition1 = Requisition("03/04/2024", "FN19", "John Paul")
print(requisition1.add_requisition(["T-shirts", "Jeans"], [150, 300]))
print(requisition1.approve_requisition())
print(requisition1.approval_reference)

requisition2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
print(requisition2.add_requisition(["Sweatshirts"], [1000]))
print(requisition2.approve_requisition())
print(requisition2.approval_reference)
requisition1.display_requisitions()
requisition1.requisition_statistics()