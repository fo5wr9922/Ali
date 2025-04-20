import json
import os

DATA_FILE = "donations.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def add_donation():
    name = input("أدخل اسم العنصر المتبرع به: ")
    category = input("نوع العنصر (طعام / ملابس / كتب / أدوات): ")
    location = input("المنطقة / المدينة: ")
    note = input("ملاحظات إضافية (اختياري): ")

    donation = {
        "العنصر": name,
        "النوع": category,
        "المنطقة": location,
        "ملاحظات": note
    }

    data = load_data()
    data.append(donation)
    save_data(data)
    print("تمت إضافة التبرع بنجاح!")

def view_donations():
    data = load_data()
    if not data:
        print("لا توجد تبرعات حالياً.")
        return
    for i, item in enumerate(data, 1):
        print(f"#{i}")
        for key, value in item.items():
            print(f"{key}: {value}")
        print("-" * 20)

def main():
    while True:
        print("\n--- تطبيق مُنقِذ ---")
        print("1. إضافة تبرع")
        print("2. عرض التبرعات")
        print("3. خروج")
        choice = input("اختر خياراً: ")

        if choice == "1":
            add_donation()
        elif choice == "2":
            view_donations()
        elif choice == "3":
            print("مع السلامة!")
            break
        else:
            print("خيار غير صالح. حاول مرة أخرى.")

if __name__ == "__main__":
    main()