lineArray = []

for line in open('C:\\Users\\MaxShaps\\Desktop\\Written Documents\\Times Through The Order Penalty\\First Time Through Hitting Results\\2012 (Partitioned)\\2012 FTT Hitting Events_1.csv'):
    lineArray.append(line != '\n')

print lineArray
