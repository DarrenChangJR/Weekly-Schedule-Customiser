from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser(description='Stay organised. Stay nerdy. Prettily.', epilog='Created by darrenjr')
parser.add_argument('-f', '--font', metavar='', help='Type of text font', default='sans-serif')
parser.add_argument('-b', '--background', metavar='', help='Colour of background', default='#666666')
parser.add_argument('-t', '--table', metavar='', help='Colour of headers and table cells', default='#009879')
args = parser.parse_args()

# opening the downloaded SA_LEARNER_SERVICES.SSR_SSENRL_SCHD_W.html
with open('SA_LEARNER_SERVICES.SSR_SSENRL_SCHD_W.html') as frame:
	soup = BeautifulSoup(frame, 'html.parser')
	table = soup.find('table', 'PSLEVEL1GRIDWBO')
	table.find(class_='PSLEVEL1GRIDLABEL').parent.replace_with('')



def customise_css():

	# changing background colour
	table['style'] = f'background-color: {args.background};'


	# changing table colour
	for i in table.find_all('td', style='color:rgb(0,0,0);background-color:rgb(182,209,146);text-align: center;'):
		i.span['class'], i.span['style'] = 'MAINREASON', f'background-color: {args.table}; font-family: {args.font};'
		i['class'], i['style'] = 'MAINREASON_BG', f'background-color: {args.table};'
	for i in table.find_all('th'):
		i['style'] = f'background-color: {args.table}; font-family: {args.font};'
		# removing days of the week
		i.string = i.contents[0]

customise_css()

html_header = '''<head><style>
.PSLEVEL1GRIDWBO {
    border-collapse: collapse;
    font-size: 0.9em;
    margin: 0 auto;
    transform: rotate(90deg);
    transform-origin:bottom left;
    position:absolute;
    top: -100vw;
    left: 0;
    height:100vw;
    width:100vh;
    overflow:auto;
}

.PSLEVEL1GRIDWBO tbody tr th, .MAINREASON {
    color: #ffffff;
    text-align: center;
}

.PSLEVEL1GRIDWBO tbody tr td {
    text-align: center;
    border: 1px solid #dddddd;
}

.MAINREASON {
    font-size: 0.9em;
    font-family: sans-serif;
}

.MAINREASON_BG {
    padding-top: 20px;
    padding-bottom: 20px;
}
</style></head>
'''

with open('your_very_own_schedule.html', 'w') as new_file:
	new_file.write(html_header + str(table))