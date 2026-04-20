def diagnosa_tht():
    print("=========================================")
    print("   Sistem Pakar Diagnosa Penyakit THT    ")
    print("=========================================\n")
    print("Jawablah pertanyaan berikut dengan 'y' (ya) atau 'n' (tidak).\n")

    gejala_user = []

    # Data lengkap 37 Gejala
    daftar_gejala = {
        "G1": "Nafas abnormal", "G2": "Suara serak", "G3": "Perubahan kulit",
        "G4": "Telinga penuh", "G5": "Nyeri bicara menelan", "G6": "Nyeri tenggorokan",
        "G7": "Nyeri leher", "G8": "Pendarahan hidung", "G9": "Telinga berdenging",
        "G10": "Airliur menetes", "G11": "Perubahan suara", "G12": "Sakit kepala",
        "G13": "Nyeri pinggir hidung", "G14": "Serangan vertigo", "G15": "Getah bening",
        "G16": "Leher bengkak", "G17": "Hidung tersumbat", "G18": "Infeksi sinus",
        "G19": "Beratbadan turun", "G20": "Nyeri telinga", "G21": "Selaput lendir merah",
        "G22": "Benjolan leher", "G23": "Tubuh tak seimbang", "G24": "Bolamata bergerak",
        "G25": "Nyeri wajah", "G26": "Dahi sakit", "G27": "Batuk",
        "G28": "Tumbuh dimulut", "G29": "Benjolan dileher", "G30": "Nyeri antara mata",
        "G31": "Radang gendang telinga", "G32": "Tenggorokan gatal", "G33": "Hidung meler",
        "G34": "Tuli", "G35": "Mual muntah", "G36": "Letih lesu", "G37": "Demam"
    }

    # Data lengkap 23 Penyakit dan Gejalanya
    database_penyakit = {
        "Tonsilitis": ["G37", "G12", "G5", "G27", "G6", "G21"],
        "Sinusitis Maksilaris": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
        "Sinusitis Frontalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
        "Sinusitis Edmoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
        "Sinusitis Sfenoidalis": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
        "Abses Peritonsiler": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
        "Faringitis": ["G37", "G5", "G6", "G7", "G15"],
        "Kanker Laring": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
        "Deviasi Septum": ["G37", "G17", "G20", "G8", "G18", "G25"],
        "Laringitis": ["G37", "G5", "G15", "G16", "G32"],
        "Kanker Leher & Kepala": ["G5", "G22", "G8", "G28", "G3", "G11"],
        "Otitis Media Akut": ["G37", "G20", "G35", "G31"],
        "Contact Ulcers": ["G5", "G2"],
        "Abses Parafaringeal": ["G5", "G16"],
        "Barotitis Media": ["G12", "G20"],
        "Kanker Nafasoring": ["G17", "G8"],
        "Kanker Tonsil": ["G6", "G29"],
        "Neuronitis Vestibularis": ["G35", "G24"],
        "Meniere": ["G20", "G35", "G14", "G4"],
        "Tumor Syaraf Pendengaran": ["G12", "G34", "G23"],
        "Kanker Leher Metastatik": ["G29"],
        "Osteosklerosis": ["G34", "G9"],
        "Vertigo Postular": ["G24"]
    }

    # Proses Input Pengguna
    for kode, nama in daftar_gejala.items():
        while True:
            tanya = input(f"Apakah Anda mengalami {nama} ({kode})? (y/n): ").strip().lower()
            if tanya in ['y', 'n']:
                if tanya == 'y':
                    gejala_user.append(kode)
                break
            else:
                print("Input tidak valid. Harap masukkan 'y' atau 'n'.")

    # Proses Diagnosa (Forward Chaining Sederhana)
    hasil_diagnosa = []
    for penyakit, gejala_syarat in database_penyakit.items():
        # Memeriksa apakah SEMUA gejala syarat terpenuhi oleh input user
        if all(g in gejala_user for g in gejala_syarat):
            hasil_diagnosa.append(penyakit)

    # Menampilkan Hasil
    print("\n=========================================")
    print("             HASIL DIAGNOSA              ")
    print("=========================================")
    if len(gejala_user) == 0:
        print("Anda tidak memasukkan gejala apa pun. Anda sepertinya sehat!")
    elif hasil_diagnosa:
        print("Berdasarkan gejala yang Anda alami, Anda kemungkinan menderita:")
        for res in hasil_diagnosa:
            print(f"- {res}")
    else:
        print("Penyakit tidak dapat diidentifikasi dari kombinasi gejala yang diberikan.")
    print("=========================================\n")

if __name__ == "__main__":
    diagnosa_tht()
