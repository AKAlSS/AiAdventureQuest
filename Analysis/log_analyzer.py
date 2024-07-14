import re
from collections import Counter

def analyze_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    error_patterns = [r'ERROR: (.+)', r'Exception: (.+)']
    user_input_pattern = r'User input: (.+)'
    errors = []
    user_inputs = []

    for line in logs:
        for pattern in error_patterns:
            match = re.search(pattern, line)
            if match:
                errors.append(match.group(1))
        match = re.search(user_input_pattern, line)
        if match:
            user_inputs.append(match.group(1))

    error_counts = Counter(errors)
    input_counts = Counter(user_inputs)

    return error_counts, input_counts

def generate_recommendations(error_counts, input_counts):
    recommendations = []

    if error_counts:
        recommendations.append("Errors identified:")
        for error, count in error_counts.items():
            recommendations.append(f"{error}: {count} occurrences")

    if input_counts:
        recommendations.append("User input patterns identified:")
        for input_text, count in input_counts.items():
            recommendations.append(f"'{input_text}': {count} times")

    # Additional recommendations can be added based on the analysis
    return recommendations

if __name__ == "__main__":
    error_counts, input_counts = analyze_logs('game.log')
    recommendations = generate_recommendations(error_counts, input_counts)
    for recommendation in recommendations:
        print(recommendation)
