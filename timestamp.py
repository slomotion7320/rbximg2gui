from datetime import datetime

# Validated format for filenames
def cleantimestamp():
    return (str(datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))) 