try:
    file = open("data.txt", "r")
except FileNotFoundError:
    file = open("data.txt", "w")
except FileNotFoundError as e:
    print(f"{e}")
else:
    # This runs only if there was no exception in the try block
    print("Division was successful. Result is:")
finally:
    print("Execution completed.")
