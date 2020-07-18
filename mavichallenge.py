# Challenge: 1) Create a method called 'calcDayBorn' that receives two
# parameters.
# 2) The first parameter is the name of the user. The second
# parameter is the full date on which the user was born. Let's start by
# assuming the date will be in the format YYYY-MM-DD.
# 3) The function will print "username was born on a _____" where username is
# the username of the caller and _____ is the day of the week they were born.
# 4) Then, we will use the function to calculate my day born and your day born
def calcDayBorn(username, birth):
    import datetime
    birthdate = birth.split("-")  # Converted birth from a
    # single string into a list of three strings
    birthdatetime = datetime.datetime(
        int(birthdate[0]), int(birthdate[1]), int(birthdate[2])
    )
    if birthdatetime.weekday() == 0:
        return ("%s was born on a Monday" % username)
    elif birthdatetime.weekday() == 1:
        return ("%s was born on a Tuesday" % username)
    elif birthdatetime.weekday() == 2:
        return ("%s was born on a Wednesday" % username)
    elif birthdatetime.weekday() == 3:
        return ("%s was born on a Thursday" % username)
    elif birthdatetime.weekday() == 4:
        return ("%s was born on a Friday" % username)
    elif birthdatetime.weekday() == 5:
        return ("%s was born on a Saturday" % username)
    elif birthdatetime.weekday() == 6:
        return ("%s was born on a Sunday" % username)


def main():
    print(calcDayBorn("mavaddat", "1982-05-26"))
    print(calcDayBorn("Joshua", "2009-2-24"))


if __name__ == "__main__":
    main()
