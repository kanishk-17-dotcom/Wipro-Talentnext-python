                                  # MINI PROJECTS

""" 
1. 
Your friend has sent you a text file containing n lines. He sent a secret message with it, which tells
you the place and time where you have to go and meet him.He challenges you to find it out without seeing 
the content of the file. He has given hints to find it. Let's surprise him by breaking the challenge with 
our python code.

Hints to find the secret message: 

1.The number of lines in the file tells you the meeting time.
Note: 1<= number of lines <= 24
If the number of lines is exceeding 12, you need to convert it to 12 hour format. 
For example:
1. If the number of lines is 15, then the meeting time is 3 PM. 
2. If the number of lines is10, then the meeting time is 10 AM.

2.The word appearing for the maximum number of times tells you the meeting place.
Note:Meeting place will be a street name.
For example:
1. If the word Oxfordappears for the maximum number of times, then meeting place is Oxford Street.
2. If the word Parkappears for the maximum number of times, then meeting place is Park Street. 

Sample input 1:
Sample.txt
Cricket a bat-and-ball park game  played  between  two  teams  of  eleven park 
players on a field at the park center of which is a 20-metre (22-yard) pitch with 
a wicket at each end, each park comprising two bails balanced on three stumps. 
The batting park scores runs by striking the ball bowled at the park wicket with 
the park bat, while the bowling and park fielding side tries to prevent this and 
dismiss each park player  (so  they  are  "out").  Means  of park include being 
bowled, when the ball hits the park and dislodges the bails, and by the fielding 
side park the ball after it is hit by the bat, but before it hits the park. When ten 
parkhave been dismissed, the innings ends and the teams park roles.

Sample output 1:
Meeting time: 9 AM 
Meeting place: Park Street
Explanation: Number of lines is 9. The word park appears for the maximum of 15 times.

Sample input 2:
Sample.txt
Royal  Enfield  is  an  Indian Apollo motorcycle  manufacturing  brand  with  tag  of 
"oldest Apollo motorcycle  brand  in  continuous  production"  manufactured 
Apollo factories ChennaiApolloIndia. Licensed from Royal Enfield by indigenous 
Indian Madras Motors, it is now a Apollo subsidiary Eicher Motors Limited, an 
Indian Apollo automaker. The company makes Apollo Royal Enfield Bullet, and 
other  single-cylinder  and  twin-cylinder Apollo motorcycles. First  produced 
Apolloin  1901,  Royal  Enfield is oldest  motorcycle Apollo brand  world  still
production, with Bullet model enjoying longest motorcycle Apollo production 
run of all time.In 1990, Royal Enfield collaborated with Eicher Apollo Group, an 
automotive company Apollo India,and merged with it 1994.Apart from bikes, 
Eicher Apollo Group is involved in the production and sales Apollo commercial 
vehicles  and  automotive  gears.  Although Apollo Royal  Enfield  experienced 
difficulties 1990s,  and  ceased Apollo motorcycle  production  at  their  Jaipur 
factory 2002, by 2013 Apollo company opened a  new primary Apollo factory 
Apollo Chennai suburb  of  Oragadam  on strength  of  increased  demand  for  its 
Apollo motorcycles. This was followed in Apollo 2017 by inauguration another 
new  factory  of  a  similar  size  to facility  at Apollo Oragadam  (capacity  600,000 
vehicles  per  year)  at  Vallam Apollo Vagadal.  The  original  factory  at Apollo 
Tiruvottiyur  became  secondary,  and  continues  to  produce  some  limited-run 
motorcycle models.

Sample output 2:
Meeting time: 8 PM
Meeting place: Apollo Street
Explanation: Number of lines is 20 and converting it to 12 hour format we get 8 PM. The word Apollo 
appears for the maximum of 25 times.
"""

from collections import Counter

def find_meeting_details(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    num_lines = len(lines)
    if num_lines <= 12:
        time = f"{num_lines} AM"
    else:
        time = f"{num_lines % 12 or 12} PM"
    words = []
    for line in lines:
        words.extend(line.strip().split())
    word_freq = Counter(words)
    most_common_word, _ = word_freq.most_common(1)[0]
    meeting_place = f"{most_common_word} Street"
    print(f"Meeting time: {time}")
    print(f"Meeting place: {meeting_place}")

find_meeting_details("sample.txt")
