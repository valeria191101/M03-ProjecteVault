def check_password(pwd):
	# 1. Comprovar longitud mínima de 8
	if len(pwd) < 8:
		return False
	# 2. Comprovar si conté almenys un número 
	if not any(char.isdigit() for char in pwd):
		return False
	#3. Comprovar si conté almenys una majúscula 
	if not any(char.isupper() for char in pwd):
		return False 
	#4. Comprovar que No contingui la paraula "admin"
	if "admin" in pwd.lower():
		return False
	return True
