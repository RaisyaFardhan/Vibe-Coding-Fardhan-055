import tkinter as tk
from tkinter import messagebox
import random


# =========================================================
# WARNA
# =========================================================

WARNA_BG = "#FFF8F0"
WARNA_UTAMA = "#6C5CE7"
WARNA_SEKUNDER = "#A29BFE"

WARNA_PINK = "#FD79A8"
WARNA_PINK_GELAP = "#E84393"

WARNA_BIRU = "#0984E3"
WARNA_BIRU_MUDA = "#74B9FF"

WARNA_KUNING = "#FDCB6E"
WARNA_EMAS = "#F39C12"

WARNA_HIJAU = "#00B894"
WARNA_UNGU = "#6C5CE7"

WARNA_TEXT = "#2D3436"
WARNA_PUTIH = "#FFFFFF"

WARNA_CARD_CAPTION = "#FFE4EC"
WARNA_BORDER_CAPTION = "#FD79A8"

WARNA_CARD_TAGLINE = "#E3F2FD"
WARNA_BORDER_TAGLINE = "#0984E3"


# =========================================================
# FONT
# =========================================================

FONT_JUDUL = ("Times New Roman", 25, "bold")
FONT_JUDUL_HOME = ("Times New Roman", 32, "bold")
FONT_SUBJUDUL = ("Times New Roman", 17, "bold")
FONT_NORMAL = ("Times New Roman", 13)
FONT_BUTTON = ("Times New Roman", 12, "bold")


# =========================================================
# WINDOW UTAMA
# =========================================================

window = tk.Tk()

window.title("✨ Creative Caption & Tagline Generator ✨")
window.geometry("900x700")
window.resizable(False, False)
window.configure(bg=WARNA_BG)


# =========================================================
# FUNGSI MENGHAPUS HALAMAN
# =========================================================

def hapus_halaman():

    for widget in window.winfo_children():
        widget.destroy()


# =========================================================
# NAVBAR
# =========================================================

def buat_navbar():

    navbar = tk.Frame(
        window,
        bg=WARNA_UTAMA,
        height=65
    )

    navbar.pack(fill="x")
    navbar.pack_propagate(False)


    # Logo
    logo = tk.Label(
        navbar,
        text="✨ Creative Generator",
        bg=WARNA_UTAMA,
        fg=WARNA_PUTIH,
        font=("Times New Roman", 17, "bold")
    )

    logo.pack(
        side="left",
        padx=25
    )


    # Tombol Beranda
    tombol_home = tk.Button(
        navbar,
        text="🏠 Beranda",
        command=halaman_utama,
        bg=WARNA_UTAMA,
        fg=WARNA_PUTIH,
        activebackground=WARNA_SEKUNDER,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_home.pack(
        side="right",
        padx=8
    )


    # Tombol Tagline
    tombol_tagline = tk.Button(
        navbar,
        text="💡 Tagline",
        command=halaman_tagline,
        bg=WARNA_UTAMA,
        fg=WARNA_PUTIH,
        activebackground=WARNA_SEKUNDER,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_tagline.pack(
        side="right",
        padx=8
    )


    # Tombol Caption
    tombol_caption = tk.Button(
        navbar,
        text="📝 Caption",
        command=halaman_caption,
        bg=WARNA_UTAMA,
        fg=WARNA_PUTIH,
        activebackground=WARNA_SEKUNDER,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_caption.pack(
        side="right",
        padx=8
    )


# =========================================================
# HALAMAN UTAMA
# =========================================================

def halaman_utama():

    hapus_halaman()
    buat_navbar()


    frame = tk.Frame(
        window,
        bg=WARNA_BG
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # Emoji
    emoji = tk.Label(
        frame,
        text="🌟",
        bg=WARNA_BG,
        font=("Times New Roman", 50)
    )

    emoji.pack(
        pady=(40, 5)
    )


    # Judul
    judul = tk.Label(
        frame,
        text="Selamat Datang!",
        bg=WARNA_BG,
        fg=WARNA_UTAMA,
        font=FONT_JUDUL_HOME
    )

    judul.pack()


    # Salam
    salam = tk.Label(
        frame,
        text="Halo! Senang melihat kamu di sini. 👋",
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=("Times New Roman", 18, "bold")
    )

    salam.pack(
        pady=12
    )


    # Deskripsi
    deskripsi = tk.Label(
        frame,
        text=(
            "Selamat datang di Creative Caption & Tagline! ✨\n\n"
            "Aplikasi sederhana ini dibuat untuk membantu kamu\n"
            "menemukan ide caption dan tagline yang menarik.\n\n"
            "Masukkan tema yang kamu inginkan, pilih jenis tulisan,\n"
            "dan biarkan kreativitas dimulai! 🚀"
        ),
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=FONT_NORMAL,
        justify="center"
    )

    deskripsi.pack(
        pady=15
    )


    # Frame tombol
    frame_pilihan = tk.Frame(
        frame,
        bg=WARNA_BG
    )

    frame_pilihan.pack(
        pady=20
    )


    # Tombol Caption
    tombol_caption = tk.Button(
        frame_pilihan,
        text="📝\nBuat Caption",
        command=halaman_caption,
        bg=WARNA_PINK,
        fg=WARNA_PUTIH,
        activebackground=WARNA_PINK_GELAP,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        width=18,
        height=3,
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_caption.grid(
        row=0,
        column=0,
        padx=15
    )


    # Tombol Tagline
    tombol_tagline = tk.Button(
        frame_pilihan,
        text="💡\nBuat Tagline",
        command=halaman_tagline,
        bg=WARNA_BIRU,
        fg=WARNA_PUTIH,
        activebackground=WARNA_BIRU_MUDA,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        width=18,
        height=3,
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_tagline.grid(
        row=0,
        column=1,
        padx=15
    )


# =========================================================
# HALAMAN CAPTION
# =========================================================

def halaman_caption():

    hapus_halaman()
    buat_navbar()


    frame = tk.Frame(
        window,
        bg=WARNA_BG
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # Judul
    judul = tk.Label(
        frame,
        text="📝 Caption Generator",
        bg=WARNA_BG,
        fg=WARNA_PINK,
        font=FONT_JUDUL
    )

    judul.pack(
        pady=(25, 5)
    )


    # Keterangan
    keterangan = tk.Label(
        frame,
        text="Buat caption panjang yang cocok untuk postingan media sosial ✨",
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=FONT_NORMAL
    )

    keterangan.pack(
        pady=5
    )


    # Label input
    label_input = tk.Label(
        frame,
        text="Masukkan tema yang ingin dibuat:",
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=FONT_SUBJUDUL
    )

    label_input.pack(
        pady=(10, 5)
    )


    # Input
    input_tema = tk.Entry(
        frame,
        width=50,
        font=FONT_NORMAL,
        justify="center",
        relief="solid",
        bd=1
    )

    input_tema.pack(
        pady=5,
        ipady=7
    )

    input_tema.insert(
        0,
        "Masukkan tema..."
    )


    # =====================================================
    # FRAME HASIL CAPTION
    # =====================================================

    frame_hasil = tk.Frame(
        frame,
        bg=WARNA_CARD_CAPTION,
        highlightbackground=WARNA_BORDER_CAPTION,
        highlightthickness=3
    )

    frame_hasil.pack(
        padx=50,
        pady=15,
        fill="both",
        expand=True
    )


    # Judul hasil
    judul_hasil = tk.Label(
        frame_hasil,
        text="✨ HASIL CAPTION ✨",
        bg=WARNA_CARD_CAPTION,
        fg=WARNA_PINK_GELAP,
        font=("Times New Roman", 16, "bold")
    )

    judul_hasil.pack(
        pady=(10, 0)
    )


    # Text hasil
    hasil_text = tk.Text(
        frame_hasil,
        height=10,
        wrap="word",
        bg=WARNA_CARD_CAPTION,
        fg=WARNA_TEXT,
        font=FONT_NORMAL,
        relief="flat",
        padx=20,
        pady=10
    )

    hasil_text.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=5
    )


    # Warna teks caption
    hasil_text.tag_config(
        "pembuka",
        foreground=WARNA_UNGU,
        font=("Times New Roman", 15, "bold")
    )

    hasil_text.tag_config(
        "isi",
        foreground=WARNA_TEXT,
        font=("Times New Roman", 13)
    )

    hasil_text.tag_config(
        "penutup",
        foreground=WARNA_EMAS,
        font=("Times New Roman", 14, "bold")
    )

    hasil_text.tag_config(
        "hashtag",
        foreground=WARNA_BIRU,
        font=("Times New Roman", 12, "bold")
    )


    # Pesan awal
    hasil_text.insert(
        tk.END,
        "Caption kamu akan muncul di sini... 💭",
        "isi"
    )

    hasil_text.config(
        state="disabled"
    )


    # =====================================================
    # FUNGSI GENERATE CAPTION
    # =====================================================

    def generate_caption():

        tema = input_tema.get().strip()


        if tema == "" or tema == "Masukkan tema...":

            messagebox.showwarning(
                "Oops! 😅",
                "Silakan masukkan tema terlebih dahulu."
            )

            return


        # Pembuka
        pembuka = [

            f"✨ Ada cerita menarik di balik {tema}!",

            f"🌟 Yuk, kenali lebih dekat tentang {tema}!",

            f"💫 Setiap momen punya cerita, termasuk tentang {tema}...",

            f"🔥 Saatnya membagikan cerita tentang {tema}!",

            f"📸 Sebuah momen, sebuah cerita, dan tentunya {tema}!",

            f"🌈 Pernah terpikir betapa menariknya {tema}?",

            f"🚀 Hari ini, mari kita berbicara tentang {tema}!",

            f"💖 Ada banyak hal menarik yang bisa ditemukan dari {tema}."

        ]


        # Isi
        isi = [

            (
                f"{tema} bukan hanya sekadar sesuatu yang kita lihat "
                f"atau nikmati, tetapi juga bisa menjadi bagian dari "
                f"pengalaman yang berkesan. Setiap proses memberikan "
                f"cerita baru dan setiap langkah membawa kita menuju "
                f"pengalaman yang berbeda."
            ),

            (
                f"Kadang, hal sederhana seperti {tema} bisa memberikan "
                f"makna yang lebih besar dari yang kita bayangkan. "
                f"Dari sebuah ide kecil, bisa muncul pengalaman, "
                f"inspirasi, dan cerita yang layak untuk dibagikan "
                f"kepada orang lain."
            ),

            (
                f"Di balik {tema}, selalu ada sesuatu yang menarik "
                f"untuk ditemukan. Mulai dari prosesnya, pengalaman "
                f"yang didapat, hingga cerita yang tercipta di "
                f"dalamnya. Karena pada akhirnya, perjalanan itulah "
                f"yang membuat sebuah momen menjadi lebih berarti."
            ),

            (
                f"Setiap orang memiliki cara sendiri dalam menikmati "
                f"{tema}. Ada yang melihatnya sebagai sebuah pengalaman, "
                f"ada juga yang menjadikannya sebagai sumber inspirasi. "
                f"Yang pasti, selalu ada cerita baru yang bisa kita "
                f"temukan di dalamnya."
            )

        ]


        # Penutup
        penutup = [

            "Jadi, jangan lewatkan momennya! 🚀",

            "Yuk, ciptakan cerita baru hari ini! ✨",

            "Karena setiap momen layak untuk dikenang. 📸💙",

            "Mari nikmati prosesnya dan buat cerita yang berkesan! 🌟",

            "Siap menciptakan pengalaman berikutnya? 🔥",

            "Jangan hanya melihat — jadilah bagian dari ceritanya! 💫",

            "Karena cerita terbaik dimulai dari sebuah langkah kecil. 🌈"

        ]


        # Hashtag
        hashtag = (
            f"\n\n#{tema.replace(' ', '')} "
            f"#CreativeMoment #Inspiration #Story"
        )


        # Pilih secara acak
        pembuka_pilihan = random.choice(pembuka)
        isi_pilihan = random.choice(isi)
        penutup_pilihan = random.choice(penutup)


        # Aktifkan text
        hasil_text.config(
            state="normal"
        )


        # Hapus hasil sebelumnya
        hasil_text.delete(
            "1.0",
            tk.END
        )


        # Masukkan pembuka
        hasil_text.insert(
            tk.END,
            pembuka_pilihan + "\n\n",
            "pembuka"
        )


        # Masukkan isi
        hasil_text.insert(
            tk.END,
            isi_pilihan + "\n\n",
            "isi"
        )


        # Masukkan penutup
        hasil_text.insert(
            tk.END,
            penutup_pilihan,
            "penutup"
        )


        # Masukkan hashtag
        hasil_text.insert(
            tk.END,
            hashtag,
            "hashtag"
        )


        # Kunci text
        hasil_text.config(
            state="disabled"
        )


    # =====================================================
    # TOMBOL GENERATE CAPTION
    # =====================================================

    tombol_generate = tk.Button(
        frame,
        text="✨ Generate Caption ✨",
        command=generate_caption,
        bg=WARNA_PINK,
        fg=WARNA_PUTIH,
        activebackground=WARNA_PINK_GELAP,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        width=25,
        height=2,
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_generate.pack(
        pady=8
    )


# =========================================================
# HALAMAN TAGLINE
# =========================================================

def halaman_tagline():

    hapus_halaman()
    buat_navbar()


    frame = tk.Frame(
        window,
        bg=WARNA_BG
    )

    frame.pack(
        fill="both",
        expand=True
    )


    # Judul
    judul = tk.Label(
        frame,
        text="💡 Tagline Generator",
        bg=WARNA_BG,
        fg=WARNA_BIRU,
        font=FONT_JUDUL
    )

    judul.pack(
        pady=(40, 5)
    )


    # Keterangan
    keterangan = tk.Label(
        frame,
        text="Buat tagline singkat, kreatif, dan mudah diingat! 🚀",
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=FONT_NORMAL
    )

    keterangan.pack(
        pady=5
    )


    # Label input
    label_input = tk.Label(
        frame,
        text="Masukkan tema yang ingin dibuat:",
        bg=WARNA_BG,
        fg=WARNA_TEXT,
        font=FONT_SUBJUDUL
    )

    label_input.pack(
        pady=(20, 5)
    )


    # Input tema
    input_tema = tk.Entry(
        frame,
        width=50,
        font=FONT_NORMAL,
        justify="center",
        relief="solid",
        bd=1
    )

    input_tema.pack(
        pady=5,
        ipady=7
    )

    input_tema.insert(
        0,
        "Masukkan tema..."
    )


    # =====================================================
    # FRAME HASIL TAGLINE
    # =====================================================

    frame_hasil = tk.Frame(
        frame,
        bg=WARNA_CARD_TAGLINE,
        highlightbackground=WARNA_BORDER_TAGLINE,
        highlightthickness=3
    )

    frame_hasil.pack(
        padx=50,
        pady=20,
        fill="x"
    )


    # Judul hasil
    judul_hasil = tk.Label(
        frame_hasil,
        text="💎 HASIL TAGLINE 💎",
        bg=WARNA_CARD_TAGLINE,
        fg=WARNA_BIRU,
        font=("Times New Roman", 16, "bold")
    )

    judul_hasil.pack(
        pady=(20, 10)
    )


    # Hasil tagline
    label_hasil = tk.Label(
        frame_hasil,
        text="Tagline kamu akan muncul di sini... 💭",
        bg=WARNA_CARD_TAGLINE,
        fg=WARNA_TEXT,
        wraplength=700,
        justify="center",
        font=("Times New Roman", 20, "bold"),
        padx=30,
        pady=30
    )

    label_hasil.pack(
        fill="x",
        padx=20,
        pady=10
    )


    # =====================================================
    # FUNGSI GENERATE TAGLINE
    # =====================================================

    def generate_tagline():

        tema = input_tema.get().strip()


        # Validasi
        if tema == "" or tema == "Masukkan tema...":

            messagebox.showwarning(
                "Oops! 😅",
                "Silakan masukkan tema terlebih dahulu."
            )

            return


        # Daftar tagline
        taglines = [

            f"✨ {tema} — ciptakan cerita, hadirkan makna!",

            f"🔥 {tema}! Lebih dari sekadar pengalaman.",

            f"🌟 Temukan cerita baru bersama {tema}!",

            f"💫 {tema} — karena setiap momen berarti.",

            f"🚀 Berawal dari {tema}, tercipta sebuah cerita!",

            f"📸 Rasakan momennya. Ceritakan kisahnya. {tema}!",

            f"🌈 {tema} — jadikan hari ini lebih berwarna!",

            f"⚡ Satu langkah, satu cerita, satu {tema}!",

            f"💙 {tema} untuk pengalaman yang tak terlupakan.",

            f"🔥 Jangan hanya melihat — rasakan {tema}!",

            f"🌟 {tema} — mulai dari sini, ciptakan sesuatu yang berarti!",

            f"✨ Temukan inspirasi baru bersama {tema}!"

        ]


        # Pilih tagline secara acak
        hasil = random.choice(
            taglines
        )


        # Tampilkan hasil
        label_hasil.config(
            text=hasil
        )


    # =====================================================
    # TOMBOL GENERATE TAGLINE
    # =====================================================

    tombol_generate = tk.Button(
        frame,
        text="💡 Generate Tagline 💡",
        command=generate_tagline,
        bg=WARNA_BIRU,
        fg=WARNA_PUTIH,
        activebackground=WARNA_BIRU_MUDA,
        activeforeground=WARNA_PUTIH,
        relief="flat",
        width=25,
        height=2,
        font=FONT_BUTTON,
        cursor="hand2"
    )

    tombol_generate.pack(
        pady=5
    )


# =========================================================
# MENJALANKAN PROGRAM
# =========================================================

halaman_utama()

window.mainloop()