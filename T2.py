from math import ceil

call = float(input("Enter minutes: "))
text = int(input("Enter texts: "))
data = float(input("Enter data in GB: "))

data = ceil(data)

cost_call = 0.05 * call
cost_text = 0.1 * text
cost_data = 0.5 * data

if data > 10:
    cost_total = cost_data
else:
    cost_total = cost_call + cost_text + cost_data

print(cost_total)