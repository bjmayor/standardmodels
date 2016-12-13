import os
os.environ["USER"] = "user"
print os.path.expandvars("/home/$USER/config")
print os.path.expandvars("$USER/folders")