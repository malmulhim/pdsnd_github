import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_name = ''
    while city_name.lower() not in CITY_DATA:
        city_name = input("\n What is the name of the city you want to analyze its data? (Please write: chicago, new york city, or washington)\n")
        if city_name.lower() in CITY_DATA:
            city = CITY_DATA[city_name.lower()]
        else:
            print("\nSorry we did not get the name of the city correctly, Please input either chicago, new york city, or washington)\n")


    # TO DO: get user input for month (all, january, february, ... , june)
    month_name=''
    while month_name.lower() not in MONTHS:
        month_name = input("\n What is the name of the month you want to analyze its data? (Please write: 'all' to not apply a month filter or 'january', 'february', .... ,'june')\n")
        if month_name.lower() in MONTHS:
            month = month_name.lower()
        else:
            print("\nSorry we did not get the name of the month correctly, Please input either 'all' to not apply a month filter or 'january', 'february', .... ,'june')\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name=''
    while day_name.lower() not in DAYS:
        day_name = input("\n What is the name of the day you want to analyze its data? (Please write: 'all' to not apply a day filter or 'monday', 'tuesday', .... ,'sunday')\n")
        if day_name.lower() in DAYS:
            day = day_name.lower()
        else:
            print("Sorry we did not get the name of the day correctly, Please input either 'all' to not apply a day filter or 'monday', 'tuesday', .... ,'sunday')\n")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file 
    df = pd.read_csv(city)
    
    #convert start time column to datetime to extract the data from it
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month, day, and hour to create new columns
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable
    if month != 'all':
        month = MONTHS.index(month)
        df = df.loc[df['month'] == month]
        
     #filter by day if applicable
    if day != 'all':
     #   day = DAYS.index(day)
        df = df.loc[df['weekday'] == day.title()]
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month from the given filtered data is: " + MONTHS[common_month].title())


    # TO DO: display the most common day of week
    common_day = df['weekday'].mode()[0]
    print("The most common day from the given filtered data is: " + common_day)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour from the given filtered data is: " + str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station used from the given filtered data is: " + common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station used from the given filtered data is: " + common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station trip is: " + str(frequent_combination.split("||")))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given filterd data is:" + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given filterd data is:" + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The counts of user types from the given filterd data is:" + str(user_types))
        
    # TO DO: Display counts of gender
    #Since the gender column in chicago and new york city files only we will use if condition..
    if city == 'chicago.csv' or city == 'new_york_city.csv':
        gender = df['Gender'].value_counts()
        print("The counts of gender from the given filterd data is:" + str(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print("Earlist birth from the given filterd data is:\n" + str(earliest_birth))
        print("Most recent birth from the given filterd data is:\n" + str(most_recent_birth))
        print("Most commo n birth from the given filterd data is:\n" + str(most_common_birth))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def view_raw_data(df):
   # Display raw data (5 rows at a time ) till the user input 'NO' 
    print(df.head())
    next = 0
    while True:
        raw_data = input('\nwould you like to display the next 5 rows of raw data? (Enter either "yes" or "no".\n')
        if raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])
   


def main():
    while True:
       city, month, day = get_filters()
       df = load_data(city, month, day)

       time_stats(df)
       station_stats(df)
       trip_duration_stats(df)
       user_stats(df,city)
       while True:
            raw_data = input('\nwould you like to display the next 5 rows of raw data? (Enter either "yes" or "no".\n')
            if raw_data.lower() != 'yes':
                break
            view_raw_data(df)
            break


       restart = input('\nWould you like to restart? Enter yes or no.\n')
       
       if restart.lower() != 'yes':
           break
        
        
if __name__ == "__main__":
	main()
