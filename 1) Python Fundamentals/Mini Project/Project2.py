COST_PER_HOUR = 0.51
BUDGET = 918

cost_per_day = COST_PER_HOUR * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30  # Assuming a 30-day month
days_with_budget = BUDGET / cost_per_day

print(f"How much does it cost to operate one server per day? ${cost_per_day:.2f}")
print(f"How much does it cost to operate one server per week? ${cost_per_week:.2f}")
print(f"How much does it cost to operate one server per month? ${cost_per_month:.2f}")
print(f"How many days can I operate one server with ${BUDGET}? {int(days_with_budget)} days")