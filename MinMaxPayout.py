from random import randint, seed



def maximalPayout(base_pay):
	'''Maximal payout to each employee'''

	# Base case
	pay = base_pay
	distribution = [1] # pay one to the minimal employee
	pay -= 1

	lambsToPay, length, total, position = 1, 1, 1, 0

	while pay > 0:

		lambsToPay = lambsToPay * 2 # Rule 2 applied here to maximize payout

		if total + lambsToPay > base_pay:

			break

		total += lambsToPay

		length += 1

		position += 1

		pay -= lambsToPay

	return length




def minimalPayout(base_pay):
	'''Minimal payout to each worker'''

	# Base case
	pay = base_pay
	distribution = [1] # pay one to the minimal employee
	pay -= 1
	lambsToPay, length, total, position = 1, 1, 1, 0
	prevSubs = [0, 1]

	while pay > 0:

		lambsToPay = sum(prevSubs) # This is rule 3 -> Can't pay less than past 2 subordinates

		if total + lambsToPay > base_pay:

			break

		total += lambsToPay # Add lambs paid to total

		# Swap prevSubs
		prevSubs[0] = prevSubs[1]
		prevSubs[1] = lambsToPay

		length += 1 # Extra employee paid

		position += 1 # Increment position

		pay -= lambsToPay # Deduct lambs paid

	return length


def answer(pay):

	return minimalPayout(pay) - maximalPayout(pay)



def test():
	seed(1000)
	cases = [randint(10, 10*9) for i in range(100)]

	for case in cases:
		try:
			answer(case)
		except:
			print(False)
test()
