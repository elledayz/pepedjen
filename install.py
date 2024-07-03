import subprocess  
# Define the command to be executed 
command = ['pip', 'install', '-r', 'requirements.txt'] 
# Execute the command 
subprocess.run(command, check=True)
