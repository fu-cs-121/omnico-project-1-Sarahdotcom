# Open the file and read its contents
with open('euphoria_data.csv', 'r') as data_file:
    column_headers = data_file.readline().strip().split(',')  # Read and process header
    user_sessions = [line.strip().split(',') for line in data_file]  # Read all data

# Initialize statistics dictionary
engagement_stats = {algorithm: {'total_happiness': 0, 'total_duration': 0, 'session_count': 0} 
                     for algorithm in ['JoyStream', 'SerenityFlow', 'DeepPulse']}

# Process data
for session in user_sessions:
    algorithm, session_duration, happiness_score = session[1], int(session[2]), int(session[3])
    engagement_stats[algorithm]['session_count'] += 1
    engagement_stats[algorithm]['total_duration'] += session_duration
    engagement_stats[algorithm]['total_happiness'] += happiness_score

# Calculate averages
average_metrics = {
    algorithm: {
        'avg_happiness': engagement_stats[algorithm]['total_happiness'] / engagement_stats[algorithm]['session_count'],
        'avg_duration': engagement_stats[algorithm]['total_duration'] / engagement_stats[algorithm]['session_count']
    } for algorithm in engagement_stats
}

# Display Report
print('Euphoria User Engagement Analysis Report')
print('----------------------------------------\n')

print('Average Happiness Rating per Algorithm:')
for algorithm in engagement_stats:
    print(f'- {algorithm}: {average_metrics[algorithm]["avg_happiness"]:.2f}')
print()

print('Total Number of Sessions per Algorithm:')
for algorithm in engagement_stats:
    print(f'- {algorithm}: {engagement_stats[algorithm]["session_count"]}')
print()

print('Average Session Duration per Algorithm:')
for algorithm in engagement_stats:
    print(f'- {algorithm}: {average_metrics[algorithm]["avg_duration"]:.2f} minutes')
print()

# Determine highest happiness and longest duration
most_happy_algorithm = max(average_metrics, key=lambda x: average_metrics[x]['avg_happiness'])
longest_session_algorithm = max(average_metrics, key=lambda x: average_metrics[x]['avg_duration'])

print(f'Highest Average Happiness Rating:')
print(f'- {most_happy_algorithm} with an average happiness rating of {average_metrics[most_happy_algorithm]["avg_happiness"]:.2f}\n')

print(f'Longest Average Session Duration:')
print(f'- {longest_session_algorithm} with an average session duration of {average_metrics[longest_session_algorithm]["avg_duration"]:.2f} minutes')
