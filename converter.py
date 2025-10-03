def celcius_to_fahrenheit(c):
	return (c * 9/5) + 32
	
def fahrenheit_to_celcius(f):
	return (f - 32) * 5/9
	
def main():
	print("=== Temperature Converter ===")
	print("1. Celcius to Fahrenheit")
	print("2. Fahrenheit to Celcius")
	
	pilihan = input("Choose (1/2) : ")
	
	if pilihan == "1" :
		c = float(input("Enter temperature in Celcius : "))
		f = celcius_to_fahrenheit(c)
		print(f"{c}°C = {f:.2f}°F")
	elif pilihan == "2" :
		f = float(input("Enter temperature in Fahrenheit : "))
		c = fahrenheit_to_celcius(f)
		print(f"{f}°C = {c:.2f}°F")		
	else:
		print("Invalid choice!")
		
if __name__ == "__main__":
	main()