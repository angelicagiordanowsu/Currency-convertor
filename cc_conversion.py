import tkinter as tk
from tkinter import ttk
import requests
import keyboard

OptionList = [
"Afghanistan: AFN", "Akrotiri and Dhekelia: EUR", "Aland Islands: EUR", "Albania: ALL", "Algeria: DZD", "American Samoa: USD", "Andorra: EUR", "Angola: AOA", "Anguilla: XCD", "Antigua and Barbuda: XCD", "Argentina: ARS", "Armenia: AMD",
"Aruba: AWG", "Ascension Island : SHP", "Australia: AUD", "Austria: EUR", "Azerbaija: AZN", "Bahamas: BSD", "Bahrain: BHD", "Bangladesh: BDT", "Barbados: BBD", "Belarus: BYN", "Belgium: EUR", "Belize: BZD", "Benin: XOF", "Bermuda: BMD", "Bhutan: BTN", "Bolivia: BOB", "Bonaire: USD", "Bosnia and Herzegovina: BAM", "Botswana: BWP", "Brazil: BRL", "British Indian Ocean Territory : USD", "British Virgin Islands: USD", "Brunei: BND", "Bulgaria: BGN", "Burkina Faso: XOF", "Burundi: BIF", "Cabo Verde: CVE", "Cambodia: KHR", "Cameroon: XAF", "Canada: CAD", "Caribbean Netherlands: USD", "Cayman Islands: KYD", "Central African Republic: XAF", "Chad: XAF", "Chatham Islands: NZD", "Chile: CLP", "China: CNY", "Christmas Island: AUD", "Cocos (Keeling) Islands: AUD", "Colombia: COP", "Comoros: KMF", "Congo, Democratic Republic of the: CDF", "Congo, Republic of the: XAF", "Cook Islands: none", "Costa Rica: CRC", "Côte d'Ivoire: XOF", "Croatia: HRK", "Cuba: CUP", "Curacao: ANG", "Cyprus: EUR", "Czechia (Czech Republic): CZK", "Denmark: DKK", "Djibouti: DJF", "Dominica: XCD", "Dominican Republic: DOP", "Ecuador: USD", "Egypt: EGP", "El Salvador: USD", "Equatorial Guinea: XAF", "Eritrea: ERN", "Estonia: EUR", "Eswatini (fmr. <<Swaziland>>): SZL", "Falkland Islands: FKP", "Ethiopia: ETB", "Faroe Islands : none", "Fiji: FJD","Finland: EUR", "France: EUR", "French Guiana: EUR", "French Polynesia: XPF" "Gabon: XAF", "Gambia: GMD", "Georgia: GEL", "Germany: EUR", "Ghana: GHS", "Gibraltar: GIP", "Greece: EUR", "Greenland : DKK", "Grenada: XCD", "Guadeloupe: EUR", "Guam: USD", "Guernsey: GGP", "Guatemala: GTQ", "Guinea: GNF", "Guinea-Bissau: XOF", "Guyana: GYD", "Haiti: HTG", "Holy See: EUR", "Honduras: HNL", "Hong Kong: HDK", "Hungary: HUF", "Iceland: ISK", "India: INR", "Indonesia: IDR", "International Monetary Fund (IMF): XDR", "Iran: IRR", "Iraq: IQD", "Ireland: IRR", "Isle of MaN: IMP", "Israel: ILS", "Italy: EUR", "Jamaica: JMD", "Japan: JPY", "Jersey: JEP", "Jordan: JOD", "Kazakhstan: KZT", "Kenya: KES", "Kiribati: AUD", "Kosovo: EUR", "Kuwait: KWD", "Kyrgyzstan: KGS", "Laos: LAK", "Latvia: EUR", "Lebanon: LBP", "Lesotho: LSL", "Liberia: LRD", "Libya: LYD", "Liechtenstein: CHF", "Lithuania: EUR", "Luxembourg: EUR", "Macau: MOP", "Madagascar: MGA", "Malawi: MWK" , "Malaysia: MYR", "Maldives: MVR", "Mali: XOF", "Malta: EUR", "Marshall Islands: USD", "Martinique : EUR", "Mauritania: MRU", "Mauritius: MUR", "Mayotte: EUR", "Mexico: MXN", "Micronesia: USD", "Moldova: MDL", "Monaco: EUR", "Mongolia: MNT", "Montenegro: EUR", "Montserrat: XCD", "Morocco: MAD", "Mozambique: MZN", "Myanmar (formerly Burma): MMK", "Namibia: NAD", "Nauru: AUD", "Nepal: NPR", "Netherlands: EUR", "New Caledonia: XPF", "New Zealand: NZD", "Nicaragua: NIO", "Niger: XOF", "Nigeria: NGN", "Niue : NZD", "Norfolk Island: AUD", "Northern Mariana Islands: USD" "North Korea: KPW", "North Macedonia (formerly Macedonia): MKD", "Norway: NOK", "Oman: OMR", "Pakistan: PKR",
"Palau: USD", "Palestine State: ILS", "Panama: USD", "Papua New Guinea: PGK", "Paraguay: PYG", "Peru: PEN", "Philippines: PHP", "Pitcairn Islands: NZD", "Poland: PLN", "Portugal: EUR", "Puerto Rico: USD", "Qatar: QAR", "Reunion : EUR", "Romania: RON", "Russia: RUB", "Rwanda: RWF", "Saba : USD", "Saint Barthelemy : USD", "Saint Helena: SHP", "Saint Kitts and Nevis: XCD", "Saint Lucia: XCD", "Saint Martin: EUR", "Saint Pierre and Miquelon: EUR", "Saint Vincent and the Grenadines: XCD", "Samoa: WST", "San Marino: EUR", "Sao Tome and Principe: STN", "Saudi Arabia: SAR", "Senegal: XOF", "Serbia: RSD", "Seychelles: SCR", "Sierra Leone: SRR", "Singapore: SGD", "Sint Eustatius: USD", "Sint Maarten: ANG", "Slovakia: EUR", "Slovenia: EUR", "Solomon Islands: SBD", "Somalia: SOS", "South Africa: ZAR", "South Georgia Island: GBP", "South Korea: KRW", "South Sudan: SSP", "Spain: EUR", "Sri Lanka: LKR", "Sudan: SDG", "Suriname: SRD", "Svalbard and Jan Mayen: NOK", "Sweden: SEK", "Switzerland: CHF", "Syria: SYP", "Taiwan: TWD", "Tajikistan: TJS", "Tanzania: TZS", "Thailand: THB", "Timor-Leste: USD", "Togo: XOF", "Tokelau : NZD","Tonga: TOP", "Trinidad and Tobago: TTD", "Tristan da Cunha: GBP", "Tunisia: TND", "Turkey: TRY", "Turkmenistan: TMT", "Turks and Caicos Islands: USD", "Tuvalu: AUD", "Uganda: UGX", "Ukraine: UAH", "United Arab Emirates. AED", "United Kingdom: GBP", "United States of America: USD", "Uruguay: UYU", "US Virgin Islands : USD", "Uzbekistan: UZS", "Vanuatu: VUV", "Venezuela: VES", "Vietnam: VND", "Wake Island: USD", "Wallis and Futuna: XPF","Yemen: YER", "Zambia: ZMW", "Zimbabwe: USD"
]
app = tk.Tk()
ttk.Style().theme_use('xpnative')
app.title('Currency Converter')
app.geometry('1000x1000')
app.resizable(True, True)
app.config(bg = "black")

label_one = tk.Label(text = "CURRENCY CONVERTER", bg = "black", fg = "white")
label_one.config(font = ("Calibri", 15))
label_one.place(x = 200, y = 250, anchor = "center")

var = tk.StringVar(app)
var.set("FROM")

text = tk.StringVar(app)
text.set("TO")

E2 = ttk.Combobox(app, textvariable = var)
E2['values'] = OptionList
E2.config(width=90, font=('Calibri', 12, "bold"))
E2.place(x = 200, y = 300)

E3 = ttk.Combobox(app, textvariable = text)
E3['values'] = OptionList
E3.config(width=90, font=('Calibri', 12, "bold"))
E3.place(x = 200, y = 350)

L4 = tk.Label(app, text = "AMOUNT:", bg = "black", fg = "white", font= ('Calibri', 14))
L4.place(x = 100, y = 400)
E4 = tk.Entry(app, bd = 5)
E4.place(x = 200, y = 400)

#def clear_text_two(self):
#    E2.delete(0, 'end')
clear_text_two = lambda self : E2.delete(0, 'end')
clear_text_three = lambda self : E3.delete(0, 'end')
 
#def clear_text_three(self):
 #   E3.delete(0, 'end')
class curr_main:
    
    def __init__(self):
        self.apikey = "e00d40017f8b8832f6c7" 
        self.baseurl = "https://free.currconv.com/api/v7/"
    
    def countries(self):
        req = requests.get(self.baseurl + "countries?apiKey=" + self.apikey)
        return req.json()

    def currencies(self):
        req = requests.get(self.baseurl + "currencies?apiKey=" + self.apikey)
        return req.json()

    def convert(self, curr_code):
        parameter = {
        "apiKey":self.apikey,
        "compact":"ultra",
        "q": curr_code
        }
        req = requests.get(self.baseurl + "convert", params = parameter)
        if not req.status_code == 200:
            raise AssertionError
        if req.json() == {}:
            errorbox = tk.Label(text = 'No data found for the conversion, probably a wrong currency code!', font = ("Calibri", 16, "bold"))
            errorbox.place(x=300, y=500, anchor = "w")
            ebox = True
        if ebox == True & len(curr_code) == 7: errorbox.destroy()
        return req.json()[curr_code]

def funct():
    aaa = var.get()
    f = aaa[-3:]
    bbb = text.get()
    t = bbb[-3:]   
    curr_code = f + "_" + t
#    def clear_text_four(self):
#        E4.delete(0, 'end')
    clear_text_four = lambda self : E4.delete(0, 'end')

    def lab_three():
        a = E4.get()
        label = a.title()
        clear_text_four(label)
        return a
    curr_instance = curr_main()
    final_amount =  curr_instance.convert(curr_code)
    a = E4.get()
            
    fff = round(final_amount * float(a), 3)
    result = tk.Label(bg= "violet", text = (" The converted amount is " + str(fff)) + " ", font = ("Calibri", 12, "italic"))
    result.place(x = 200, y = 200, anchor= "center")

tk.Button(app, text= (' ' + 'SEND' + ' '), font = ('Calibri', 12), relief='raised', bg= "white", command = funct).place(x = 937, y = 410, anchor= "center")
app.bind('<Return>', funct)

#if keyboard.is_pressed("enter"):  this gives error
#    app.bind('<Return>', funct)

if __name__ == "__main__":
    app.mainloop()


