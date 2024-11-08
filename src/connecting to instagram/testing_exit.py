import sys , os

def func(x):
    if (x == 1):
        print("An error has occured")
        raise SystemError("HUH")
    
    print(x * x)
    return

# try:
#     func(0)
# except SystemError as e:
#     print(e)
#     sys.exit(1)


os.path.abspath(__file__)
root_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

output_directory = os.path.join(root_directory,"sample_output")

clip_names = list(os.listdir(output_directory))

print(clip_names)