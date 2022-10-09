from colorama import *

def totalPaymentRequest():
  totalPayment = input(f"What is the total cost of the payment? {Style.DIM}[Integer value]{Style.RESET_ALL}: ")
  return totalPayment

try:
  totalPayment = int(totalPaymentRequest())
except:
  print("Invalid payment amount")
  totalPaymentRequest()

def yearsRequest():
  years = input(f"How many years? {Style.DIM}[Integer value]{Style.RESET_ALL}: ")
  return years

try:
  years = int(yearsRequest())
except:
  print("Invalid payment amount")
  yearsRequest()

def interestPercentRequest():
  interestPercent = input(f"Interest percent {Style.DIM}[Float (No %)]{Style.RESET_ALL}: ")
  return interestPercent

try:
  interestPercent = float(interestPercentRequest())
except:
  print(f"{Fore.RED}Invalid interest percent")
  interestPercentRequest()

numberOfPayments = years * 12
years = str(years)
toBePaid = (totalPayment * (interestPercent/100)) + totalPayment
perMonth = toBePaid / numberOfPayments
perMonth = str(round(perMonth, 5))
interest = (interestPercent/100)*totalPayment

print(f"~ ${Fore.MAGENTA + Style.BRIGHT + perMonth}{Style.RESET_ALL} per month for {Fore.CYAN + years} year(s)")
print(f"{Style.BRIGHT + Fore.CYAN}|", end="")
for i in range(round((totalPayment/toBePaid) * 50)):
  print(f"{Fore.YELLOW + Style.BRIGHT}■", end ="")

for i in range(round((interest/toBePaid) * 50)):
  print(f"{Fore.MAGENTA + Style.BRIGHT}■", end ="")

print(f"{Style.BRIGHT + Fore.CYAN}|", end="")

print(f"\n{Fore.YELLOW}■ Payment - ${totalPayment}")
print(f"{Fore.MAGENTA}■ Additional Interest - ${interest}")
print(f"{Fore.CYAN}Total - ${toBePaid}")