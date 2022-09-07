from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.bill import Bill, Roommate
from flatmates_bill.pdf import PdfReport

app = Flask(__name__)  # flask object


# Home page HTML
class HomePage(MethodView):
    def get(self):
        return render_template("index.html")


# Bill form page HTML
class BillFormPage(MethodView):
    def get(self):
        bill_form_object = BillForm()  # instantiate BillForm() Object we created to ask user input
        return render_template("bill_form_page.html", bill_form=bill_form_object)  # return html page and apply
        # BillForm() object


# result page
class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)  # instantiate the BillForm() Object to retrieve users input

        amount = bill_form.amount.data  # retrieve amount
        period = bill_form.period.data  # retrieve date
        new_bill = Bill(amount=float(amount), period=period)  # instantiate Bill() object

        name_1 = bill_form.roommate_one_name.data  # retrieve first roommate name
        days_1 = bill_form.roommate_one_days.data  # retrieve first roommate days
        name_2 = bill_form.roommate_two_name.data  # retrieve second roommate name
        days_2 = bill_form.roommate_two_days.data  # retrieve second roommate days
        roommate_1 = Roommate(name=name_1, days_in_house=int(days_1))  # instantiate Roommate #1
        roommate_2 = Roommate(name=name_2, days_in_house=int(days_2))  # instantiate Roommate #2

        pdf = PdfReport(f"{period}_bill.pdf")  # create PDF by passing file path
        pdf.generate(roommate_one=roommate_1, roommate_two=roommate_2, bill=new_bill)
        return render_template("results.html", name1=roommate_1.name, pay1=roommate_1.pay_rate(new_bill, roommate_2),
                               name2=roommate_2.name, pay2=roommate_2.pay_rate(new_bill, roommate_1),
                               date1=roommate_1.days_in_house, date2=roommate_2.days_in_house)


# f"Bill Amount: {amount} period: {period}\n {name_1} must pay {roommate_1.pay_rate(new_bill, roommate_2)}\n {name_2}
# must pay {roommate_2.pay_rate(new_bill, roommate_1)}" Form for billing input and retrieval
class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    roommate_one_name = StringField("Name: ")
    roommate_one_days = StringField("Day's in the house: ")
    roommate_two_name = StringField("Name: ")
    roommate_two_days = StringField("Day's in the house: ")
    button_calculate = SubmitField("Calculate")


app.add_url_rule("/", view_func=HomePage.as_view("home_page"))
app.add_url_rule("/bill", view_func=BillFormPage.as_view("bill_form_page"))
app.add_url_rule("/results", view_func=ResultsPage.as_view("results_page"))

app.run(debug=True)
