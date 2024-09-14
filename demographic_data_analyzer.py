import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    just_men = df[df['sex'] == 'Male']
    average_age_men = round(just_men['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    just_bachelors = df[df['education'] == 'Bachelors']
    bachelors = just_bachelors['education'].count()
    all_education = df['education'].count()
    fraction = bachelors / all_education
    percentage_bachelors = round(fraction * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    all_higher_education = higher_education['education'].count()
    higher_only_rich = higher_education[higher_education['salary'] == '>50K']['salary'].count()

    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    all_lower_education = lower_education['education'].count()
    lower_only_rich = lower_education[lower_education['salary'] == '>50K']['salary'].count()

    # percentage with salary >50K
    higher_education_rich = round(higher_only_rich * 100 / all_higher_education, 1)
    lower_education_rich = round(lower_only_rich * 100 / all_lower_education, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['hours-per-week'].count()

    min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    num_min_workers_rich = min_workers_rich['salary'].count()

    rich_percentage = 100 * num_min_workers_rich / num_min_workers

    # What country has the highest percentage of people that earn >50K?
    rich_by_country = df[df['salary'] == '>50K'].groupby('native-country').size()
    country_counts = df.groupby('native-country').size()
    highest_earning_country_percentage = round((rich_by_country / country_counts * 100).sort_values(ascending=False).iloc[0], 1)
    highest_earning_country = (rich_by_country / country_counts * 100).idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
    just_india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    occupations_rich = just_india_rich['occupation'].value_counts()
    top_IN_occupation = occupations_rich.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }