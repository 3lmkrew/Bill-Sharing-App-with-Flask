# This is the PDF class and FileSharer classes (OOP)

import webbrowser
import fpdf
import os
from filestack import Client


class PdfReport:
    """
    Object that contains roommate one object, roommate two object and the bill
    it will generate a PDF bill based on roommates days stay in house and total bill amount
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, roommate_one, roommate_two, bill):
        pdf = fpdf.FPDF()
        pdf.add_page()
        pdf.set_font(family='Arial', style='B', size=24)
        pdf.image(name="flatmates_bill/files/house.png", w=50, h=50, x=85)
        pdf.cell(w=0, h=40, txt="Roommate's Electricity Bill", align="C", ln=1)
        pdf.set_font(family='Times', style='B', size=18)
        pdf.cell(w=170, h=20, txt=f"Period:  {bill.period}", align="R", ln=1)
        pdf.set_text_color(r=255, g=0, b=0)
        pdf.cell(w=185, h=20, txt=f"Total Amount Due: ${bill.amount}", align="R", ln=1)
        pdf.set_text_color(r=0, g=0, b=0)
        pdf.set_font(family='Arial', size=14)
        pdf.cell(w=50, h=30, txt=f"{roommate_one.name} must pay ${roommate_one.pay_rate(bill, roommate_two)} "
                                 f"for {roommate_one.days_in_house} days in the house.", ln=1)

        pdf.cell(w=50, h=20, txt=f"{roommate_two.name} must pay ${roommate_two.pay_rate(bill, roommate_one)} "
                                 f"for {roommate_two.days_in_house} days in the house")
        #pdf.cell(w=50, h=30, txt=f"formula is as follows: Total Days in the month + plus a single roommate amount of days spent in the house, then you divide the answer by total days in month and multiplay by bill amount to get the answer")
        os.chdir("flatmates_bill/files")
        pdf.output(self.file_name)
        webbrowser.open(self.file_name)


class FileSharer:
    """
    Object must pass file name and API key.
    will create a URL link.
    """

    def __init__(self, file_name, api_key):
        self.API_key = api_key
        self.file_name = file_name

    def Create_link(self):
        client = Client(self.API_key)
        new_filelink = client.upload(filepath=self.file_name)
        return new_filelink.url
