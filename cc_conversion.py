#docs: https://www.currencyconverterapi.com/docs 
import requests

f, t, a = input("Enter the starting currency (XXX) and the final currency you want to convert your amount in (YYY) + the amount you want to convert, separated by a comma\n>> ").split(", ")

class curr_main:
  def __init__(self):
    self.apikey = "e00d40017f8b8832f6c7"
    self.baseurl = "https://free.currconv.com/api/v7/"

  def countries(self): #to return list of countries
    req = requests.get(self.baseurl + "countries?apiKey=" + self.apikey)
    return req.json()

  def currencies(self): #to return currencies
    req = requests.get(self.baseurl + "currencies?apiKey=" + self.apikey)
    return req.json()

  def generate_curr_code(self, f, t):
    curr_code = f + "_" + t 
    return curr_code

  def convert(self, curr_code):
    parameter = {
      "apiKey":self.apikey,
      "compact":"ultra",
      "q":curr_code
    }
    req = requests.get(self.baseurl + "convert", params = parameter)
    return req.json()[curr_code]

curr_instance = curr_main()

curr_cod = curr_instance.generate_curr_code(f,t)
final_amount = curr_instance.convert(curr_cod)
print(round(final_amount * float(a), 3))
