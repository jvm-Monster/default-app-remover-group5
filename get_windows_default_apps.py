import subprocess


# This function is used to get windows diffult apps
def get_default_apps():
    try:
        # Run the windows PowerShell command to get the default apps
        result = subprocess.run(['powershell',
                                 'Get-AppxPackage | Where-Object {($_.Publisher -like "*Microsoft Corporation*") '
                                 '-and (-not $_.IsFramework) -and ($_.SignatureKind -eq "Store")}'],
                                capture_output=True, text=True)

        # Split the output by newlines to get individual app information
        app_lines = result.stdout.strip().split('\n')

        # Extract the name of each app
        defaults = [line.split(':')[1].strip() for line in app_lines if line.startswith('Name')]

        return defaults
    except subprocess.CalledProcessError:
        return []


# Test the function
print(get_default_apps())
