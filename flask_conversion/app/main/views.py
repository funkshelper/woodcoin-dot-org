from flask import render_template, send_file, url_for, Blueprint, redirect, request



main_blueprint = Blueprint('main', __name__,)

@main_blueprint.route('/', methods=['GET', 'POST'])
def home():
	title = "Sustainable. Digital. Cash."
	return render_template('index.html', title=title)

@main_blueprint.route('/faq', methods=['GET', 'POST'])
def faq():
	title = "Frequently Asked Questions"
	return render_template('faq.html', title=title)

@main_blueprint.route('/specs', methods=['GET', 'POST'])
def specs():
	title = "Specifications"
	return render_template('specs.html', title=title)

@main_blueprint.route('/downloads', methods=['GET', 'POST'])
def downloads():
	title = "Downloads"
	return render_template('downloads.html', title=title)

@main_blueprint.route('/merchants', methods=['GET', 'POST'])
def merchants():
	title = "Merchant Directory"
	return render_template('merchants.html', title=title)

@main_blueprint.route('/extras', methods=['GET', 'POST'])
def extras():
	title = "Extra Stuff"
	return render_template('extras.html', title=title)

@main_blueprint.route('/logic.phm', methods=['GET', 'POST'])
def logic():
	title = "OpenTTD Scenario"
	return render_template('logic.phm.html', title=title)

@main_blueprint.route('/bounties', methods=['GET', 'POST'])
def bounties():
	title = "Help the Forest, Earn LOGs"
	return render_template('bounties.html', title=title)



@main_blueprint.route('/woodcoin.pdf/', )
def woodcoin():
    
    return send_file('/home/robert/woodcoin.org/app/static/woodcoin.pdf', attachment_filename='woocoin.pdf')

