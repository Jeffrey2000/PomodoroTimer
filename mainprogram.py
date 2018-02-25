import time
from time import gmtime, strftime
from bs4 import BeautifulSoup;
from urllib.request import Request, urlopen
from random import randint
from multiprocessing import Process


class Pomodoro:
    scoredPoints = 0;
    counterTimerInSeconds = 1500;
    pageUrl = Request("https://www.brainyquote.com/topics/motivational", headers={'User-Agent': 'Chrome'});
    pageToGetQuotesFrom = urlopen(pageUrl).read()
    webpageSourceCode = BeautifulSoup(pageToGetQuotesFrom, 'html.parser');
    timeIntervalsToDelay = [1, 300, 900, 1380];

    def __init__(self):
        self.scoredPoints += 1;
        print(strftime("%H:%M:%S", gmtime()));

    def userProceed(self):
        readyToContinue = input("Are you ready to continue ? ");
        if readyToContinue:
            return True
        else:
            self.userProceed();

    def printMotivationalQuotes(self, timesToDelay):
        time.sleep(timesToDelay)
        # quotes are all within anchor <a> tags and have the title therefore they need to be searched
        motivationalQuotesFromPage = self.webpageSourceCode.find_all('a', attrs={"title": "view quote"});
        print(motivationalQuotesFromPage[randint(0, len(motivationalQuotesFromPage) - 1)].text)

    def beginCountingDown(self, timerDuration):
        while timerDuration:
            timerMinutes, timerSeconds = divmod(timerDuration, 60);
            formatOfTime = '{:02d}:{:02d}'.format(timerMinutes, timerSeconds)
            print(formatOfTime, end='\r');
            time.sleep(1)
            timerDuration -= 1

    def startProcess(self, function, arguments): #dyadic function maybe should look to refactoring
        currentProcess = Process(target=function, args=[arguments]);
        currentProcess.start();
        return currentProcess;

    #unable to start and join process under the same function -more research to be done
    def joinProcess(self,process):
        process.join();


if __name__ == "__main__":
    newPomodoro = Pomodoro();
    willProceed = newPomodoro.userProceed();
    if willProceed:
        for eachTimeDelay in range(len(newPomodoro.timeIntervalsToDelay)):
            printMotivationalQuotesProcess = newPomodoro.startProcess(newPomodoro.printMotivationalQuotes,newPomodoro.timeIntervalsToDelay[eachTimeDelay]);
        beginCountingDownProcess = newPomodoro.startProcess(newPomodoro.beginCountingDown, newPomodoro.counterTimerInSeconds);

        newPomodoro.joinProcess(beginCountingDownProcess);
        newPomodoro.joinProcess(printMotivationalQuotesProcess);


#
