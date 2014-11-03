

class NextDate1():  # Simple version

    def Date(self, month, day, year):
        tomorrowDay = 0
        tomorrowMonth = 0
        tomorrowYear = 0

        if month in (1, 3, 5, 7, 8, 10):  # 31 day months (except Dec.)
            if day < 31:
                tomorrowDay = day + 1
                tomorrowMonth = month
                tomorrowYear = year
            else:
                tomorrowDay = 1
                tomorrowMonth = month + 1

        if month in (4, 6, 9, 11):  # 30 day months
            if day < 30:
                tomorrowDay = day + 1
                tomorrowMonth = month
                tomorrowYear = year
            else:
                tomorrowDay = 1
                tomorrowMonth = month + 1

        if month == 12:  # December
            if day < 31:
                tomorrowDay = day + 1
                tomorrowMonth = month
                tomorrowYear = year
            else:
                tomorrowDay = 1
                tomorrowMonth = 1
                if year == 2012:
                    print("2012 is over")
                else:
                    tomorrowYear = year + 1

        if month == 2:  # February
            if day < 28:
                tomorrowDay = day + 1
                tomorrowMonth = month
                tomorrowYear = year
            else:
                if day == 28:
                    tomorrowDay = 1
                    tomorrowMonth = 3
                elif day == 29:
                    tomorrowDay = 1
                    tomorrowMonth = 3
                else:
                    print("Cannot have Feb.", day)

        print"Tomorrow's date is: ", tomorrowMonth, tomorrowDay, tomorrowYear
