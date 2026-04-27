class MyCalendar:

    def __init__(self):
        self.calendar=[]

    def book(self, startTime: int, endTime: int) -> bool:
        current=[startTime,endTime]
        if self.calendar:
            for i in range(len(self.calendar)):
                if current[1]<=self.calendar[i][0]:
                    if i==0:
                        self.calendar.insert(i,current)
                        return True
                    elif current[0]>=self.calendar[i-1][1]:
                        self.calendar.insert(i,current)
                        return True
                    else:
                        return False
            else:
                if current[0]>=self.calendar[-1][1]:
                    self.calendar.append(current)
                    return True
                else:
                    return False
        else:
            self.calendar.append(current)
            return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)