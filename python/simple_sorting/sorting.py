patients = [
    {"name": "muntashir", "type": "emergency", "arrival": 2},
    {"name": "mmm", "type": "regular", "arrival": 2},
    {"name": "alice", "type": "emergency", "arrival": 1},
    {"name": "bob", "type": "regular", "arrival": 1},
    {"name": "charlie", "type": "emergency", "arrival": 2},
    {"name": "david", "type": "regular", "arrival": 3}
]

type_priority = {
    "emergency": 0,
    "regular": 1,
}

sorted_patients = sorted(patients, key=lambda k: (type_priority[k["type"]], k["arrival"], k["name"]))
print(sorted_patients)
final_priority_queue = []
for patient in sorted_patients:
    final_priority_queue.append(patient["name"])

print(final_priority_queue)

#Another Approch
emergency_queue = []
regular_queue = []

for patient in patients:
    if patient["type"] == "emergency":
        emergency_queue.append(patient)
    else:
        regular_queue.append(patient)
for i in range(len(emergency_queue)):
    for j in range(i+1,  len(emergency_queue)):
        if emergency_queue[j]["arrival"] < emergency_queue[i]["arrival"] or \
                (emergency_queue[j]["arrival"] == emergency_queue[i]["arrival"] and emergency_queue[j]["name"] < emergency_queue[i]["name"]):
            emergency_queue[i], emergency_queue[j] = emergency_queue[j], emergency_queue[i]

for i in range(len(regular_queue)):
    for j in range(i+1,  len(regular_queue)):
        if regular_queue[j]["arrival"] < regular_queue[i]["arrival"] or \
                (regular_queue[j]["arrival"] == regular_queue[i]["arrival"] and regular_queue[j]["name"] < regular_queue[i]["name"]):
            regular_queue[i], regular_queue[j] = regular_queue[j], regular_queue[i]

final_priority_queue2 = []
patients_sorted = emergency_queue + regular_queue
for patient in patients_sorted:
    final_priority_queue2.append(patient["name"])
print(final_priority_queue2)