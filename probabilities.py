""" This file is to be run from the terminal prompt. It should be in the same
directory as the '2006-2007.regular_season','2007-2008.regular_season',
'2008-2009.regular_season' folders that contain game information. When entered
from the terminal, the probability of various queries can be returned. They can
take one of 3 forms that are displayed the the terminal. Then, league average
and particular player probabilities are calculated.

Paul Legler
"""
import csv
import os
import fileinput
import sys
import math

MADE = "made"
players = {}
basket = [25,6]
PLAYERS = ['Troy Murphy', 'Pau Gasol', 'Randy Livingston', 'Joakim Noah', 'Randy Foye', 'Donyell Marshall', 'Mike Miller', 'Kyle Lowry', 'Carlos Boozer', 'Jannero Pargo', 'Raymond Felton', 'Sean May', 'Thaddeus Young', 'Eddie Griffin', 'Billy Thomas', 'Bonzi Wells', 'Mike Taylor', 'Aaron Brooks', 'Chauncey Billups', 'Gary Payton', 'Marcin Gortat', 'Brian Cook', 'Ivan McFarlin', 'Paul Millsap', 'Joe Johnson', 'Primoz Brezec', 'Taurean Green', 'Jerome James', 'James Jones', 'Lorenzen Wright', 'Peja Stojakovic', 'Rasheed Wallace', 'Robert Hite', 'Juan Dixon', 'Caron Butler', 'Sean Singletary', 'Marc Gasol', 'Joey Graham', 'Tony Parker', 'Derek Anderson', 'Robert Swift', 'LeBron James', 'Brook Lopez', 'Jerry Stackhouse', 'D.J. Augustin', 'Zach Randolph', 'Nazr Mohammed', 'Nicolas Batum', 'Luke Ridnour', 'David Wesley', 'Malik Rose', 'Pat Burke', 'Devin Brown', 'Delonte West', 'Yao Ming', 'Johan Petro', 'Antoine Wright', 'Jason Williams', 'Mario Chalmers', 'Sasha Vujacic', 'Rafael Araujo', 'Reggie Evans', 'Tyronn Lue', 'Scott Padgett', 'Kareem Rush', 'Pat Garrity', 'DeSagana Diop', 'Cuttino Mobley', 'Kelenna Azubuike', 'Al Horford', 'Alexander Johnson', 'Mickael Gelabale', 'Robin Lopez', 'Chris Mihm', 'Rawle Marshall', 'Juan Carlos Navarro', 'Jawad Williams', 'Amir Johnson', 'Joe Smith', 'James Posey', 'Greg Oden', 'Dorell Wright', 'Andre Brown', 'Chris Kaman', 'Ersan Ilyasova', 'O.J. Mayo', 'Mike Sweetney', 'Jose Barea', 'Yakhouba Diawara', 'Julian Wright', 'John Lucas', 'Sean Marks', 'Marquis Daniels', 'Brandon Rush', 'Manu Ginobili', 'Josh Powell', 'Kevin Love', 'Antawn Jamison', 'Kevin Garnett', 'Leandro Barbosa', 'Courtney Lee', 'Luol Deng', 'Bobby Jones', 'Jarvis Hayes', 'Rudy Fernandez', 'Zaza Pachulia', 'Josh Smith', 'Eric Williams', 'Ronald Dupree', 'Kenny Thomas', 'Jason Terry', 'Bernard Robinson', 'Jamal Crawford', 'Julius Hodge', 'Allen Iverson', 'Pops Mensah-Bonsu', 'David Noel', 'Walter Sharpe', 'Zydrunas Ilgauskas', 'Sergio Rodriguez', 'Kobe Bryant', 'Daniel Ewing', 'DeMarcus Nelson', 'Rodney Carney', 'Jackie Butler', 'Mark Blount', 'DeAndre Jordan', 'Anthony Johnson', "Jermaine O'Neal", 'Lance Allred', 'Hakim Warrick', 'Chris Wilcox', 'Antonio Daniels', 'Matt Freije', 'James White', 'Darius Miles', 'Darnell Jackson', 'David Lee', 'Kevin Martin', 'J.J. Hickson', 'Marcus Williams', 'Kris Humphries', 'Sarunas Jasikevicius', 'Keith Langford', 'Jason Richardson', 'Michael Olowokandi', 'David West', 'Kyrylo Fesenko', 'Loren Woods', 'Rajon Rondo', 'Jelani McCoy', 'Mike Hall', 'Carlos Delfino', 'LaMarcus Aldridge', 'Bobby Simmons', 'Rodney Stuckey', 'Rashad McCants', 'Beno Udrih', 'Chris Paul', 'Ricky Davis', 'Jamal Sampson', 'Jake Tsakalidis', 'Jason Kapono', 'Cedric Simmons', 'Fred Jones', 'Sasha Pavlovic', 'Raja Bell', 'Mike Conley', 'Shane Battier', 'P.J. Tucker', 'Anthony Tolliver', 'Luke Jackson', 'Hassan Adams', 'Alan Anderson', 'Erick Dampier', 'Robert Horry', 'Kevinn Pinkney', 'Samuel Dalembert', 'Kirk Hinrich', 'Adrian Griffin', 'Shavlik Randolph', 'Trevor Ariza', 'Linton Johnson', 'Tarance Kinsey', 'Monta Ellis', 'Vassilis Spanoulis', 'Kyle Weaver', 'Jamaal Tinsley', 'Othello Hunter', 'Jeff Green', 'Al Thornton', 'Roy Hibbert', 'Nathan Jawai', 'Javaris Crittenton', 'Nenad Krstic', 'Tony Allen', 'Ben Wallace', 'Daequan Cook', 'Goran Dragic', 'Doug Christie', 'Kevin Durant', 'Stephane Lasme', 'D.J. Strawberry', 'Danilo Gallinari', 'Sebastian Telfair', 'Von Wafer', 'JaVale McGee', 'Luke Schenscher', 'Marco Belinelli', 'Shannon Brown', 'Melvin Ely', 'Chris Quinn', 'Corey Brewer', 'Mike Harris', 'Jason Kidd', 'Eddie Gill', 'Darrell Arthur', 'Scot Pollard', 'Michael Finley', 'Alando Tucker', 'Nene Hilario', 'Jarron Collins', 'Eduardo Najera', 'Ron Artest', 'Thomas Gardner', 'Morris Peterson', 'Jordan Farmar', 'Calvin Booth', 'Ira Newble', 'Jamario Moon', 'Earl Barron', 'Steven Smith', 'Shaun Livingston', 'Austin Croshere', 'Ronald Murray', 'Vince Carter', 'Smush Parker', 'Andres Nocioni', 'Sonny Weems', 'Sam Cassell', 'Rasual Butler', 'Vitaly Potapenko', 'Roger Powell', 'Nick Young', 'Jacque Vaughn', 'Luther Head', 'Brian Cardinal', 'Kosta Koufos', 'Eddie Jones', 'Damon Stoudamire', 'Bostjan Nachbar', 'Dan Gadzuric', 'Devean George', 'Dajuan Wagner', 'Ryan Bowen', 'Anderson Varejao', 'Brian Scalabrine', 'Jamaal Magloire', 'J.J. Redick', 'Eddie House', 'Morris Almond', 'Michael Sweetney', 'Yaroslav Korolev', 'P.J. Brown', 'Emeka Okafor', "Patrick O'Bryant", 'David Harrison', 'Jameer Nelson', 'Willie Green', 'Will Solomon', 'Donte Greene', 'Deron Williams', 'Esteban Batista', 'Brandon Roy', 'Mo Williams', 'Baron Davis', 'Pape Sow', 'Steve Blake', 'Allan Ray', 'Udonis Haslem', 'Keith Bogans', 'Daniel Gibson', 'Amare Stoudemire', 'Joe Alexander', 'Martell Webster', 'Chris Webber', 'Kevin Willis', 'Aaron Williams', 'John Salmons', 'Linas Kleiza', 'Stromile Swift', 'Kevin Ollie', 'Theo Ratliff', 'Fabricio Oberto', 'Dominic McGuire', 'Dijon Thompson', 'Travis Diener', 'Marcus Vinicius', 'Paul Pierce', 'Mike James', 'Jason Hart', 'Mark Madsen', 'Tim Thomas', 'James Lang', 'Chris McCray', 'Dee Brown', 'Chris Richard', 'Richard Hamilton', 'Jason Collins', 'Brad Miller', 'Bobby Jackson', 'Bo Outlaw', 'Jeff Foster', 'Marcus Camby', 'Eric Snow', 'Joel Anthony', 'Darrick Martin', 'Adam Morrison', 'Kwame Brown', 'Steve Nash', 'Louis Williams', 'Quinton Ross', 'Cedric Bozeman', 'Tracy McGrady', 'Lamar Odom', 'Solomon Jones', 'Al Harrington', "Shaquille O'Neal", 'Gordan Giricek', 'Mike Wilks', 'Carmelo Anthony', 'Josh Howard', 'Gerald Wallace', 'Danny Fortson', 'Spencer Hawes', 'Jeremy Richardson', 'Chuck Hayes', 'Orien Greene', 'Thabo Sefolosha', 'Kyle Korver', 'Randolph Morris', 'Roko Ukic', 'Darryl Watkins', 'Othella Harrington', 'Brandon Bass', 'Nick Collison', 'Jumaine Jones', 'Wilson Chandler', 'Derek Fisher', 'Steven Hill', 'Jose Calderon', 'D.J. White', 'Josh McRoberts', 'Donell Taylor', 'DJ Mbenga', 'Uros Slokar', 'Damien Wilkins', 'Speedy Claxton', 'Hawes', 'Clifford Robinson', 'Tyrus Thomas', 'Mouhamed Sene', 'Anthony Morrow', 'Tony Battie', 'Richie Frahm', 'Mike Bibby', 'Grant Hill', 'C.J. Watson', 'Wally Szczerbiak', 'Ramon Sessions', 'Joe Crawford', 'Slava Medvedenko', 'Brevin Knight', 'Rudy Gay', 'Awvee Storey', 'Desmond Mason', 'Josh Childress', 'Jarrett Jack', 'Adonal Foyle', 'Marko Jaric', 'Josh Boone', 'Drew Gooden', 'Dwyane Wade', 'Steven Hunter', 'Nick Fazekas', 'Brian Skinner', 'Juwan Howard', 'Will Bynum', 'Dikembe Mutombo', 'Keith McLeod', 'Ronnie Price', 'Shawn Marion', 'Renaldo Balkman', 'Mike Dunleavy', 'Gabe Pruitt', 'Etan Thomas', 'Hedo Turkoglu', 'Carlos Arroyo', 'Rashard Lewis', 'Kirk Snyder', 'Travis Outlaw', 'Stanislav Medvedenko', 'Damon Jones', 'Troy Hudson', 'Marcus Banks', 'Jason Maxiell', 'Anthony Parker', 'Hilton Armstrong', 'Kasib Powell', 'Luc Richard Mbah a Moute', 'Acie Law IV', 'Casey Jacobsen', 'Brandan Wright', 'Steve Novak', 'Marvin Williams', 'Dwayne Jones', 'Yi Jianlian', 'Ronnie Brewer', 'Marc Jackson', 'Cartier Martin', 'Keyon Dooling', 'Aaron Gray', 'Darius Washington', 'Ray Allen', 'Mile Ilic', 'Antonio McDyess', 'Courtney Sims', 'Michael Redd', 'Ronny Turiaf', 'Eddy Curry', 'Yue Sun', 'Jared Jeffries', 'Salim Stoudamire', 'DerMarr Johnson', 'Alvin Williams', 'Michael Beasley', 'Kaniel Dickens', 'Charlie Villanueva', 'Marreese Speights', 'Gilbert Arenas', 'Quincy Douby', 'Junior Harrington', 'Alonzo Mourning', 'Kelvin Cato', 'Walter Herrmann', 'Will Conroy', 'J.R. Smith', 'Lou Williams', 'Eric Gordon', 'Boris Diaw', 'Kosta Perovic', 'Dan Dickau', 'Matt Bonner', 'Ian Mahinmi', 'Anfernee Hardaway', 'Lawrence Roberts', 'Rasho Nesterovic', 'Maurice Taylor', 'Russell Westbrook', 'James Singleton', 'Lindsey Hunter', 'Dirk Nowitzki', 'Luc Mbah a Moute', 'Bracey Wright', 'Will Blalock', 'Glen Davis', 'Viktor Khryapa', 'Dontell Jefferson', 'Tim Duncan', 'Mickael Pietrus', 'Matt Barnes', 'Earl Watson', 'Malik Hairston', 'Dahntay Jones', 'Dale Davis', 'Sean Williams', 'Acie Law', 'Eric Piatkowski', 'Justin Williams', 'Ryan Anderson', 'Mardy Collins', 'Leon Powe', 'Ruben Patterson', 'DeShawn Stevenson', 'Sun Yue', 'Bill Walker', 'Stephen Graham', 'Tyson Chandler', 'Ime Udoka', 'Rafer Alston', 'Jerryd Bayless', 'Richard Jefferson', 'Malik Allen', 'Shawne Williams', 'Jeff McInnis', 'Andre Barrett', 'Joey Dorsey', 'Maurice Evans', 'C.J. Miles', 'Ike Diogu', 'Carl Landry', 'Antoine Walker', 'Cheikh Samb', 'Jason Thompson', 'Andris Biedrins', 'Andre Miller', 'Jalen Rose', 'Royal Ivey', 'Mikki Moore', 'Louis Amundson', 'Tayshaun Prince', 'Lynn Greer', 'Luke Walton', 'Michael Doleac', 'Mario West', 'Bruce Bowen', 'Francisco Garcia', 'Demetris Nichols', 'Trenton Hassell', 'Andrea Bargnani', 'Arron Afflalo', 'Chucky Atkins', 'Andray Blatche', 'James Augustine', 'Kendrick Perkins', 'Bobby Brown', 'Derrick Rose', 'Brendan Haywood', 'Stephen Jackson', 'Andreas Glyniadakis', 'Guillermo Diaz', 'Corey Maggette', 'Luis Scola', 'Kurt Thomas', 'Jorge Garbajosa', 'Jake Voskuhl', 'Mehmet Okur', 'Anthony Randolph', 'Kenyon Martin', 'Al Jefferson', 'Corliss Williamson', 'Shelden Williams', 'Channing Frye', 'Hamed Haddadi', 'Francisco Elson', 'Devin Harris', 'Ben Gordon', 'Darrell Armstrong', 'Charlie Bell', 'Maceo Baston', 'Oleksiy Pecherov', 'Ryan Gomes', 'Andre Iguodala', 'Shareef Abdur-Rahim', 'Chris Duhon', 'Desmon Farmer', 'Danny Granger', 'Aaron McKie', 'Elton Brand', 'Roger Mason', 'Vladimir Radmanovic', 'Tarence Kinsey', 'Alex Acker', 'Jared Reiner', 'Jared Dudley', 'Craig Smith', 'Rob Kurz', 'Maurice Ager', 'Greg Buckner', 'Brent Barry', 'Trey Johnson', 'Blake Ahearn', 'Coby Karl', 'Jason Smith', 'Anthony Carter', 'Anthony Roberson', 'Mike Conley Jr.', 'Ryan Hollins', 'J.R. Giddens', 'Dwight Howard', 'Shammond Williams', 'Justin Reed', 'Jermareo Davidson', 'Wayne Simien', 'Matt Carroll', 'Steve Francis', 'Chris Bosh', 'Darko Milicic', 'Chris Andersen', 'Joel Przybilla', 'Jose Juan Barea', 'Gerald Green', 'Chris Douglas-Roberts', 'Nate Robinson', 'Darius Songaila', 'Stephon Marbury', 'Michael Ruffin', 'Cheick Samb', 'Andrew Bogut', 'Damir Markota', 'Earl Boykins', 'George Hill', 'Raef LaFrentz', 'Andre Owens', 'Larry Hughes', 'D.J. Mbenga', 'Andrew Bynum', 'Paul Davis', 'Alan Henderson', 'Alexis Ajinca', 'Andrei Kirilenko', 'Quentin Richardson', 'Matt Harpring', 'T.J. Ford']
TYPES = ['driving hook', 'step back jump', 'running tip', 'turnaround hook', 'driving dunk', 'jump', 'hook', 'running finger roll', 'jump bank', 'running hook', 'running tip-in', 'alley oop dunk', 'driving bank', 'fade away jumper', 'turnaround fade away', 'driving reverse layup', 'de souza jump', 'turnaround bank', 'driving finger roll', 'tip', 'running finger roll layup', 'putback layup', 'putback reverse dunk', 'turnaround bank hook', 'pullup jump', 'running slam dunk', 'running dunk', 'turnaround finger roll', 'dunk', 'running bank', '3pt', 'alley oop layup', 'hook bank', 'turnaround jump', 'putback dunk', 'de souza driving layup', 'layup', 'putback slam dunk', 'pullup bank', 'slam dunk', 'running layup', 'driving jump', 'jump hook', 'driving layup', 'reverse layup', 'driving slam dunk', 'running reverse layup', 'follow up dunk', 'fade away', 'driving bank hook', 'floating jump', 'finger roll layup', 'reverse dunk', 'finger roll', 'running jump', 'jump bank hook', 'running 3pt', 'running finger', 'tip-in', 'driving finger roll layup', 'running bank hook', 'alley oop layup shot', 'fade away bank', 'reverse slam dunk']
RANGES = {"inside":(0,3), "close":(3,8), "shortmid":(8,15), "longmid":(15,23), "close3":(23,28), "deep3":(28,35), "chuck":(35,100)}
dist_probability = {} # maps each Distance Range to a probability
type_probability = {} # maps each Shot Type to a probability
player_probability = {} # maps a player to a map of each Distance Range to a probability and a map of each Shot Type to a probability
dist_data = {dist:[0,0] for dist in RANGES.keys()}
type_data = {t:[0,0] for t in TYPES}
player_data = {p:[{dist:[0,0] for dist in RANGES.keys()},{t:[0,0] for t in TYPES}] for p in PLAYERS} #first is for distance, second for type


# Examine one file at a time - recording important information and updating probability tables
def examine(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[13] == 'shot':
                shooter, result, shot, x, y = row[23], int(MADE == row[27]), row[29], row[30], row[31]
                if x == "" or y == "":
                    x, y = 25, 6
                else:
                    x, y = int(x), int(y)
                update_type_data(shot, result)
                update_dist_data(x, y, result)
                update_player_data(shooter, shot, result, x, y)
                if shooter in players:
                    players[shooter].append([result, x, y])
                else:
                    players[shooter] = [[result, x, y]]

# For each player - we keep track of the distance and type
def update_player_data(shooter, shot, result, x, y):
    # For the distance of each shot tracked by player
    distance = calcDistance(x, y)
    dist = getRange(distance)
    makes, total = player_data[shooter][0][dist]
    player_data[shooter][0][dist] = [makes + result, total + 1]
    # The type of each shot tracked by splayer
    makes, total = player_data[shooter][1][shot]
    player_data[shooter][1][shot] = [makes + result, total + 1]

# We keep a probability table that maps from the distance of the shot grouped
# into a number of different catagories
def update_dist_data(x, y, result):
    distance = calcDistance(x, y)
    dist = getRange(distance)
    makes, total = dist_data[dist]
    dist_data[dist] = [makes + result, total + 1]

# We keep a probability table that maps from the type of shot grouped into the
# given catagories
def update_type_data(shot, result):
    makes, total = type_data[shot]
    type_data[shot] = [makes + result, total + 1]

# Calculating the distance from (x,y) to the basket
def calcDistance(x, y):
    locs = [x - basket[0], y - basket[1]]
    distance = math.pow(math.pow(locs[0],2) + math.pow(locs[1],2), .5)
    return distance

# Find which range a distance from the basket is
def getRange(distance):
    for dist, range_ in RANGES.items():
        if distance >= range_[0] and distance < range_[1]:
            return dist
    return 'close'

# Get the probability of a particular shot going in from a particular player
# and the league wide average
def getProbability(shooter, shot, x="all", y="all"):
    # If the type of input is Player,Shot Type,X,Y
    if x != None:
        type_prob = type_probability[shot]
        player_type_prob = player_probability[shooter][1][shot]
        x, y = int(x), int(year)
        distance = calcDistance(x,y)
        dist = getRange(distance)
        dist_prob = dist_probability[dist]
        player_dist_prob = player_probability[shooter][0][dist]
        league_prob = .5*dist_prob + .5*type_prob
        player_prob = 'unknown'
        if player_dist_prob != "no shots":
            if player_type_prob != "no shots":
                player_prob = .5*player_dist_prob + .5*player_type_prob
            player_prob = player_dist_prob
        elif player_type_prob != "no shots":
            player_prob = player_type_prob
    # If the type of input is Player,Distance Range
    elif shot in RANGES.keys():
        player_prob = 'unknown'
        if player_probability[shooter][0][shot]:
            player_prob = player_probability[shooter][0][shot]
        league_prob = dist_probability[shot]
    # If the type of input is Player,Shot Type
    else:
        player_prob = 'unknown'
        if player_probability[shooter][1][shot] != "no shots":
            player_prob = player_probability[shooter][1][shot]
        league_prob = type_probability[shot]
    return [league_prob, player_prob]

# All available input folders with games inside them
folders =['2006-2007.regular_season','2007-2008.regular_season', '2008-2009.regular_season']

# Figuring out the end of the data range
print("Input the last year you would like to consider beginning at 2006")
year = int(sys.stdin.readline())
print("Calculating...")

# Go through every filename and examine it
for i in range(len(folders)):
    if i+2006 <= year:
        for filename in os.listdir(folders[i]):
            if filename != '.DS_Store':
                examine(folders[i] + "/" + filename)

# Calculating league wide probabilit tables
for d in dist_data:
    if dist_data[d][1]:
        dist_probability[d] =  1.0*dist_data[d][0]/dist_data[d][1]
for t in type_data:
    if type_data[t][1]:
        type_probability[t] =  1.0*type_data[t][0]/type_data[t][1]

# Calculating individual player probability tables
for p in player_data:
    player_probability[p] = [{},{}]
    for d in player_data[p][0]:
        if player_data[p][0][d][1]:
            player_probability[p][0][d] =  1.0*player_data[p][0][d][0]/player_data[p][0][d][1]
        else:
            player_probability[p][0][d] = 'no shots'
    for t in player_data[p][1]:
        if player_data[p][1][t][1]:
            player_probability[p][1][t] =  1.0*player_data[p][1][t][0]/player_data[p][1][t][1]
        else:
            player_probability[p][1][t] = 'no shots'

# Run in terminal - takes user input
print("Basket located at (25,6)\nShot Types:" + str(TYPES)+ "\nDistance Ranges: "+ str(RANGES.keys())+"\nFormat options as follows (no spaces):\nPlayer,Shot Type,X,Y\nPlayer,Shot Type\nPlayer,Distance Range")
while True:
    command = sys.stdin.readline()
    spl = command.split(",")
    # For different types of inputs
    if len(spl) == 4:
        shooter, shot, x, y = spl
    else:
        spl.append(None)
        spl.append(None)
        shooter, shot, x, y = spl
    if y:
        y = y[0:len(shot)-1]
    else:
        shot = shot[0:len(shot)-1]
    lw, ply = getProbability(shooter, shot, x, y) #league wide and player probabilities
    print("League Wide Probability: " + str(lw) + ", Individual Probability: " + str(ply))
