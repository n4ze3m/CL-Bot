# git push --mirror https://github.com/NazeemNato/CL-Bot.git

# https://en.wikipedia.org/wiki/UEFA_coefficient#Men's_Club_coefficient
# Using current uefa coefficient rankings
# England , Spain, Germany and Italy required teams
# France and Portugal  70-30 chance

# Fixtures post 
# fixtures results requried to post after one hours

# Round 16
# No Same nations

# Home and Away fixtures required 
# Max goals 7 

# Final one leg
import tweepy
from twitter_api import *
from bs4 import BeautifulSoup
from bs4.dammit import EncodingDetector
import requests
from random import choices,sample,randint
from league_list import *
from time import sleep
header ={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
def top4leagues(leagueList,index): 
    rangeOfWork = team_qulfied[index]
    defaultLst = []
    temIndex = sample(range(12),rangeOfWork)
    #print(rangeOfWork)
    #print(temIndex)
    for i in range(rangeOfWork):
        clubsIndex = randint(0,1)
        #print(clubsIndex)
        try:
            tempClubsLst = []
            url = 'https://www.worldfootball.net'+leagueList[clubsIndex]
            source = requests.get(url, headers=header)
            http_encoding = source.encoding if 'charset' in source.headers.get('content-type', '').lower() else None
            html_encoding = EncodingDetector.find_declared_encoding(source.content, is_html=True)
            encoding = html_encoding or http_encoding
            soup = BeautifulSoup(source.content, 'lxml', from_encoding=encoding)
            find_boxS= soup.find('div',class_="scrollable_tables")
            the_team_table = find_boxS.find('table', {'class':'standard_tabelle'})
            for theTeamAtag in the_team_table.find_all('a',href=True):
                if theTeamAtag.text:
                    tempClubsLst.append(theTeamAtag.text)
            y = temIndex[i]
            teamNames = tempClubsLst[y]
            defaultLst.append(teamNames)
            tempClubsLst.pop()
        except Exception as e:
            print(e)
    return defaultLst

def otherTeams(sumOfQ):
    remainigTeams = 16- sumOfQ
    finalTeams = []
    if remainigTeams <=0:
        return []
    else:
        randomTeams = sample(range(10),remainigTeams)
        randomTeamsIndex = sample(range(remainigTeams+2),remainigTeams)
        randomTeamSelection = choices(range(len(league_qlf_list)),k=remainigTeams)
        #print(randomTeams)
        #print(randomTeamsIndex)
        #print(randomTeamSelection)
        for i in range(0,remainigTeams):
            temp_x = randomTeamSelection[i]
            try:
            	tempClubsLst = []
            	url = 'https://www.worldfootball.net'+league_qlf_list[temp_x]
            	source = requests.get(url, headers=header)
            	http_encoding = source.encoding if 'charset' in source.headers.get('content-type', '').lower() else None
            	html_encoding = EncodingDetector.find_declared_encoding(source.content, is_html=True)
            	encoding = html_encoding or http_encoding
            	soup = BeautifulSoup(source.content, 'lxml', from_encoding=encoding)
            	find_boxS= soup.find('div',class_="scrollable_tables")
            	the_team_table = find_boxS.find('table', {'class':'standard_tabelle'})
            	for theTeamAtag in the_team_table.find_all('a',href=True):
            		if theTeamAtag.text:
            			tempClubsLst.append(theTeamAtag.text)
            	y = randomTeamsIndex[i]
            	teamNames = tempClubsLst[y]
            	finalTeams.append(teamNames)
            except Exception as e:
                print(e)
        return finalTeams
def the16(epl,laliga,seriea,bundesliga,other):
    tempLst = []
    theLstOfLeagues = [epl,laliga,seriea,bundesliga,other]
    for i in range(len(theLstOfLeagues)):
        for j in range(len(theLstOfLeagues[i])):
            tempLst.append(theLstOfLeagues[i][j])
    return tempLst

def vsPrint(year,home,away,n):
    apndLst = []
    for i in range(n):
        tag = '#UCL'
        results = home[i]+' VS '+away[i]+'\n'
        apndLst.append(results)
    if len(apndLst)  == 8:
        mes = str(year)+' UCL - Round of 16\n\n'
        f1 = '[1/2] '+tag
        c = ''.join(map(str, apndLst[0:4]))
        print(mes+c+f1) # Change that to tweepy status update
        api.update_status(status=mes+c+f1)
        sleep(100) # change that to 30 sec afther finishing
        f2 ='[2/2] '+tag
        p =''.join(map(str, apndLst[4:8]))
        print(mes+p+f2)
        api.update_status(status=mes+p+f2)
        sleep(100)
    elif len(apndLst) == 4:
        mes = str(year)+' UCL - Quarter finals \n\n'
        c = ''.join(map(str, apndLst))
        print(mes+c+tag)
        api.update_status(status=mes+c+tag)
        sleep(300)
    else:
        mes = str(year)+' UCL - Semi finals \n\n'
        c = ''.join(map(str, apndLst))
        print(mes+c+tag)
        api.update_status(status=mes+c+tag)
        sleep(300)
def legScores(n):
    homeTeam = []
    if n == 1:
        for i in range(n):
            scoreHome = randint(0,4)
            homeTeam.append(scoreHome)
    else:
        for i in range(n):
            scoreHome = randint(0,6)
            homeTeam.append(scoreHome)
    return homeTeam
def resultsTweet(home,away,s1,s2,n):
	tag = '#UCL'
	apndLst=[]
	for i in range(n):
		results = home[i]+' '+str(s1[i])+'-'+str(s2[i])+' '+away[i]+'\n'
		apndLst.append(results)
	if len(apndLst)  == 8:
		mes = str(year)+' UCL Results - Round of 16\n\n'
		f1 = '[1/2] '
		c = ''.join(map(str, apndLst[0:4]))
		print(mes+c+f1+tag) # Change that to tweepy status update
		api.update_status(status=mes+c+f1+tag)
		sleep(150) # change that to 30 sec afther finishing
		f2 ='[2/2] '
		p =''.join(map(str, apndLst[4:8]))
		print(mes+p+f2+tag)
		api.update_status(status=mes+p+f2+tag)
		sleep(150)
	elif len(apndLst) == 4:
		mes = str(year)+' UCL Results - Quarter finals \n\n'
		c = ''.join(map(str, apndLst))
		print(mes+c+tag)
		api.update_status(status=mes+c+tag)
		sleep(600)
	else:
		mes = str(year)+' UCL Results - Semi finals \n\n'
		c = ''.join(map(str, apndLst))
		print(mes+c+tag)
		api.update_status(status=mes+c+tag)
		sleep(600)
def koTeams(h,a,s1,s2,n, year):
    tempTeams = []
    if n == 2:
        for i in range(n):
            if s1[i] > s2[i]:
                s = str(s1[i])+'-'+str(s2[i])
                mes = '😍 '+str(year)+', '+h[i]+' beat '+a[i]+' ('+s+') to qualify for the UCL final. #UCLFinal'
                print(mes)
                tempTeams.append(h[i])
                api.update_status(status=mes)
                sleep(800)
            elif s1[i] < s2[i]:
                s= str(s2[i])+'-'+str(s1[i])
                mes = '😍 '+str(year)+', '+a[i]+' beat '+h[i]+' ('+s+') to qualify for the UCL final. #UCLFinal'
                print(mes)
                tempTeams.append(a[i])
                api.update_status(status=mes)
                sleep(800)
            else:
                t = randint(0,1)
                if t == 0:
                    scr = ['5-3','4-2','5-4','3-2','6-5','4-3']
                    ran = randint(0,5)
                    mes='🤪😍 '+str(year)+', '+h[i]+' defeats '+a[i]+' in shootout ('+scr[ran]+'), advancing to UCL final #UCLFinal '
                    print(mes)
                    api.update_status(status=mes)
                    tempTeams.append(h[i])
                    sleep(800)
                else:
                    scr = ['5-3','4-2','5-4','3-2','6-5','4-3']
                    ran = randint(0,5)
                    s =str(s2[i])+'-'+str(s1[i])
                    mes='🤪😍 '+str(year)+', '+a[i]+' defeats '+h[i]+' in shootout ('+scr[ran]+'), advancing to UCL final #UCLFinal'
                    print(mes)
                    api.update_status(status=mes)
                    tempTeams.append(a[i])
                    sleep(800)
    else:
        for i in range(n):
            if s1[i] > s2[i]:
                s = str(s1[i])+'-'+str(s2[i])
                mes = '😼 '+str(year)+', '+h[i]+' beat '+a[i]+' ('+s+') and qualified to the next UCL round. #UCL'
                print(mes)
                api.update_status(status=mes)
                tempTeams.append(h[i])
                sleep(800)
            elif s1[i] < s2[i]:
                s= str(s2[i])+'-'+str(s1[i])
                mes = '😼 '+str(year)+', '+a[i]+' beat '+h[i]+' ('+s+') and qualified to the next UCL round. #UCL'
                print(mes)
                api.update_status(status=mes)
                tempTeams.append(a[i])
                sleep(800)
            else:
                t = randint(0,1)
                if t == 0:
                    s = str(s1[i])+'-'+str(s2[i])
                    mes='😱 '+str(year)+', '+h[i]+' triumphed via a penalty shootout, after the match agains '+a[i]+' ended '+ s+' in normal time #UCL'
                    print(mes)
                    api.update_status(status=mes)
                    tempTeams.append(h[i])
                    sleep(800)
                else:
                    s =str(s2[i])+'-'+str(s1[i])
                    mes='😱 '+str(year)+', '+a[i]+' triumphed via a penalty shootout, after the match agains '+h[i]+' ended '+ s+' in normal time #UCL'
                    print(mes)
                    api.update_status(status=mes)
                    tempTeams.append(a[i])
                    sleep(800)
    return tempTeams
def finalCongrats(h,a,s1,s2,year):
    #year = 2045
    for i in range(1):
    	who = str(year)+' 😍 UCL Final'+h[i]+' vs '+a[i]+ ' #UCLFinal'
    	api.update_status(status=who)
    	sleep(1800)
        if s1[i]>s2[i]:
            s = str(s1[i])+'-'+str(s2[i])
            mes = str(year)+','+h[i]+' beat '+a[i]+' ('+s+') to win Champions League trophy 🏆 \n#UCLFinal'
            print(mes)
            api.update_status(status=mes)
            sleep(150)
            print()
            s = str(s1[i])+'-'+str(s2[i])
            ucl = '🏆 '+str(year)+' UCL FINAL RESULT🏆 \n'+h[i]+'⭐️ '+s+' '+a[i]+'\n#UCLFinal'
            print(ucl)
            path = '/1.jpeg'
            api.update_status(status=ucl)
            sleep(150)
            cong = '😍🏆 Congratulations to '+ h[i]+' for winning the '+str(year)+' Champions League title \n#UCLFinal'
            print(cong)
            api.update_status(status=mes)
            sleep(150)
        elif s1[i]<s2[i]:
            s = str(s2[i])+'-'+str(s1[i])
            mes = str(year)+','+a[i]+' beat '+h[i]+' ('+s+') to win Champions League trophy 🏆 \n#UCLFinal'
            print(mes)
            api.update_status(status=mes)
            sleep(150)
            s = str(s1[i])+'-'+str(s2[i])
            ucl = '🏆 '+str(year)+' UCL FINAL RESULT🏆 \n'+h[i]+' '+s+' ⭐️'+a[i]+'\n#UCLFinal'
            print(ucl)
            api.update_status(status=ucl)
            sleep(150)
            path = '/1.jpeg'
            cong = '😍🏆 Congratulations to '+ a[i]+' for winning the '+str(year)+' Champions League title \n#UCLFinal'
            api.update_status(status=cong)
            print(cong)
            sleep(150)
        else:
            #year = 2045
            #s = str(s2[i])+'-'+str(s1[i])
            t = randint(0,1)
            if t == 0:
                scr = ['5-3','4-2','5-4','3-2','6-5','4-3']
                ran = randint(0,5)
                mes = h[i]+' Beat '+a[i]+' '+scr[ran]+' on  penalties in the '+str(year)+' Champions League final 🏆 \n#UCLFinal'
                print(mes)
                api.update_status(status=mes)
                sleep(150)
                cong ='😍🏆 Congratulations to '+ h[i]+' for winning the '+str(year)+' Champions League title \n#UCLFinal'
                path = '/1.jpeg'
                api.update_status(status=cong)
                print(cong)
                sleep(150)
            else:
                scr = ['5-3','4-2','5-4','3-2','6-5','4-3']
                ran = randint(0,5)
                mes =  a[i]+' Beat '+h[i]+' '+scr[ran]+' on  penalties in the '+str(year)+' Champions League final 🏆 \n#UCLFinal'
                print(mes)
                api.update_status(status=mes)
                sleep(150)
                cong = '😍🏆 Congratulations to '+ a[i]+' for winning the '+str(year)+' Champions League title \n#UCLFinal'
                path = '/1.jpeg'
                api.update_status(status=cong)
                print(cong)
                sleep(150)
print("BOT Started")
print()
for year in range(2054,8000):
	try:
		data = [1,2,3,4]
		team_qulfied = choices(data,k=4)
		epl_lst=top4leagues(english_leagues,0)
		bundesliga_lst =top4leagues(german_leagues,1)
		laliga_lst=top4leagues(spainsh_league,2)
		serieA_lst = top4leagues(italian_leagues,3)
		sumOfQ = sum(team_qulfied)
		otherTeams_lst =otherTeams(sumOfQ)
		the16teams = the16(epl_lst,bundesliga_lst,laliga_lst,serieA_lst,otherTeams_lst)
		teamA = the16teams[0:8]
		teamB = the16teams[8:16]
		scores1 = legScores(8)
		scores2 = legScores(8)
		vsPrint(year,teamA,teamB,8)
		t = koTeams(teamA,teamB,scores1,scores2,8,year)
		resultsTweet(teamA,teamB,scores1,scores2,8)
		scores1 = legScores(4)
		scores2 = legScores(4)
		teamA = t[0:4]
		teamB = t[4:8]
		vsPrint(year,teamA,teamB,4)
		t = koTeams(teamA,teamB,scores1,scores2,4,year)
		resultsTweet(teamA,teamB,scores1,scores2,4)
		scores1 = legScores(2)
		scores2 = legScores(2)
		teamA = t[0:2]
		teamB = t[2:4]
		vsPrint(year,teamA,teamB,2)
		t = koTeams(teamA,teamB,scores1,scores2,2,year)
		resultsTweet(teamA,teamB,scores1,scores2,2)
		teamA = t[0:1]
		teamB = t[1:2]
		scores1 = legScores(1)
		scores2 = legScores(1)
		finalCongrats(teamA,teamB,scores1,scores2,year)
	except Exception as e:
		print(e)