def create_user_profile(**kwargs):
    if not kwargs:
        return "No profile data provided."

    profile_parts = []
    for key, value in kwargs.items():
        profile_parts.append(f"{key.capitalize()}: {value}")
    
    return "\n".join(profile_parts)

# Example usage
profile = create_user_profile(name="Alice", age=30, occupation="Engineer")
print(profile)