## Repository untuk belajar machine learning
## setup environment
    prerequest:
    1. install git client
        pastikan git sudah terinstall:
        1. buka CMD
        2. git -v
    2. install python 3
        pastikan python sudah terinstall:
        1. buka CMD
        2. python -v
### steps kolaborasi:
    1. fork repository
    2. buka terminal atau cmd
    3. ketik: git clone https://github.com/labkoding/belajar-ml.git
    4. ketik: cd belajar-ml
    5. ketik: code . (aplikasi vscode akan terbuka)
    6. buka terminal dari dalam vscode
    7. ketik py atau python lalu enter
### upload hasil kerjaan
    1. buka terminal/cmd
    2. ketik: cd belajar-ml (untuk masuk ke foler belajar-ml)
    3. ketik: git add *
    4. ketik: git commit -am "hanya print hello world"
    5. ketik: git push origin master

### steps to run flask app
    ```bash
        flask --app filename.py run
    ```
### spesifikasi api index
    1. method: GET
    2. url: /nama/index
    3. response: json
    4. response body:
        {
            "message": "hello world"
        }

