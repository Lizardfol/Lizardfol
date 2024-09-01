import random
import math

num_stations = int(input('Állomások száma: '))
num_trains = int(input('Vonato száma: '))
max_capacity = int(input('Maximális kapacitás: '))
max_time = int(input('Napok száma: '))

G = {
    0: {
        'name': 'Pécs', 
        'load': random.randint(20, 70),
        'connections': {
            1: {'time': 12, 'risk': 0.04},  # Pécs -> Nyíregyháza
            3: {'time': 18, 'risk': 0.03}   # Pécs -> Nyugati
        }
    },
    1: {
        'name': 'Nyíregyháza', 
        'load': random.randint(20, 70),
        'connections': {
            0: {'time': 12, 'risk': 0.04},  # Nyíregyháza -> Pécs
            2: {'time': 15, 'risk': 0.02}   # Nyíregyháza -> Debrecen
        }
    },
    2: {
        'name': 'Debrecen', 
        'load': random.randint(20, 70),
        'connections': {
            1: {'time': 15, 'risk': 0.02},  # Debrecen -> Nyíregyháza
            4: {'time': 20, 'risk': 0.05}   # Debrecen -> Bécs
        }
    },
    3: {
        'name': 'Nyugati', 
        'load': random.randint(20, 70),
        'connections': {
            0: {'time': 18, 'risk': 0.03},  # Nyugati -> Pécs
            4: {'time': 10, 'risk': 0.01}   # Nyugati -> Bécs
        }
    },
    4: {
        'name': 'Bécs', 
        'load': random.randint(20, 70),
        'connections': {
            2: {'time': 20, 'risk': 0.05},  # Bécs -> Debrecen
            3: {'time': 10, 'risk': 0.01}   # Bécs -> Nyugati
        }
    }
}


for station_id, station_info in G.items():
    print(f"Állomás: {station_info['name']}, Utasok száma: {station_info['load']}")
    for conn_id, conn_info in station_info['connections'].items():
        print(f"  Kapcsolat: {G[conn_id]['name']}, Idő: {conn_info['time']}, Kockázat: {conn_info['risk']}")
    print("\n")



def simulate_traffic(G, num_trains, max_time):
    for t in range(max_time):
        print(f"Nap: {t}")
        for train_id in range(num_trains):
            start_station = random.choice(list(G.keys()))
            end_station = random.choice(list(G.keys()))
            if start_station == end_station:
                continue

            print(f"Vonat {train_id} indul {G[start_station]['name']} állomásról, célállomás: {G[end_station]['name']}")


            if end_station in G[start_station]['connections']:
                path = [start_station, end_station]
                total_time = G[start_station]['connections'][end_station]['time']
                total_risk = G[start_station]['connections'][end_station]['risk']

                print(f"Útvonal: {G[start_station]['name']} -> {G[end_station]['name']}, "
                      f"útidő: {total_time} perc, baleset esélye: {total_risk}")


                for station in path:
                    G[station]['load'] = min(G[station]['load'] + 10, max_capacity)


                accident_chance = random.random()
                if accident_chance < total_risk:
                    print(f"Baleset történt az útvonalon {G[start_station]['name']} és {G[end_station]['name']} között.")
                    total_time *= random.randint(1 , 3)  
                    print(f"Az új útidő: {total_time} perc.")
            else:
                print(f"Nincs közvetlen kapcsolat {G[start_station]['name']} és {G[end_station]['name']} között.")

        print("\n")


simulate_traffic(G, num_trains, max_time)
