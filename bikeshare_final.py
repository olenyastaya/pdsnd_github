import time
import pandas as pd
import numpy as np
#python bikeshare.py

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
      # Get user input for city (chicago, new york city, washington)
    while True:
        city = input('Enter the city name (Chicago, New York City, Washington): ').lower().strip()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Invalid city name. Please enter a valid city.')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month (all, january, february, march, april, may, june): ').lower().strip()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else: 
            print('Invalid month name. Please enter a valid month.')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of week (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ').lower().strip()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else: 
            print('Invalid day of week name. Please enter a valid day of week.')
    print('-'*40)
    return city, month, day 

#city, month, day = get_filters()
#print(city, month, day)
 
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]

    return df
#df = load_data(city, month, day)   
#print('\nRequested data:\n',df.head()) 
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('\n The most common month:\n',common_month)
    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('\n The most common day of week:\n',common_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\n The most common hour:\n',common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    Common_Start_Station = df['Start Station'].value_counts().idxmax()
    print('\n The most common Start Station:\n',Common_Start_Station)
    # TO DO: display most commonly used end station
    Common_End_Station = df['End Station'].value_counts().idxmax()
    print('\n The most common End Station:\n',Common_End_Station)
    # TO DO: display most frequent combination of start station and end station trip
    Most_frequent_combination_Start_End_Stations = df.groupby(['Start Station','End Station']).size().idxmax()
    print('\n The most frequent combination of start station and end station trip: \n',Most_frequent_combination_Start_End_Stations)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_hours = int(total_travel_time // 3600)
    total_minutes = int((total_travel_time % 3600) // 60)
    total_seconds = int((total_travel_time % 3600) % 60)
    print("Total travel time: {} hour(s) {} minute(s) {} second(s).".format(total_hours, total_minutes, total_seconds))
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_hours = int(mean_travel_time // 3600)
    mean_minutes = int((mean_travel_time % 3600) // 60)
    mean_seconds = int(mean_travel_time % 3600) % 60
    print("Average travel time: {} hour(s) {} minute(s) {} second(s).".format(mean_hours, mean_minutes, mean_seconds))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nUser Types:\n',user_types)
    
    # TO DO: Display counts of gender
    column_name = 'Gender'
    if column_name in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('\nGender statistics:\n',gender_counts)
    else:
        print('\nStatistics on Gender is not available.\n')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    column_name = 'Birth Year'
    if column_name in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        print('\nEarliest Birth Year:\n',earliest_birth_year)

        df['Start Time'] = pd.to_datetime(df['Start Time'])
        greatest_birth_year =  int(df['Birth Year'].max())
        print('\nGreatest Birth Year:\n', greatest_birth_year)

        most_recent_start_time = df['Start Time'].max()
        most_recent_birth_year = int(df[df['Start Time'] == most_recent_start_time]['Birth Year'].values[0])
        print('\nMost recent Birth Year:\n',most_recent_birth_year)

        most_common_birth_year = int(df['Birth Year'].value_counts().idxmax())
        print('\nMost common Birth Year:\n',most_common_birth_year)
    else:
        print('\nStatistics on Birth Year is not available.\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_data(df):
    # Give user a possibility to see the raw data on request
    first_row = 0
    rows_diff = 5
    while True:
        answer = input('Do you want to see 5 lines of raw data? Enter yes or no:').lower().strip()
        if answer == 'yes':
            last_row = first_row + rows_diff
            if last_row <= len(df):
                with pd.set_option('display.max_columns',200):
                    print(df[first_row:last_row])
                    first_row = last_row
            else: 
                print('\nNo more raw data to display.\n')
                break
        elif answer == 'no':
            break
        else: 
            print('Invalid answer. Please enter a valid answer (yes or no).')
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower().strip() != 'yes':
            break
if __name__ == "__main__":
    main()
    