from requisition_system import Requisition

req1 = Requisition("03/04/2026", "FN19", "John Paul")
print(req1.add_requisition([["Pens", 150], ["Notebooks", 300]]))
print(req1.approve_requisition())
print(req1.approval_reference)

req2 = Requisition("05/04/2026", "FN20", "Tracy Brown")
print(req2.add_requisition([["Laptop", 1000]]))
print(req2.approve_requisition())
print(req2.approval_reference)