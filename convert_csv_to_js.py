#!/usr/bin/env python3
import csv
import json
import os

def parse_csv(filename):
    """Parse a Caltrain CSV file and return train data"""
    trains = []
    
    # First, read all data into memory
    all_rows = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        all_rows = list(reader)
    
    # Train numbers are all columns except Zone and Station Name (and empty columns)
    train_numbers = [h for h in headers if h and h not in ['Zone', 'Station Name'] and h.strip()]
    
    # Build a dictionary for each train
    for train_num in train_numbers:
        train_data = {'train_number': train_num}
        
        for row in all_rows:
            station_name = row['Station Name']
            time = row.get(train_num, '').strip()
            
            if time and time != '--' and time != '':
                # Map station names to keys used in the JS
                station_key = get_station_key(station_name)
                if station_key:
                    train_data[station_key] = time
        
        # Only add trains that have at least one stop
        if len(train_data) > 1:
            trains.append(train_data)
    
    return trains

def get_station_key(station_name):
    """Map CSV station names to JS keys"""
    mapping = {
        'San Francisco': 'sf',
        '22nd Street': '22nd',
        'Bayshore': 'bayshore',
        'South San Francisco': 'ssf',
        'San Bruno': 'bruno',
        'Millbrae': 'millbrae',
        'Burlingame': 'burlingame',
        'San Mateo': 'sanmateo',
        'Hayward Park': 'hayward',
        'Hillsdale': 'hillsdale',
        'Belmont': 'belmont',
        'San Carlos': 'sancarlos',
        'Redwood City': 'redwood',
        'Menlo Park': 'menlo',
        'Palo Alto': 'palo',
        'California Avenue': 'calave',
        'San Antonio': 'sanantonio',
        'Mountain View': 'mv',
        'Sunnyvale': 'sunnyvale',
        'Lawrence': 'lawrence',
        'Santa Clara': 'santaclara',
        'College Park': 'collegepark',
        'San Jose Diridon': 'sanjose',
        'Tamien': 'tamien',
        'Capitol': 'capitol',
        'Blossom Hill': 'blossomhill',
        'Morgan Hill': 'morganhill',
        'San Martin': 'sanmartin',
        'Gilroy': 'gilroy'
    }
    return mapping.get(station_name)

def is_bullet_train(train_data):
    """Determine if a train is a bullet train based on stops"""
    # Bullet trains typically skip many stations
    # This is a heuristic - adjust based on actual Caltrain bullet patterns
    total_possible_stops = 24
    actual_stops = len(train_data) - 1  # -1 for train_number field
    return actual_stops < total_possible_stops * 0.5

def format_train_for_js(train_data):
    """Format train data for JavaScript output"""
    # Remove train_number from output
    output = {k: v for k, v in train_data.items() if k != 'train_number'}
    
    # Add bullet flag if applicable
    if is_bullet_train(train_data):
        output['bullet'] = True
    
    return output

def main():
    csv_dir = 'caltrain_data'
    
    # Process all schedule files
    schedules = {
        'weekday': {
            'northbound': parse_csv(os.path.join(csv_dir, 'Untitled spreadsheet - weekday northbound.csv')),
            'southbound': parse_csv(os.path.join(csv_dir, 'Untitled spreadsheet - weekday southbound.csv'))
        },
        'weekend': {
            'northbound': parse_csv(os.path.join(csv_dir, 'Untitled spreadsheet - weekend northbound.csv')),
            'southbound': parse_csv(os.path.join(csv_dir, 'Untitled spreadsheet - weekend southbound.csv'))
        }
    }
    
    # Generate JavaScript file
    with open('caltrain-data-new.js', 'w') as f:
        # Station coordinates (keep existing)
        f.write("""// Caltrain station coordinates
const stations = {
    sf: { name: 'San Francisco', lat: 37.7764, lng: -122.3946 },
    '22nd': { name: '22nd Street', lat: 37.7575, lng: -122.3926 },
    bayshore: { name: 'Bayshore', lat: 37.7095, lng: -122.4009 },
    ssf: { name: 'South San Francisco', lat: 37.6557, lng: -122.4047 },
    bruno: { name: 'San Bruno', lat: 37.6305, lng: -122.4111 },
    millbrae: { name: 'Millbrae', lat: 37.6002, lng: -122.3869 },
    burlingame: { name: 'Burlingame', lat: 37.5798, lng: -122.3451 },
    sanmateo: { name: 'San Mateo', lat: 37.5685, lng: -122.3240 },
    hayward: { name: 'Hayward Park', lat: 37.5523, lng: -122.3091 },
    hillsdale: { name: 'Hillsdale', lat: 37.5376, lng: -122.2979 },
    belmont: { name: 'Belmont', lat: 37.5208, lng: -122.2758 },
    sancarlos: { name: 'San Carlos', lat: 37.5073, lng: -122.2602 },
    redwood: { name: 'Redwood City', lat: 37.4856, lng: -122.2318 },
    menlo: { name: 'Menlo Park', lat: 37.4543, lng: -122.1825 },
    palo: { name: 'Palo Alto', lat: 37.4434, lng: -122.1651 },
    calave: { name: 'California Avenue', lat: 37.4291, lng: -122.1417 },
    sanantonio: { name: 'San Antonio', lat: 37.4071, lng: -122.1072 },
    mv: { name: 'Mountain View', lat: 37.3947, lng: -122.0762 },
    sunnyvale: { name: 'Sunnyvale', lat: 37.3784, lng: -122.0308 },
    lawrence: { name: 'Lawrence', lat: 37.3708, lng: -121.9970 },
    santaclara: { name: 'Santa Clara', lat: 37.3535, lng: -121.9368 },
    sanjose: { name: 'San Jose Diridon', lat: 37.3303, lng: -121.9024 }
};

""")
        
        # Weekday schedule
        f.write("// Complete weekday schedule with all stations\n")
        f.write("const weekdaySchedule = {\n")
        f.write("    // Southbound trains from SF\n")
        f.write("    southbound: [\n")
        for i, train in enumerate(schedules['weekday']['southbound']):
            formatted = format_train_for_js(train)
            json_str = json.dumps(formatted, indent=8)
            if i < len(schedules['weekday']['southbound']) - 1:
                f.write(f"        {json_str},\n")
            else:
                f.write(f"        {json_str}\n")
        f.write("    ],\n")
        
        f.write("    // Northbound trains to SF\n")
        f.write("    northbound: [\n")
        for i, train in enumerate(schedules['weekday']['northbound']):
            formatted = format_train_for_js(train)
            json_str = json.dumps(formatted, indent=8)
            if i < len(schedules['weekday']['northbound']) - 1:
                f.write(f"        {json_str},\n")
            else:
                f.write(f"        {json_str}\n")
        f.write("    ]\n")
        f.write("};\n\n")
        
        # Weekend schedule
        f.write("// Complete weekend schedule with all stations\n")
        f.write("const weekendSchedule = {\n")
        f.write("    // Southbound trains from SF\n")
        f.write("    southbound: [\n")
        for i, train in enumerate(schedules['weekend']['southbound']):
            formatted = format_train_for_js(train)
            json_str = json.dumps(formatted, indent=8)
            if i < len(schedules['weekend']['southbound']) - 1:
                f.write(f"        {json_str},\n")
            else:
                f.write(f"        {json_str}\n")
        f.write("    ],\n")
        
        f.write("    // Northbound trains to SF\n")
        f.write("    northbound: [\n")
        for i, train in enumerate(schedules['weekend']['northbound']):
            formatted = format_train_for_js(train)
            json_str = json.dumps(formatted, indent=8)
            if i < len(schedules['weekend']['northbound']) - 1:
                f.write(f"        {json_str},\n")
            else:
                f.write(f"        {json_str}\n")
        f.write("    ]\n")
        f.write("};\n")
    
    print("Generated caltrain-data-new.js successfully!")
    print("You can review the file and then replace the old caltrain-data.js with it.")

if __name__ == "__main__":
    main()