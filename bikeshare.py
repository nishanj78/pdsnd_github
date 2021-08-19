# Script for interactive interrogation of bikeshare data

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    while True:
        try:
            city = input("Enter the city: ").lower()
            if city in CITY_DATA.keys():
                break
            
            else:
                print("Invalid city! Try again")

        except:
            print("Invalid input! Try again")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("Enter the month: ").lower()
            if month in MONTH_DATA:
                break
            
            else:
                print("Invalid month! Try again")

        except:
            print("Invalid input! Try again")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Enter the day: ").lower()
            if day in DAY_DATA:
                break
            
            else:
                print("Invalid day! Try again")

        except:
            print("Invalid input! Try again")

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = MONTH_DATA.index(month)
    
        # filter by month to create the new dataframe
        df = df.loc[(df['month'] == month)]

    # filter by day of week if applicable
    if day != 'all':
        
        # filter by day of week to create the new dataframe
        df = df.loc[(df['day_of_week'] == day.title())]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most common month: ' + MONTH_DATA[df['month'].mode()[0]].title())

    # TO DO: display the most common day of week
    print('Most common day of week: ' + df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start hour: ' + str(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most common start station: ' + df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('Most common end station: ' + df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    df['Start End Station'] = df['Start Station'] + " and " + df['End Station']
    print('Most common combination of start and end station: ' + df['Start End Station'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time: ' + str(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('Mean travel time: ' + str(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types:\n' + str(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    try:
        print('Counts of gender:\n' + df['Gender'].value_counts())
    except:
        print('Gender data not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('Earliest birth year: ' + str(df['Birth Year'].min().astype(int)))
        print('Most recent birth year: ' + str(df['Birth Year'].max().astype(int)))
        print('Most common birth year: ' + str(df['Birth Year'].mode()[0].astype(int)))
    except:
        print('Birth Year data not available')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        # Per Rubric, prompt user if they want to see the raw data
        i = 0
        more_data = input('\nWould you like to see the first 5 rows of raw data? Enter yes or no:\n')
        while more_data.lower() == 'yes':
            df_slice = df.iloc[i:i+5]
            print(df_slice)
            i += 5
            more_data = input('\nWould you like to see the next 5 rows of raw data? Enter yes or no:\n')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
