inv:
	@ python3 inv.py
mod_pow:
	@ gcc -o temp mod_pow.c 
	@ ./temp
	@ rm temp
3:
	@ python3 3.py