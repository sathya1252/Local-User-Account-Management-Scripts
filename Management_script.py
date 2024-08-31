import subprocess

def create_user(username, password):
    try:
        subprocess.run(["net", "user", username, password, "/add"], check=True)
        print(f"User '{username}' created successfully.")
        subprocess.run(["net", "localgroup", "Users", username, "/add"], check=True)
        print(f"User '{username}' added to 'Users' group.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating user: {e}")

def set_user_permissions(username):
    try:
        subprocess.run(["net", "localgroup", "Administrators", username, "/delete"], check=True)
        print(f"User '{username}' removed from 'Administrators' group (if applicable).")
    except subprocess.CalledProcessError as e:
        print(f"Error modifying user permissions: {e}")

if __name__ == "__main__":
    user_name = "keto"  # Replace with the desired username
    user_password = "    "  # Replace with the desired password

    create_user(user_name, user_password)
    set_user_permissions(user_name)
