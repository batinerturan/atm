# Use Case = Kullanım Durumları
# Check = Kontrol Etmek 
# Idle = Durur
# Scalable = Ölçeklenebilir


# Para Çekmek - Para Yatırmak - Şifre Değiştirmek 
# Kart - Şifre - Hesap İhtiyacı var

# 1) Para Çekme 
# Kartını taktı 
    # Şifre Soracağız
    # Kart - Şifre Uyumu, Şifre - Hesap Uyumu,Kart - Hesap Uyumu
    # Kart - Şifre Uyumlu değil:
        # 3 Kez şifre Soralım
    # Çekmek istediği miktar: 
            # ATM de vardır
                # Miktar hesabında vardır 
                    # Kişinin hesabından çektiği parayı düşeceğiz
                    # ATM'nin kasasından da çektiği paraya düşeceğiz
                # Miktar hesabında yoktur  
                    # Mesaj yazacağız     
            # ATM de yoktur 
                # Mesaj yazacağız 
            
# Kart Takılı değil
 

# 2) Para Yatırma
# Kartını taktı 
    # Şifre Soracağız
    # Kart - Şifre Uyumu, Şifre - Hesap Uyumu,Kart - Hesap Uyumu
    # Kart - Şifre Uyumlu değil:
        # 3 Kez şifre Soralım

    # Yatırmak istediğin miktar:
        # ATM nin kapasitesinden az:
            # Hesabına bu parayı ekleyeceğiz
            # ATM ye bu parayı ekleyeceğiz
        # ATM nin kapasitesinden fazla:
            # Mesaj yazacağız

# 3) Şifre Değiştirme
# Kartını taktı 
    # Şifre Soracağız
    # Kart - Şifre Uyumu, Şifre - Hesap Uyumu,Kart - Hesap Uyumu
    # Kart - Şifre Uyumlu değil:
        # 3 Kez şifre Soralım  

    # Yeni şifre girilecek
        # Kullanıcı bilgilerini güncelleyeceğiz. 

# Veri Tabanı

bankamatik = {'para_miktari':10000}

kullanıcılar = {'batın': 
                    {
                     'kart_no' : 190719071907     
                     },
                'ali':
                    {
                     'kart_no' : 199919991999
                    }
                }

banka_bilgileri = {190719071907:
                   {
                       'şifre' : 1907,
                       'hesap_no' :19071907
                   },
                   199919991999:{
                       'hesap_no':19991999,
                        'şifre':1999,
                   }
                   
                }


batın_kart_no = kullanıcılar['batın']['kart_no']

print(banka_bilgileri[batın_kart_no]['hesap_no'])