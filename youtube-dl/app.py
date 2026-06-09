from flask import Flask, request, send_file, render_template_string
import yt_dlp
import os

app = Flask(__name__)
DOWNLOAD_DIR = '/downloads'

HTML = '''<!DOCTYPE html>
<html>
<head>
    <title>YouTube to MP3</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 100px auto; padding: 20px; background: #1a1a1a; color: #fff; }
        h1 { color: #ff4444; }
        input { width: 100%; padding: 12px; margin: 10px 0; background: #333; border: 1px solid #555; color: #fff; border-radius: 5px; font-size: 16px; }
        button { width: 100%; padding: 12px; background: #ff4444; color: white; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; }
        button:hover { background: #cc0000; }
        #status { margin-top: 20px; padding: 10px; background: #333; border-radius: 5px; display: none; }
        #thumbnail { margin-top: 20px; display: none; border-radius: 10px; width: 100%; }
        .success { color: #44ff44; }
        .error { color: #ff4444; }
    </style>
</head>
<body>
    <h1>YouTube to MP3</h1>
    <input type="text" id="url" placeholder="Paste YouTube URL here..." />
    <button onclick="dlmp3()">Download MP3</button>
    <div id="status"></div>
    <img id="thumbnail" />
    <script>
        async function dlmp3() {
            const url = document.getElementById("url").value;
            const status = document.getElementById("status");
            const thumb = document.getElementById("thumbnail");
            status.style.display = "block";
            status.className = "";
            status.innerHTML = "Downloading... please wait";
            thumb.style.display = "none";
            const response = await fetch("/download", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({url: url})
            });
            if (response.ok) {
                const blob = await response.blob();
                const a = document.createElement("a");
                a.href = URL.createObjectURL(blob);
                a.download = "audio.mp3";
                a.click();
                status.className = "success";
                status.innerHTML = "Download complete!";
            } else {
                const data = await response.json();
                status.className = "error";
                status.innerHTML = "Error: " + data.error;
            }
        }

        document.getElementById("url").addEventListener("input", async function() {
            const url = this.value;
            if (url.includes("youtube.com/watch") || url.includes("youtu.be/")) {
                const videoId = url.match(/(?:v=|youtu\.be\/)([^&]+)/);
                if (videoId) {
                    const thumb = document.getElementById("thumbnail");
                    thumb.src = "https://img.youtube.com/vi/" + videoId[1] + "/maxresdefault.jpg";
                    thumb.style.display = "block";
                }
            }
        });
    </script>
</body>
</html>'''

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/download", methods=["POST"])
def download():
    data = request.json
    url = data.get("url")
    if not url:
        return {"error": "No URL provided"}, 400
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "noplaylist": True,
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                    "add_metadata": True,
                },
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            if info is None:
                return {"error": "Could not extract video info"}, 400
            if "entries" in info:
                info = info["entries"][0]
            title = info.get("title", "audio")
            title = "".join(c for c in title if c.isalnum() or c in (" ", "-", "_")).strip()
            filename = f"{title}.mp3"
            filepath = f"{DOWNLOAD_DIR}/{filename}"
            if not os.path.exists(filepath):
                files = sorted([f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".mp3")])
                if files:
                    filepath = f"{DOWNLOAD_DIR}/{files[-1]}"
                    filename = files[-1]
        resp = send_file(filepath, as_attachment=True, download_name=filename)
        return resp
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
