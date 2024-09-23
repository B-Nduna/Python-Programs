def calculate_aspect_ratio(width, height):
    # Calculate the greatest common divisor (GCD) to simplify the ratio
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    # Calculate GCD of width and height
    divisor = gcd(width, height)
    
    # Simplify the aspect ratio
    aspect_ratio_width = width // divisor
    aspect_ratio_height = height // divisor
    
    return aspect_ratio_width, aspect_ratio_height

# Prompt the user for width and height
try:
    width = int(input("Enter the width: "))
    height = int(input("Enter the height: "))
    
    if width <= 0 or height <= 0:
        raise ValueError("Width and height must be positive integers.")
    
    # Calculate the aspect ratio
    aspect_ratio = calculate_aspect_ratio(width, height)
    
    # Display the result
    print(f"The aspect ratio is: {aspect_ratio[0]}:{aspect_ratio[1]}")

except ValueError as e:
    print(f"Invalid input: {e}")
