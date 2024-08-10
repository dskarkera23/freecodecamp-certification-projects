import pandas as pd

def calculate_demographic_data(print_data=True):
    # Sample data similar to what you might find in 'adult.data.csv'
    data = {
        'age': [39, 50, 38, 53, 28, 37, 49, 33, 23, 52],
        'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private', 'Private', 'Private', 'Private', 'Private', 'Self-emp-not-inc'],
        'fnlwgt': [77516, 83311, 215646, 234721, 338409, 284582, 160187, 193524, 76868, 109015],
        'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors', 'Masters', '9th', 'Masters', 'HS-grad', 'Doctorate'],
        'education-num': [13, 13, 9, 7, 13, 14, 5, 14, 9, 16],
        'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse', 'Married-civ-spouse', 'Married-civ-spouse', 'Never-married', 'Never-married', 'Married-civ-spouse'],
        'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty', 'Exec-managerial', 'Other-service', 'Prof-specialty', 'Other-service', 'Prof-specialty'],
        'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife', 'Wife', 'Unmarried', 'Not-in-family', 'Own-child', 'Husband'],
        'race': ['White', 'White', 'White', 'Black', 'Black', 'White', 'Black', 'White', 'White', 'White'],
        'sex': ['Male', 'Male', 'Male', 'Male', 'Female', 'Female', 'Female', 'Female', 'Female', 'Male'],
        'capital-gain': [2174, 0, 0, 0, 0, 0, 0, 0, 0, 14084],
        'capital-loss': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        'hours-per-week': [40, 13, 40, 40, 40, 40, 16, 45, 35, 60],
        'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba', 'United-States', 'Jamaica', 'India', 'United-States', 'India'],
        'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K', '>50K', '<=50K', '>50K', '<=50K', '>50K']
    }

    df = pd.DataFrame(data)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1) if higher_education.shape[0] > 0 else 0
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1) if lower_education.shape[0] > 0 else 0

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1) if num_min_workers.shape[0] > 0 else 0

    # What country has the highest percentage of people that earn >50K?
    country_salary_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_counts = df['native-country'].value_counts()
    percentage_country = (country_salary_counts / country_counts * 100).dropna()

    highest_earning_country = percentage_country.idxmax() if not percentage_country.empty else None
    highest_earning_country_percentage = round(percentage_country.max(), 1) if not percentage_country.empty else None

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()
    top_IN_occupation = top_IN_occupation[0] if not top_IN_occupation.empty else None

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Run the function with the sample data
output = calculate_demographic_data()
print(output)

"""
Output:
Number of each race:
 race
White    7
Black    3
Name: count, dtype: int64
Average age of men: 46.4
Percentage with Bachelors degrees: 30.0%
Percentage with higher education that earn >50K: 50.0%
Percentage without higher education that earn >50K: 0.0%
Min work time: 13 hours/week
Percentage of rich among those who work fewest hours: 0.0%
Country with highest percentage of rich: India
Highest percentage of rich people in country: 100.0%
Top occupations in India: Prof-specialty
"""