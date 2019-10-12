def npv(beta, riskfree, riskmarket):
	"""
	Basic function to calculate the net present value 
	*Note* only currently works for identical cash flows 

	Beta:
	Risk Free: 
	Risk Market: 

	How to calculate the Net Present Value(NPV):
	rProject = rF + ß(E[rm] - rf)
	"""
	# Ask the user for cash flows:
	years = int(input("How many years in the project (starting index 0): "))
	num_years = []
	for number in range(0, int(years)):
		num_years.append(number)
	
	print("There are " + str(len(num_years)) + " years in the project.")

	inital_cfoutlay = input("What is the initial cashflow outlay?: ")
	cashflow = input("What are the year over year cash flows?: ")
	# Step 1 Risk of Project Calculation 
	project_risk = riskfree + beta * (riskmarket - riskfree)
	#project_risk = int(r)
	print('Return = ' + str((project_risk * 100)) + '%' ) 
	
	# Step 2 Annuity Factor Calculation
	annuity_factor = (1-1/(1+project_risk)**years)/project_risk
	print('Annuity Factor = ' + str(annuity_factor))

	# Step 3 NPV Calculation
	npv = float(inital_cfoutlay) + ((float(cashflow) * float(annuity_factor)))
	print((str(round(npv, 4))) + '%')
npv(2, .03, .1)
