def print_variables():
	first_name = "balaji"
	last_name = "sivakumar"
	return first_name+ " " +last_name

def get_names():
	user_name = input("Enter user first_name: ")
	return user_name


if __name__ == "__main__":
	print(print_variables())
	get_names()