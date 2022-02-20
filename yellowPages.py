# Import Module
import uuid  # (str(uuid.uuid4())[:6])
from dataVar import *  # import data variable
from prettytable import PrettyTable  # Table


def tampilData():
    print(menuTampil)
    while True:
        tampil = input('Pilih Menu [1-4]: ')
        try:
            tampil = int(tampil)
        except:
            pass
        else:
            if tampil == 1:
                tampilSemua()
                break
            elif tampil == 2:
                while True:
                    abjad = input('Masukkan 1 Huruf Abjad: ').upper()
                    if len(abjad) == 1 and abjad.isalnum() == True:
                        tampilAbjad(abjad)
                        break
                break
            elif tampil == 3:
                tampilFavorit()
                break
            elif tampil == 4:
                print(menuUtama)
                break
# End of tampilData()


def tampilSemua():
    t = PrettyTable(['Index', 'Nama', 'Telp'], sortby='Nama')
    for i in range(len(data)):
        d = list(data[i].values())[1:3]
        d.insert(0, i)
        t.add_row(d)
    print(t)
    tampilDetail()
# End of tampilSemua()


def tampilAbjad(abjad):
    t = PrettyTable(['Index', 'Nama', 'Telp'], sortby='Nama')
    for i in range(len(data)):
        d = list(data[i].values())[1:3]
        if d[0][0] == abjad:
            d.insert(0, i)
            t.add_row(d)
    print(t)
    tampilDetail()
# End of tampilAbjad()


def tampilFavorit():
    t = PrettyTable(['Index', 'Nama', 'Telp'], sortby='Nama')
    for i in range(len(data)):
        d = list(data[i].values())[1:3]
        if data[i]['fav'] == True:
            d.insert(0, i)
            t.add_row(d)
    print(t)
    tampilDetail()
# End of tampilFavorit()


def tampilDetail():
    while True:
        detail = input(
            'Masukkan Nomor index untuk melihat detail data, atau ketik x untuk kembali ke menu utama: ')
        if detail == 'x':
            print(menuUtama)
            break
        else:
            try:
                detail = int(detail)
            except:
                pass
            else:
                if detail < len(data):
                    if data[detail]['id'] == '1c2f7a':
                        print('\nMaaf, Kamu tidak punya ayang :(\n')
                    else:
                        print(menuDetail.format(id=data[detail]['id'],
                                                nama=data[detail]['Nama'],
                                                telp=data[detail]['Telp'],
                                                alamat=data[detail]['Alamat'],
                                                website=data[detail]['Website'],
                                                fav=data[detail]['fav']))

                        print(menuAlter)
                        while True:
                            alter = input('Pilih menu [1-3]:')
                            try:
                                alter = int(alter)
                            except:
                                continue
                            else:
                                if alter == 1:
                                    ubahData(detail)
                                    break
                                elif alter == 2:
                                    while True:
                                        konfirmasi = input(
                                            'Apakah anda yakin ingin menghapus data tersebut (y/t): ')
                                        if konfirmasi.lower() == 'y':
                                            print(
                                                f"\nData dengan nama {data[detail]['Nama']} telah dihapus")
                                            del data[detail]
                                            break
                                        elif konfirmasi.lower() == 't':
                                            print('Data tidak dihapus')
                                            break
                                    break
                                elif alter == 3:
                                    break
                        print(menuUtama)
                        break
                else:
                    print(f'Data dengan index {detail} tidak tersedia')
# End of tampilDetail()


def ubahData(i):  # i=index
    print(menuUbah)
    while True:
        ubah = input('Pilih data yang ingin diubah [1-5]: ')
        try:
            ubah = int(ubah)
            k = list(data[i].keys())[ubah]  # key
        except:
            continue
        else:
            if ubah == 5:
                if list(data[i].values())[ubah] == True:
                    while True:
                        uFav = input(
                            'Data kontak berada di dalam favorit, ingin mengilangkannya dari favorit (y/t): ')
                        if uFav.lower() == 'y':
                            while True:
                                konfirmasi = input(
                                    'Apakah anda yakin ingin menyimpan perubahan (y/t): ')
                                if konfirmasi.lower() == 'y':
                                    data[i].update({k: False})
                                    print('Data berhasil diubah')
                                    break
                                elif konfirmasi.lower() == 't':
                                    print('Data tidak diubah')
                                    break
                            break
                        elif uFav.lower() == 't':
                            print('Favorit tidak diubah')
                            break
                elif list(data[i].values())[ubah] == False:
                    while True:
                        uFav = input(
                            'Data kontak tidak berada di dalam favorit, ingin menambahkannya ke favorit (y/t): ')
                        if uFav.lower() == 'y':
                            while True:
                                konfirmasi = input(
                                    'Apakah anda yakin ingin menyimpan perubahan (y/t):')
                                if konfirmasi.lower() == 'y':
                                    data[i].update({k: True})
                                    print('Data berhasil diubah')
                                    break
                                elif konfirmasi.lower() == 't':
                                    print('Data tidak diubah')
                                    break
                            break
                        elif uFav.lower() == 't':
                            print('Favorit tidak diubah')
                            break
            else:
                if k == 'Nama':
                    while True:
                        ubahan = input(f'Ubah data {k} menjadi: ')
                        if len(ubahan) >= 2:
                            break
                        else:
                            print('Masukkan nama dengan benar')
                elif k == 'Telp':
                    while True:
                        ubahan = input(f'Ubah data {k} menjadi: ')
                        if ubahan.isdecimal() == True:
                            if ubahan[:2] == '08' or ubahan[:3] == '628':
                                break
                            else:
                                print('Hanya masukan no telp berawalan 08 atau 628')
                        else:
                            print('Hanya masukan angka')
                else:
                    ubahan = input(f'Ubah data {k} menjadi: ')

                while True:
                    konfirmasi = input(
                        'Apakah anda yakin ingin menyimpan perubahan (y/t):')
                    if konfirmasi.lower() == 'y':
                        if ubah == 1:
                            data[i].update({k: ubahan.title()})
                            print('Data berhasil diubah')
                            break
                        else:
                            data[i].update({k: ubahan})
                            print('Data berhasil diubah')
                            break
                    elif konfirmasi.lower() == 't':
                        print('Data tidak diubah')
                        break
        print(menuUtama)
        break
# End of ubahData()


def tambahData():
    # Duplicate Checker
    while True:
        id = str(uuid.uuid4())[:6]
        for i in range(len(data)):
            if data[i]['id'] == id:
                id = str(uuid.uuid4())[:6]
        break

    while True:
        nama = input('Masukkan Nama: ').title()
        if len(nama) >= 2:
            break
        else:
            print('Masukkan nama dengan benar')

    while True:
        telp = input('Masukkan Nomor Telp: ')
        if telp.isdecimal() == True:
            if telp[:2] == '08' or telp[:3] == '628':
                break
            else:
                print('Hanya masukan no telp berawalan 08 atau 628')
        else:
            print('Hanya masukan angka')

    alamat = input('Masukkan Alamat: ')
    website = input('Masukkan Alamat Website: ')

    while True:
        fav = input('Masukkan ke Kontak Favorit (y/t): ')
        if fav.lower() == 'y':
            fav = True
            break
        elif fav.lower() == 't':
            fav = False
            break

    kontakBaru = {'id': id, 'Nama': nama, 'Telp': telp,
                  'Alamat': alamat, 'Website': website, 'fav': fav}

    while True:
        simpanKontak = input('Ingin menyimpan kontak (y/t): ')
        if simpanKontak.lower() == 'y':
            data.append(kontakBaru)
            print(f'\nData dengan nama {nama} telah tersimpan')
            print(menuUtama)
            break
        elif simpanKontak.lower() == 't':
            print('\nBaik, data tidak akan disimpan')
            print(menuUtama)
            break
# End of tambahData()


print('\n++++++Yellow Pages - Kontak Telefon++++++')
print(menuUtama)
while True:
    menu = input('Pilih Menu [1-3]: ')
    try:
        menu = int(menu)
    except:
        pass
    else:
        if menu == 1:
            tampilData()
        elif menu == 2:
            tambahData()
        elif menu == 3:
            print('\nTerimakasih Sudah Menggunakan Layanan Kami')
            break
