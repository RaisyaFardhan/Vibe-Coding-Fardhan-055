from __future__ import annotations

import random

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

caption_openers = [
    lambda theme: f"✨ Ada cerita menarik di balik {theme}!",
    lambda theme: f"🌟 Yuk, kenali lebih dekat tentang {theme}!",
    lambda theme: f"💫 Setiap momen punya cerita, termasuk tentang {theme}...",
    lambda theme: f"🔥 Saatnya membagikan cerita tentang {theme}!",
    lambda theme: f"📸 Sebuah momen, sebuah cerita, dan tentunya {theme}!",
    lambda theme: f"🌈 Pernah terpikir betapa menariknya {theme}?",
    lambda theme: f"🚀 Hari ini, mari kita berbicara tentang {theme}!",
    lambda theme: f"💖 Ada banyak hal menarik yang bisa ditemukan dari {theme}.",
]

caption_bodies = [
    lambda theme: (
        f"{theme} bukan hanya sekadar sesuatu yang kita lihat atau nikmati, tetapi juga bisa menjadi bagian dari "
        "pengalaman yang berkesan. Setiap proses memberikan cerita baru dan setiap langkah membawa kita menuju "
        "pengalaman yang berbeda."
    ),
    lambda theme: (
        f"Kadang, hal sederhana seperti {theme} bisa memberikan makna yang lebih besar dari yang kita bayangkan. "
        "Dari sebuah ide kecil, bisa muncul pengalaman, inspirasi, dan cerita yang layak untuk dibagikan kepada orang lain."
    ),
    lambda theme: (
        f"Di balik {theme}, selalu ada sesuatu yang menarik untuk ditemukan. Mulai dari prosesnya, pengalaman yang didapat, "
        "hingga cerita yang tercipta di dalamnya. Karena pada akhirnya, perjalanan itulah yang membuat sebuah momen menjadi lebih berarti."
    ),
    lambda theme: (
        f"Setiap orang memiliki cara sendiri dalam menikmati {theme}. Ada yang melihatnya sebagai sebuah pengalaman, ada juga "
        "yang menjadikannya sebagai sumber inspirasi. Yang pasti, selalu ada cerita baru yang bisa kita temukan di dalamnya."
    ),
]

caption_closers = [
    "Jadi, jangan lewatkan momennya! 🚀",
    "Yuk, ciptakan cerita baru hari ini! ✨",
    "Karena setiap momen layak untuk dikenang. 📸💙",
    "Mari nikmati prosesnya dan buat cerita yang berkesan! 🌟",
    "Siap menciptakan pengalaman berikutnya? 🔥",
    "Jangan hanya melihat, jadilah bagian dari ceritanya! 💫",
    "Karena cerita terbaik dimulai dari sebuah langkah kecil. 🌈",
]

tagline_templates = [
    lambda theme: f"✨ {theme} — ciptakan cerita, hadirkan makna!",
    lambda theme: f"🔥 {theme}! Lebih dari sekadar pengalaman.",
    lambda theme: f"🌟 Temukan cerita baru bersama {theme}!",
    lambda theme: f"💫 {theme} — karena setiap momen berarti.",
    lambda theme: f"🚀 Berawal dari {theme}, tercipta sebuah cerita!",
    lambda theme: f"📸 Rasakan momennya. Ceritakan kisahnya. {theme}!",
    lambda theme: f"🌈 {theme} — jadikan hari ini lebih berwarna!",
    lambda theme: f"⚡ Satu langkah, satu cerita, satu {theme}!",
    lambda theme: f"💙 {theme} untuk pengalaman yang tak terlupakan.",
    lambda theme: f"🔥 Jangan hanya melihat — rasakan {theme}!",
    lambda theme: f"🌟 {theme} — mulai dari sini, ciptakan sesuatu yang berarti!",
    lambda theme: f"✨ Temukan inspirasi baru bersama {theme}!",
]


def generate_caption(theme: str) -> str:
    hashtag_theme = "".join(theme.split())
    opener = random.choice(caption_openers)(theme)
    body = random.choice(caption_bodies)(theme)
    closer = random.choice(caption_closers)
    return f"{opener}\n\n{body}\n\n{closer}\n\n#{hashtag_theme} #CreativeMoment #Inspiration #Story"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    payload = request.get_json(silent=True) or {}
    theme = (payload.get("theme") or "").strip()
    mode = (payload.get("mode") or "caption").lower()

    if not theme:
        return jsonify({"error": "Masukkan tema terlebih dahulu."}), 400

    if mode == "tagline":
        text = random.choice(tagline_templates)(theme)
    else:
        text = generate_caption(theme)

    return jsonify({"text": text, "mode": mode})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
