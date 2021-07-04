#docs: https://www.currencyconverterapi.com/docs 
import requests
import tkinter as tk

OptionList = [
"Afghanistan: AFN", "Akrotiri and Dhekelia: EUR", "Aland Islands: EUR", "Albania: ALL", "Algeria: DZD", "American Samoa: USD", "Andorra: EUR", "Angola: AOA", "Anguilla: XCD", "Antigua and Barbuda: XCD", "Argentina: ARS", "Armenia: AMD",
"Aruba: AWG", "Ascension Island : SHP", "Australia: AUD", "Austria: EUR", "Azerbaija: AZN", "Bahamas: BSD", "Bahrain: BHD", "Bangladesh: BDT", "Barbados: BBD", "Belarus: BYN", "Belgium: EUR", "Belize: BZD", "Benin: XOF", "Bermuda: BMD", "Bhutan: BTN", "Bolivia: BOB", "Bonaire: USD", "Bosnia and Herzegovina: BAM", "Botswana: BWP", "Brazil: BRL", "British Indian Ocean Territory : USD", "British Virgin Islands: USD", "Brunei: BND", "Bulgaria: BGN", "Burkina Faso: XOF", "Burundi: BIF", "Cabo Verde: CVE", "Cambodia: KHR", "Cameroon: XAF", "Canada: CAD", "Caribbean Netherlands: USD", "Cayman Islands: KYD", "Central African Republic: XAF", "Chad: XAF", "Chatham Islands: NZD", "Chile: CLP", "China: CNY", "Christmas Island: AUD", "Cocos (Keeling) Islands: AUD", "Colombia: COP", "Comoros: KMF", "Congo, Democratic Republic of the: CDF", "Congo, Republic of the: XAF", "Cook Islands: none", "Costa Rica: CRC", "Côte d'Ivoire: XOF", "Croatia: HRK", "Cuba: CUP", "Curacao: ANG", "Cyprus: EUR", "Czechia (Czech Republic): CZK", "Denmark: DKK", "Djibouti: DJF", "Dominica: XCD", "Dominican Republic: DOP", "Ecuador: USD", "Egypt: EGP", "El Salvador: USD", "Equatorial Guinea: XAF", "Eritrea: ERN", "Estonia: EUR", "Eswatini (fmr. <<Swaziland>>): SZL", "Falkland Islands: FKP", "Ethiopia: ETB", "Faroe Islands : none", "Fiji: FJD","Finland: EUR", "France: EUR", "French Guiana: EUR", "French Polynesia: XPF" "Gabon: XAF", "Gambia: GMD", "Georgia: GEL", "Germany: EUR", "Ghana: GHS", "Gibraltar: GIP", "Greece: EUR", "Greenland : DKK", "Grenada: XCD", "Guadeloupe: EUR", "Guam: USD", "Guernsey: GGP", "Guatemala: GTQ", "Guinea: GNF", "Guinea-Bissau: XOF", "Guyana: GYD", "Haiti: HTG", "Holy See: EUR", "Honduras: HNL", "Hong Kong: HDK", "Hungary: HUF", "Iceland: ISK", "India: INR", "Indonesia: IDR", "International Monetary Fund (IMF): XDR", "Iran: IRR", "Iraq: IQD", "Ireland: IRR", "Isle of MaN: IMP", "Israel: ILS", "Italy: EUR", "Jamaica: JMD", "Japan: JPY", "Jersey: JEP", "Jordan: JOD", "Kazakhstan: KZT", "Kenya: KES", "Kiribati: AUD", "Kosovo: EUR", "Kuwait: KWD", "Kyrgyzstan: KGS", "Laos: LAK", "Latvia: EUR", "Lebanon: LBP", "Lesotho: LSL", "Liberia: LRD", "Libya: LYD", "Liechtenstein: CHF", "Lithuania: EUR", "Luxembourg: EUR", "Macau: MOP", "Madagascar: MGA", "Malawi: MWK" , "Malaysia: MYR", "Maldives: MVR", "Mali: XOF", "Malta: EUR", "Marshall Islands: USD", "Martinique : EUR", "Mauritania: MRU", "Mauritius: MUR", "Mayotte: EUR", "Mexico: MXN", "Micronesia: USD", "Moldova: MDL", "Monaco: EUR", "Mongolia: MNT", "Montenegro: EUR", "Montserrat: XCD", "Morocco: MAD", "Mozambique: MZN", "Myanmar (formerly Burma): MMK", "Namibia: NAD", "Nauru: AUD", "Nepal: NPR", "Netherlands: EUR", "New Caledonia: XPF", "New Zealand: NZD", "Nicaragua: NIO", "Niger: XOF", "Nigeria: NGN", "Niue : NZD", "Norfolk Island: AUD", "Northern Mariana Islands: USD" "North Korea: KPW", "North Macedonia (formerly Macedonia): MKD", "Norway: NOK", "Oman: OMR", "Pakistan: PKR",
"Palau: USD", "Palestine State: ILS", "Panama: USD", "Papua New Guinea: PGK", "Paraguay: PYG", "Peru: PEN", "Philippines: PHP", "Pitcairn Islands: NZD", "Poland: PLN", "Portugal: EUR", "Puerto Rico: USD", "Qatar: QAR", "Reunion : EUR", "Romania: RON", "Russia: RUB", "Rwanda: RWF", "Saba : USD", "Saint Barthelemy : USD", "Saint Helena: SHP", "Saint Kitts and Nevis: XCD", "Saint Lucia: XCD", "Saint Martin: EUR", "Saint Pierre and Miquelon: EUR", "Saint Vincent and the Grenadines: XCD", "Samoa: WST", "San Marino: EUR", "Sao Tome and Principe: STN", "Saudi Arabia: SAR", "Senegal: XOF", "Serbia: RSD", "Seychelles: SCR", "Sierra Leone: SRR", "Singapore: SGD", "Sint Eustatius: USD", "Sint Maarten: ANG", "Slovakia: EUR", "Slovenia: EUR", "Solomon Islands: SBD", "Somalia: SOS", "South Africa: ZAR", "South Georgia Island: GBP", "South Korea: KRW", "South Sudan: SSP", "Spain: EUR", "Sri Lanka: LKR", "Sudan: SDG", "Suriname: SRD", "Svalbard and Jan Mayen: NOK", "Sweden: SEK", "Switzerland: CHF", "Syria: SYP", "Taiwan: TWD", "Tajikistan: TJS", "Tanzania: TZS", "Thailand: THB", "Timor-Leste: USD", "Togo: XOF", "Tokelau : NZD","Tonga: TOP", "Trinidad and Tobago: TTD", "Tristan da Cunha: GBP", "Tunisia: TND", "Turkey: TRY", "Turkmenistan: TMT", "Turks and Caicos Islands: USD", "Tuvalu: AUD", "Uganda: UGX", "Ukraine: UAH", "United Arab Emirates. AED", "United Kingdom: GBP", "United States of America: USD", "Uruguay: UYU", "US Virgin Islands : USD", "Uzbekistan: UZS", "Vanuatu: VUV", "Venezuela: VES", "Vietnam: VND", "Wake Island: USD", "Wallis and Futuna: XPF","Yemen: YER", "Zambia: ZMW", "Zimbabwe: USD"
]

app = tk.Tk()
app.title('Currency Converter')
app.geometry('1000x1000')
app.resize = False
app.config(bg = "black")

label_one = tk.Label(text = "CURRENCY CONVERTER", bg = "black", fg = "white")
label_one.config(font = ("Calibri", 15))
label_one.pack(pady = 10)

var = tk.StringVar(app)
var.set("CLICK ME TO SEE THE CURRENCIES")

opt = tk.OptionMenu(app, var, *OptionList)
opt.config(width=90, font=('Calibri', 15, "bold"))
opt.pack()

L2 = tk.Label(app, text = "Enter the starting currency (XXX)", bg = "black", fg = "white", font= ('Calibri', 14))
L2.place(x = 0, y = 250)
E2 = tk.Entry(app, bd = 5)
E2.place(x = 500, y = 250)
    
L3 = tk.Label(app, text = "Enter the currency you want to convert your amount in (YYY)", bg = "black", fg = "white", font= ('Calibri', 14))
L3.place(x = 0, y = 310)
E3 = tk.Entry(app, bd = 5)
E3.place(x = 500, y = 310)

L4 = tk.Label(app, text = "Enter the amount you want to convert", bg = "black", fg = "white", font= ('Calibri', 14))
L4.place(x = 0, y = 370)
E4 = tk.Entry(app, bd = 5)
E4.place(x = 500, y = 370)


f = E2.get()
t = E3.get()

# C U R R E N C Y . 1

def clear_text_two(self):
    E2.delete(0, 'end')
    
def lab_one(event= None):
    E2G = E2.get()
    label = E2G.title()
    clear_text_two(label)
    print(E2G)
    
# C U R R E N C Y . 2 

def clear_text_three(self):
    E3.delete(0, 'end')
    
def lab_two(event= None):
    E3G = E3.get()
    label = E3G.title()
    clear_text_three(label)
    print(E3G)
 
# A M O U N T
    
def clear_text_four(self):
    E4.delete(0, 'end')

def lab_three(event= None):
    E4G = E4.get()
    label = E4G.title()
    clear_text_four(label)
    print(E4G)

a = E4.get()   

tk.Button(app, text= (' ' + 'Press me to send' + ' '), font = ('Libre Baskerville', 12), command=lambda:[lab_one(), lab_two(), lab_three()]).place(x= 500, y= 500, anchor= 'CENTER')
app.bind('<Return>', (lab_one, lab_two, lab_three))
      
if __name__ == "__main__":
  app.mainloop()

# class curr_main:
  
#   def __init__(self):
#     self.apikey = "e00d40017f8b8832f6c7" 
#     self.baseurl = "https://free.currconv.com/api/v7/"

#   def countries(self): #to return list of countries
#     req = requests.get(self.baseurl + "countries?apiKey=" + self.apikey)
#     return req.json()

#   def currencies(self): #to return currencies
#     req = requests.get(self.baseurl + "currencies?apiKey=" + self.apikey)
#     return req.json()

#   def generate_curr_code(self, f, t):
#     curr_code = f + "_" + t 
#     return curr_code

#   def convert(self, curr_code):
#     parameter = {
#       "apiKey":self.apikey,
#       "compact":"ultra",
#       "q":curr_code
#     }
#     req = requests.get(self.baseurl + "convert", params = parameter)
#     if not req.status_code == 200:
#       raise AssertionError
#     if req.json() == {}:
#       print('No data found for the conversion, probably a wrong currency code, :/')
#     return req.json()[curr_code]


# curr_instance = curr_main()
# curr_cod = curr_instance.generate_curr_code(f,t)
# final_amount = curr_instance.convert(curr_cod)

# print(round(final_amount * float(a), 3))



