import numpy as np

def logistic_map_complex(z, r, iterations):

    results = []
    for _ in range(iterations):

        # Pemodelan sistem nonlinear Logistic Map
        z = r * z * (1 - z)

        # Normalisasi jika modulus lebih besar dari 1
        if abs(z) > 1:  
            z = z / abs(z)

        # membentuk pola enkripsi berdasarkan interaksi antara dua dimensi
        z_combined = abs(z) * np.angle(z)

        # gabungkan setiap pola enkripsi ke dalam satu array
        results.append(z_combined)

    return results

def string_to_ascii(input_string):

    return [ord(char) for char in input_string]

def encrypt_with_logistic_map(input_string, z0, r):

    # Konversi string menjadi angka ASCII
    ascii_values = string_to_ascii(input_string)

    # Tentukan jumlah iterasi berdasarkan panjang string
    iterations = len(ascii_values)

    # Hasilkan pola iterasi Logistic Map
    logistic_pattern = logistic_map_complex(z0, r, iterations)

    # Skala pola iterasi ke dalam bentuk integer
    scaled_pattern = [int(abs(x) * 1000) for x in logistic_pattern]

    # Lakukan operasi XOR antara ASCII dan pola iterasi
    encrypted_values = [ascii_values[i] ^ scaled_pattern[i] for i in range(iterations)]

    return encrypted_values

def decrypt_with_logistic_map(encrypted_values, z0, r):

    # Tentukan jumlah iterasi berdasarkan panjang ciphertext
    iterations = len(encrypted_values)

    # Hasilkan pola iterasi Logistic Map
    logistic_pattern = logistic_map_complex(z0, r, iterations)

    # Skala pola iterasi ke dalam bentuk integer
    scaled_pattern = [int(abs(x) * 1000) for x in logistic_pattern]

    # Lakukan operasi XOR untuk mendapatkan kembali nilai ASCII
    ascii_values = [encrypted_values[i] ^ scaled_pattern[i] for i in range(iterations)]

    # Konversi kembali ke string
    return ''.join(chr(value) for value in ascii_values)

if __name__ == "__main__":

    # Ambil input string dari terminal
    input_string = input("Masukkan string untuk dienkripsi: ")

    # Parameter kondisi set-up Logistic Map
    z0 = 1.352 + 3.031j     # bilangan kompleks
    r = 3.8                 # parameter kontrol

    # Hasilkan enkripsi
    encrypted_output = encrypt_with_logistic_map(input_string, z0, r)
    print(f"Hasil enkripsi: {encrypted_output}\n")

    z_decrypt_real = float(input("Masukkan komponen real: "))
    z_decrypt_imag = float(input("Masukkan komponen imajiner: "))
    z_decrypt = complex(z_decrypt_real, z_decrypt_imag)

    r_decrypt = float(input("Masukkan parameter kontrol: "))

    # Lakukan dekripsi
    decrypted_output = decrypt_with_logistic_map(encrypted_output, z_decrypt, r_decrypt)
    print("Hasil dekripsi:", decrypted_output)
