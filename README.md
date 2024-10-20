# Kamu Personeli Alım İlanları Hatırlatıcısı

- Bu program, Türkiye Cumhuriyeti kamu kurumlarının personel alım ilanlarını takip eden ve bu ilanları kullanıcıya hatırlatan bir programdır.
- Programın amacı, siteye yeni ilan eklenince kullanıcıya e-posta göndererek ilanı hatırlatmaktır.
- Program düzenli olarak saat başı çalışır ve ilanları kontrol eder.

## Kurulum

- Programın çalışabilmesi için bilgisayarınızda **Python 3.9** veya daha üst bir sürümünün yüklü olması gerekmektedir.
- Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install -r requirements.txt
```

- Program gereksinimleri için `.env` dosyası oluşturmanız gerekmektedir. Bu dosya içerisinde aşağıdaki bilgileri tanımlamanız gerekmektedir:

```bash
FROM_MAIL = "your_mail"
FROM_MAIL_PASSWORD = "your_password"
TO_MAIL = "to_mail"
```

**Notlar:**

- `FROM_MAIL` ve `FROM_MAIL_PASSWORD` alanları, programın e-posta göndermek için kullanacağı e-posta adresi ve şifresi olmalıdır. `TO_MAIL` alanı ise, e-posta gönderilecek adresi belirtir.

- Gmail kullanıyorsanız ve 2 adımlı doğrulama açık ise, [şu adresten](https://myaccount.google.com/apppasswords) uygulama şifresi oluşturmanız gerekmektedir.

## Kullanım

- Programı çalıştırmak için aşağıdaki komutları çalıştırabilirsiniz:

```bash
python app.py
```

- Programı arka planda çalıştırmak için aşağıdaki komutu çalıştırabilirsiniz:

```bash
nohup python app.py &
```

- Program çalıştırıldığında, ilanlar kontrol edilir ve yeni ilanlar varsa e-posta gönderilir.
