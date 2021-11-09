import pulp


def expression(prob):
	x = pulp.LpVariable('x', 0, None)
	y = pulp.LpVariable('y', 0, None)
	prob += -8 * x - 9 * y
	prob += -15 * x - y <= -62
	prob += -3 * x - 10 * y >= -136
	prob += 3 * x - 10 * y <= -24
	prob += -10 * x + 5 * y >= -105
	print(prob)
	prob.solve()
	print('Status: ', pulp.LpStatus[prob.status])
	print(pulp.value(x), pulp.value(y), pulp.value(prob.objective))


def func(exercise: int, word=None):
	if exercise == 1:
		if word == 'max':
			prob = pulp.LpProblem('MAX', pulp.LpMaximize)
			expression(prob)
		elif word == 'min':
			prob = pulp.LpProblem('MIN', pulp.LpMinimize)
			expression(prob)
		else: print('Попробуйте еще раз.')
	if exercise == 2:
		prob = pulp.LpProblem('MAX', pulp.LpMaximize)
		x = pulp.LpVariable('x', 0, None)
		y = pulp.LpVariable('y', 0, None)
		prob += -5 * x - y
		prob += -3 * x - 4 * y >= -44
		prob += -3 * x + 3 * y >= 3
		print(prob)
		prob.solve()
		print('Status: ', pulp.LpStatus[prob.status])
		print(pulp.value(x), pulp.value(y), pulp.value(prob.objective))
	elif exercise == 3:
		prob = pulp.LpProblem('MAX', pulp.LpMaximize)
		x1 = pulp.LpVariable('x1', 0, None)
		x2 = pulp.LpVariable('x2', 0, None)
		x3 = pulp.LpVariable('x3', 0, None)
		prob += 5 * x1 + 4 * x2 + 5 * x3
		prob += 17 * x1 + 3 * x2 + 5 * x3 <= 390
		prob += 13 * x1 + 7 * x2 + 12 * x3 <= 251
		prob += 7 * x1 + 7 * x2 + 3 * x3 <= 266
		print(prob)
		prob.solve()
		print('Status: ', pulp.LpStatus[prob.status])
		print(pulp.value(x1), pulp.value(x2), pulp.value(x3), pulp.value(prob.objective))
	elif exercise == 4:
		prob = pulp.LpProblem('MAX', pulp.LpMaximize)
		x1 = pulp.LpVariable('x1', 0, None)
		x2 = pulp.LpVariable('x2', 0, None)
		x3 = pulp.LpVariable('x3', 0, None)
		prob += 6 * x1 + x2 + 5 * x3
		prob += 7 * x1 + 17 * x2 + 17 * x3 <= 242
		prob += 16 * x1 + 5 * x2 + x3 <= 329
		prob += 18 * x1 + 3 * x2 + 3 * x3 <= 325
		print(prob)
		prob.solve()
		print('Status: ', pulp.LpStatus[prob.status])
		print(pulp.value(x1), pulp.value(x2), pulp.value(x3), pulp.value(prob.objective))
	else: print('Попробуй еще раз)')


if __name__ == '__main__':
	exercise = int(input('Введите номер задания: '))
	if exercise == 1:
		word = str(input('Введите max или min: '))
		func(exercise, word)
	else: func(exercise)
