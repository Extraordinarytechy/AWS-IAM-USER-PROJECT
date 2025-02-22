import boto3
import random
import string


# intialize AWS IAM client
iam = boto3.client('iam')

def generate_password(length=12):
    """ Generate a random password."""
 
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range (length))

def check_user_exists(username):
    """Check if the IAM user already exists."""
    
    try:

        iam.get_user(UserName=username)
        return True
   
    except iam.exceptions.NoSuchEntityException:
        return False

def get_user_policies(username):
    """Get a list of policies attached to the user."""
    attached_policies = iam.list_attached_user_policies(UserName=username)['AttachedPolicies']
    return [policy['PolicyName'] for policy in attached_policies]


def create_user(username):
    """ Create IAM user if it does not exist and generate login credentials."""
    formatted_username = f"aws-{username}"  # added prefix to avoid collison

    if check_user_exists(formatted_username):
        print(f"IAM user '{formatted_username}'already exists.")
        return # Prevent further execution if user exists

     # Create user
    iam.create_user(UserName=formatted_username)

        # Generate a random password
    password = generate_password()

    try:
        # Assign login password
        iam.create_login_profile(
            UserName=formatted_username,
            Password=password,
            PasswordResetRequired=True
       )

        print(f"IAM user '{formatted_username}' created successfully.")
        print(f"Temporary password: {password}")
        print(f"Login URL: https://console.aws.amazon.com")
  
    except iam.exceptions.PasswordPolicyViolationException as e:
        print(f"Password policy violation: {e}")
 
def attach_policy(username, policy_arn):
    """Attach a policy to the IAM user."""
    iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    print(f"policy {policy_arn} attached to user {username}.")

def main():
 
  # Essential AWS policies list
    policies = {
       "AdministratorAccess": "arn:aws:iam::aws:policy/AdministratorAccess",
       "AmazonS3FullAccess": "arn:aws:iam::aws:policy/AmazonS3FullAccess",
       "AmazonEC2FullAccess": "arn:aws:iam::aws:policy/AmazonEC2FullAccess",     
       "AmazonEC2ReadOnlyAccess":"arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess",
       "CloudWatchFullAccess": "arn:aws:iam::aws:policy/CloudWatchFullAccess",
       "AWSLambdaBasicExecutionRole": "arn:aws:iam::aws:policy/AWSLambdaBasicExecutionRole"
    }

      # user input
    username = input("Enter IAM username: ")
    
       #create user if not exists
    create_user(username)

       # Get current policies attached to user
    formatted_username = f"aws-{username}"
    user_policies = get_user_policies(formatted_username)

      #if user has Admin access ,skip policy attachment
    if "AdministratorAccess" in user_policies:
        print(f"User '{formatted_username}' already has AdministratorAccess."
                " No additonal policies needed.")
        return

      # Show available policies 
    print("\nAvailable policies:")
     
    for idx, policy_name in enumerate(policies.keys(), start=1):
        print(f"{idx}. {policy_name}")

      # Selected policies
    selected_policies = input("\nEnter policy numbers (comma-separated, e.g 1,2):").split(',')

    for choice in selected_policies:
        choice = choice.strip().rstrip('.') 
        if choice.isdigit():
           choice= int(choice)
           if 1 <= choice <= len(policies):
               policy_name = list(policies.keys())[choice - 1]
               if policy_name not in user_policies:
                   attach_policy(formatted_username, policies[policy_name])
               else:
                    print(f"Policy '{policy_name}' is already attached to '{formatted_username}'."
                            "Skipping attachment.")
           else:
               print(f"Invalid selection: {choice}")
        else:
             print(f"Invalid input: {choice}")

if __name__ == "__main__":
    main()

