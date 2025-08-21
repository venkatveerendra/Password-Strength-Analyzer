import re
import string
import getpass

class PasswordStrengthAnalyzer:
    def __init__(self):
        self.min_length = 8
        self.score = 0
        self.feedback = []

    def check_length(self, password):
        if len(password) >= self.min_length:
            self.score += 1
            self.feedback.append("✓ Password meets minimum length requirement")
        else:
            self.feedback.append("✗ Password should be at least 8 characters long")

    def check_uppercase(self, password):
        if any(c.isupper() for c in password):
            self.score += 1
            self.feedback.append("✓ Password contains uppercase letters")
        else:
            self.feedback.append("✗ Password should contain uppercase letters")

    def check_lowercase(self, password):
        if any(c.islower() for c in password):
            self.score += 1
            self.feedback.append("✓ Password contains lowercase letters")
        else:
            self.feedback.append("✗ Password should contain lowercase letters")

    def check_numbers(self, password):
        if any(c.isdigit() for c in password):
            self.score += 1
            self.feedback.append("✓ Password contains numbers")
        else:
            self.feedback.append("✗ Password should contain numbers")

    def check_special_chars(self, password):
        if any(c in string.punctuation for c in password):
            self.score += 1
            self.feedback.append("✓ Password contains special characters")
        else:
            self.feedback.append("✗ Password should contain special characters")

    def check_common_patterns(self, password):
        common_patterns = [
            r'12345',
            r'qwerty',
            r'password',
            r'admin'
        ]
        
        if any(re.search(pattern, password.lower()) for pattern in common_patterns):
            self.feedback.append("✗ Password contains common patterns")
        else:
            self.score += 1
            self.feedback.append("✓ Password doesn't contain common patterns")

    def analyze_password(self, password):
        self.score = 0
        self.feedback = []

        self.check_length(password)
        self.check_uppercase(password)
        self.check_lowercase(password)
        self.check_numbers(password)
        self.check_special_chars(password)
        self.check_common_patterns(password)

        strength = (self.score / 6) * 100
        return strength, self.feedback

def main():
    analyzer = PasswordStrengthAnalyzer()
    
    print("Password Strength Analyzer")
    print("=========================")
    
    while True:
        password = getpass.getpass("Enter a password to analyze (or 'q' to quit): ")
        
        if password.lower() == 'q':
            break

        strength, feedback = analyzer.analyze_password(password)
        
        print("\nPassword Strength Analysis:")
        print("---------------------------")
        for item in feedback:
            print(item)
            
        print(f"\nOverall Strength: {strength:.1f}%")
        
        if strength < 50:
            print("Verdict: Weak password")
        elif strength < 80:
            print("Verdict: Moderate password")
        else:
            print("Verdict: Strong password")
        
        print("\n")

if __name__ == "__main__":
    main()
