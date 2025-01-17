from g4f.client import Client
from g4f.Provider import BingCreateImages, OpenaiChat, Gemini


def detect_algorithm(code):
    client = Client(
    provider=OpenaiChat,
    image_provider=Gemini,
    # Add any other necessary parameters
    )
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        prompt = f"Given the following Python code, please identify the algorithm that it implements. {code}",
        messages=[
            {
                "role": "system",
                "content": "Given the following Python code, please identify the algorithm that it implements. {code}"
    
                }])

    return response.choices[0].message.content
    

code = """ 
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1                                  
"""

print(detect_algorithm(code))