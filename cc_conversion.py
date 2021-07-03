#docs: https://www.currencyconverterapi.com/docs 
import requests
import tkinter as tk
import tkinter as tk

OptionList = [
"Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
"Australia", "Austria", "Azerbaija", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Côte d'Ivoire", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica","Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Democratic Republic of the Congo", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. <<Swaziland>>)", "Ethiopia", "Fiji","Finland", "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Holy See", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi" , "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania","Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan",
"Palau", "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia","Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay", "Uzbekistan", "Vanuatu", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

app = tk.Tk()
app.geometry('500x500')

var = tk.StringVar(app)
var.set("List of countries")

opt = tk.OptionMenu(app, var, *OptionList)
opt.config(width=90, font=('Calibri', 10))
opt.pack()

app.mainloop()

CNT_list = []
a = int(input("How many countries' currency names would you like to know?\nEnter a number: "))
b = 0
print("Enter the name of the countries below")

while b < a:
  cnt = input(": ")
  b = b + 1



f, t, a = input("Enter the starting currency (XXX) and the final currency you want to convert your amount in (YYY) + the amount you want to convert, everything separated by a comma\n>> ").split(", ")

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
    if not req.status_code == 200:
      raise AssertionError
    if req.json() == {}:
      print('No data found for the conversion, probably a wrong currency code, :/')
    return req.json()[curr_code]


curr_instance = curr_main()
curr_cod = curr_instance.generate_curr_code(f,t)
final_amount = curr_instance.convert(curr_cod)
print(round(final_amount * float(a), 3))



