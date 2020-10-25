rented = {"asen" : {"pirin": 5, "cska": 4, "juve": 6}, "julia": {"love": 10, "skae": 5}}
ll = []
tok = [ll.append([k, v]) for k, v in rented.items()]
usr = ""
days_t = 0
for x in ll:
    usr = x[0]
    if "juve" in x[1]:
        days_t = x[1]["juve"]
        break

print(ll)

print(f"The book \"{'juve'}\" is already rented and will be available in available in {days_t} by {usr}")