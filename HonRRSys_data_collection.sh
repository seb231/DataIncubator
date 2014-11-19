#!/bin/sh
#$ -cwd                 # use current working directory
#$ -V                   # this makes it verbose
#$ -j y                 # and put all output (inc errors) into it
#$ -l h_rt=240:0:0       # Request 140 hour runtime (upto 240 hours)
#$ -l h_vmem=1G 
#$ -pe smp 1

# generate 100000 'random' 17 digit numbers up until 100000
touch random.numbers;
while [[ $(cat random.numbers | wc -l) -le 100000 ]]; 
do 
tr -dc '0-9' </dev/urandom |  head -c 17 | sed -e 's/$/\n/g' >> random.numbers; 
done;

# write a script for each random number/steam profile to collect games webpage data
for f in random.numbers; 
do 
sed -e 's/^/wget http:\/\/steamcommunity\.com\/profiles\//g' -e 's/$/\/games\/?tab=all/g' $f >> collect_steam_data.sh; 
done;

# insert sleep timer in between data recovery
#for f in collect_steam_data.sh; 
#do 
#sed -i 's/$/\nsleep 2s/g' $f; 
#done;

sh collect_steam_data.sh;

# check index.html output from wget, files with "Sorry!" are deleted as they contain no game info
# for files with game data parse gamer tag as name of file to store data on game name and hours played in .info file
for f in index.html*; 
do 
if grep -q 'Sorry!' $f; 
then 
pass; 
elif grep -q 'rgGames' $f;
then
gamer_tag=$(grep "<title>Steam Community ::" $f | cut -f4 -d ' ' | sed -e 's/$/\.info/g');
grep 'rgGames' $f | sed -e 's/appid/\n/g' | tail -n +2 | cut -d '"' -f5,27 $f | tr '"' '\t' > $gamer_tag;
fi;
done;

# example output from gamer_tag=schen_loung.
# examples shows name of games (and how many owned) as well as 
# time played (lack of entry indicates playtime <1hr).
#
# Counter-Strike  2.3
# Counter-Strike: Condition Zero
# Counter-Strike: Condition Zero Deleted Scenes
# Day of Defeat
# Deathmatch Classic
# Ricochet

# No. of characters = 1766