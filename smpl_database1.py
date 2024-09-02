class SimpleDB:
    def __init__(self, filename='database.txt'):
        self.filename = filename
        self.load_data()

    def load_data(self):
        self.data = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    key, value = line.strip().split(':', 1)
                    self.data[key] = value
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.filename, 'w') as file:
            for key, value in self.data.items():
                file.write(f'{key}:{value}\n')

    def select(self):
        if not self.data:
            print("Adat hiány")
        else:
            for key, value in self.data.items():
                print(f"ID: {key}, Adat: {value}")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_data()
            print(f"Törlés ID: {key}")
        else:
            print("Ilyen ID nincs.")

    def edit(self, key, new_data):
        if key in self.data:
            self.data[key] = new_data
            self.save_data()
            print(f"Frissítés: ID: {key}")
        else:
            print("ID nem létezik.")

    def new(self, key, data):
        if key in self.data:
            print("ID ilyen néven már létezik.")
        else:
            self.data[key] = data
            self.save_data()
            print(f"Új ID: {key}")

    def rename(self, old_key, new_key):
        if old_key in self.data:
            if new_key in self.data:
                print("New ID already exists.")
            else:
                self.data[new_key] = self.data.pop(old_key)
                self.save_data()
                print(f"Átnevezés ID {old_key}-ről {new_key}-ra.")
        else:
            print("Nincs ilyen nevü file.")

if __name__ == "__main__":
    db = SimpleDB()

    while True:
        command = input("Írjon be egy parancsot (SELECT, DELETE, EDIT, NEW, RENAME, EXIT): ").strip().upper()

        if command == 'SELECT':
            db.select()
        elif command == 'DELETE':
            key = input("Írja be az ID-t a törléshez: ").strip()
            db.delete(key)
        elif command == 'EDIT':
            key = input("Írjon be ID a módosításhoz: ").strip()
            new_data = input("Új adat: ").strip()
            db.edit(key, new_data)
        elif command == 'NEW':
            key = input("Új ID: ").strip()
            data = input("Adat: ").strip()
            db.new(key, data)
        elif command == 'RENAME':
            old_key = input("Régi ID: ").strip()
            new_key = input("Új ID: ").strip()
            db.rename(old_key, new_key)
        elif command == 'EXIT':
            print("Ciao...")
            break
        else:
            print("IDK.")
