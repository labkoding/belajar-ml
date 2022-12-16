5. tugas tanggal 15 November 2022
Buatlah script python untuk penggunaan library chat bot. Contoh script nya ada di link berikut:
https://chatterbot.readthedocs.io/en/stable/examples.html

agar library chatbot nya bisa dipakai, ikuti langkah-langka berikut:
  1. pip3.7 install ChatterBot
  2. pip3.7 install spacy
  3. python3.7 -m spacy download en_core_web_sm
  4. edit file /Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/chatterbot/chatterbot.py
  5. replace line ke 13:
          spacy.load(self.language.ISO_639_1.lower())
      dengan:
          if self.language.ISO_639_1.lower() == 'en':
              self.nlp = spacy.load('en_core_web_sm')
          else:
              self.nlp = spacy.load(self.language.ISO_639_1.lower())

  untuk perintah pip dan python disesuaikan dengan yang ada pada computer masing-masing,
  begitu juga pada step nomor 4, disusaikan dengan alamat direktory pada masing-masing komputer

  Script pythhon di atas dibuat pada folder masing-masing pada repository belajar-ml
  hasil tugas dikumpulkan melalui pull request pada repository belajar-ml

