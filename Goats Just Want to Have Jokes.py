import statistics
import csv
 
def read_csv_data_set(file_name):
    '''
    Read a data set from a CSV file.
 
    Parameters
    ----------
    file_name : string
        Name of the CSV file in the current folder.
 
    Returns
    -------
    data_set : List of dictionaries.
        Data set.
 
    '''
    # Create a list to be the return value.
    data_set = []
    with open('./' + file_name) as file:
        file_csv = csv.DictReader(file)
        # Put each row into the return list.
        for row in file_csv:
            data_set.append(row)
    return data_set

def is_count_ok(count_in, min):
    # Is it an int?
    try:
        count = int(count_in)
    except Exception:
        # Not an int.
        return False
    # Check range.
    if count < min:
        return False
    # All OK.
    return True

def is_record_ok(record):
    performer = record['Performer'].strip().lower()
    if performer == '' or performer == None:
        return False
    hecklers = record['Hecklers']
    sound = record['Highest laugh dB']
    if not is_count_ok(hecklers, 0):
        return False
    if not is_count_ok(sound, 0):
        return False
    return True

def clean_goat_data(raw_goat_data):
    clean_data = []
    invalid_data = 0
    for raw_record in raw_goat_data:
        if is_record_ok(raw_record):
            clean_record = {
                'Performer': raw_record['Performer'],
                'Hecklers': int(raw_record['Hecklers']),
                'Highest laugh dB': int(raw_record['Highest laugh dB'])
                }
            clean_data.append(clean_record)
        else:
            invalid_data += 1
    return clean_data, invalid_data

def extract_goat_data(cleaned_goat_data):
    heckler_list = []
    sound_list = []
    for record in cleaned_goat_data:
        hecklers = record['Hecklers']
        sound = record['Highest laugh dB']
        heckler_list.append(hecklers)
        sound_list.append(sound)
    return heckler_list, sound_list

raw_goat_data = read_csv_data_set('goat-jokes.csv')
cleaned_goat_data, invalid_goat_data = clean_goat_data(raw_goat_data)
heckler_data, sound_data = extract_goat_data(cleaned_goat_data)

#processing
heckler_mean = statistics.mean(heckler_data)
heckler_stdev = statistics.stdev(heckler_data)
heckler_min = min(heckler_data)
heckler_max = max(heckler_data)

sound_mean = statistics.mean(sound_data)
sound_stdev = statistics.stdev(sound_data)
sound_min = min(sound_data)
sound_max = max(sound_data)

#min and max records
heckler_min_record = min(cleaned_goat_data, key=lambda x: x['Hecklers'])
heckler_max_record = max(cleaned_goat_data, key=lambda x: x['Hecklers'])
sound_min_record = min(cleaned_goat_data, key=lambda x: x['Highest laugh dB'])
sound_max_record = max(cleaned_goat_data, key=lambda x: x['Highest laugh dB'])

#min and max performers
heckler_min_performer = heckler_min_record['Performer']
heckler_max_performer = heckler_max_record['Performer']
sound_min_performer = sound_min_record['Performer']
sound_max_performer = sound_max_record['Performer']

#output
print('Goats Just Want to Have Jokes')
print('===== ==== ==== == =====')
print('')
print('Counts')
print('- - - -')
print('Valid records: ' + str(len(cleaned_goat_data)))
print('Invalid records: ' + str(invalid_goat_data))
print('Total records: ' + str(len(raw_goat_data)))
print('')
print('Hecklers')
print('- - - -')
print('Mean: ' + str(round(heckler_mean, 2)))
print('Std dev: ' + str(round(heckler_stdev, 2)))
print('Smallest: ' + str(heckler_min) + ' ' + heckler_min_performer)
print('Largest: ' + str(heckler_max) + ' ' + heckler_max_performer)
print('')
print('Sound')
print('- - -')
print('Mean: ' + str(round(sound_mean, 2)))
print('Std dev: ' + str(round(sound_stdev, 2)))
print('Smallest: ' + str(sound_min) + ' ' + sound_min_performer)
print('Largest: ' + str(sound_max) + ' ' + sound_max_performer)
