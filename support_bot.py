def support_bot(issue):
    issues = {
        "login issue": "Please reset your password and try again.",
        "api error": "Verify API key and endpoint configuration.",
        "slow system": "Check system resources and network connectivity."
    }
    return issues.get(issue.lower(), "Please raise a support ticket.")

if __name__ == "__main__":
    user_issue = input("Enter your issue: ")
    print(support_bot(user_issue))
