from concurrent.futures import ProcessPoolExecutor

DEDUCTION_RATES = {
	"SSS": 0.045,
	"PhilHealth": 0.025,
	"Pag-IBIG": 0.02,
	"Withholding Tax": 0.10,
}

EMPLOYEES = [
	("Alice", 25000),
	("Bob", 32000),
	("Charlie", 28000),
	("Diana", 40000),
	("Edward", 35000),
]


def compute_payroll(employee):
	name, salary = employee
	deductions = {key: salary * rate for key, rate in DEDUCTION_RATES.items()}
	total_deduction = sum(deductions.values())
	net_salary = salary - total_deduction
	return name, salary, total_deduction, net_salary


def main():
	with ProcessPoolExecutor() as executor:
		results = list(executor.map(compute_payroll, EMPLOYEES))

	for name, salary, total_deduction, net_salary in results:
		print(f"Employee: {name}")
		print(f"  Gross Salary: {salary:,.2f}")
		print(f"  Total Deduction: {total_deduction:,.2f}")
		print(f"  Net Salary: {net_salary:,.2f}")
		print("-" * 40)


if __name__ == "__main__":
	main()
