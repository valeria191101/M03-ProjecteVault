import unittest
# Intentem importar del nou mòdil que encara no existeix
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):
	def test_password_length(self):
		# Mínim 8 caràcters
		self.assertFalse(check_password("Ab123"))
		self.assertTrue(check_password("Ab1234567"))
	def test_password_numbers(self):
		#Ha de contenir majúscules
		self.assertFalse(check_password("PasswordSenseNumeros"))
		self.assertTrue(check_password("PasswordAmb123"))
	def test_password_uppercase(self):
		#Ha de contenir majúscules
		self.assertFalse(check_password("nomajuscules123"))
		self.assertTrue(check_password("SiMajuscules123"))
	def test_password_no_admin(self):
		# No ha de contenir la paraula "admin" (insensible a majúscules)
		self.assertFalse(check_password("Admin12345"))
		self.assertFalse(check_password("sistema_admin_99"))
		self.assertTrue(check_password("VaultUser2024"))

if __name__ == "__main__":
	unittest.main()
