import os;

link = "http://promo.na.leagueoflegends.com/sru-map-assets/6/"

column = 0;
rc_column = 0;
while (rc_column == 0):
	row = 0;
	rc_column = os.system('wget ' + link + str(column) + '/' + str(row) + '.png -O ' + str(1000 + column) + '-' + str(1000 + row) + '.png')
	rc_row = rc_column
	while (rc_row == 0):
		row += 1
		rc_row = os.system('wget ' + link + str(column) + '/' + str(row) + '.png -O ' + str(1000 + column) + '-' + str(1000 + row) + '.png')

	column += 1
	
p = os.popen('ls -1 *.png | tail -n2');
second_last_file = p.readline();
last_file = p.readline();

column_end = last_file[0:4]
row_end = second_last_file[5:9]

print column_end
print row_end

os.system('rm ' + column_end + '*');
os.system('rm *-' + row_end + '.png');

column_end = int(column_end) - 1000;
row_end = int(row_end) - 1000;

os.system('mkdir temp')

i = 0;
for r in range(0, row_end):
	for c in range(0, column_end):
		file_to_move = str(1000 + c) + '-' + str(1000 + row_end - r - 1) + '.png'
		os.system('cp ' + file_to_move + ' ./temp/' + str(100000 + i) + '.png');
		i += 1
		
os.system('montage ./temp/*.png -tile ' + str(column_end) + 'x' + str(row_end) + ' -geometry +0+0 result.png');
os.system('montage ./temp/*.png -tile ' + str(column_end) + 'x' + str(row_end) + ' -geometry +0+0 result.jpg');
os.system('rm temp -r');
os.system('rm 1*.png');
