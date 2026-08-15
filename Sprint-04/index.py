from pathlib import Path
import re, html

p = Path("itsenja_modern_javascript_async_fetch_api.html")
s = p.read_text(encoding="utf-8")

# Add a visual API flow + reference/playbook styling.
extra_css = r"""
<style>
.visual-api{display:flex;align-items:center;justify-content:center;gap:10px;flex-wrap:wrap;margin:18px 0}
.node{background:#fff;border:2px solid #cbd5e1;border-radius:14px;padding:14px 18px;text-align:center;min-width:130px;box-shadow:0 8px 24px rgba(26,39,67,.07)}
.node b{display:block;font-size:1rem}.node small{display:block;color:#667085;margin-top:4px}
.node.client{border-color:#60a5fa}.node.api{border-color:#818cf8}.node.server{border-color:#34d399}.node.data{border-color:#f59e0b}
.flow-arrow{font-size:1.3rem;font-weight:900;color:#2563eb}
.step-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:18px}
.step{background:#fff;border:1px solid #dbe2ec;border-radius:14px;padding:16px}.step strong{display:block;color:#2563eb;margin-bottom:6px}.step p{font-size:.95rem!important;margin:0}
.refgrid{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.ref{display:block;background:#fff;border:1px solid #dbe2ec;border-radius:14px;padding:16px;text-decoration:none;color:#172033}.ref:hover{border-color:#2563eb}.ref b{display:block;color:#2563eb}.ref small{color:#667085}
.quiz{display:grid;grid-template-columns:1fr 1fr;gap:14px}.q{background:#fff;border:1px solid #dbe2ec;border-radius:14px;padding:16px}.q b{display:block;margin-bottom:7px}.answer{display:none;margin-top:10px;padding:10px;border-radius:8px;background:#eef6ff;color:#334155}.q button{border:0;background:#2563eb;color:#fff;border-radius:8px;padding:7px 10px;cursor:pointer}
@media(max-width:900px){.step-grid,.refgrid,.quiz{grid-template-columns:1fr}}
</style>
"""
s = s.replace("</style></head>", extra_css + "</style></head>")

# Replace selected generic slides with more pedagogical versions.
def replace_by_badge(badge, new_section):
    global s
    pattern = rf'<section class="slide"><div class="badge">{re.escape(badge)}</div>.*?</section>'
    s, n = re.subn(pattern, new_section, s, count=1, flags=re.S)
    return n

replace_by_badge("API", '''<section class="slide"><div class="badge">API</div><h2>Apa itu <span class="blue">API?</span></h2>
<p class="lead"><b>Application Programming Interface</b> adalah aturan dan antarmuka yang memungkinkan aplikasi meminta atau mengirim data ke layanan lain.</p>
<div class="visual-api"><div class="node client"><b>Browser</b><small>Client</small></div><div class="flow-arrow">→ request →</div><div class="node api"><b>API</b><small>Endpoint</small></div><div class="flow-arrow">→</div><div class="node server"><b>Server</b><small>Process data</small></div><div class="flow-arrow">→ response →</div><div class="node data"><b>JSON</b><small>Data</small></div></div>
<div class="grid2"><div class="card"><h3>Analogi restoran</h3><p>Kamu sebagai pelanggan tidak masuk ke dapur. Kamu memberi pesanan kepada pelayan. Pelayan meneruskan pesanan dan mengembalikan hasilnya.</p></div><div class="card"><h3>Dalam web</h3><p>Frontend meminta data melalui API. Server memproses request lalu mengirim response. Frontend kemudian mengolah data tersebut menjadi UI.</p></div></div>
<div class="callout"><b>Intinya:</b> API adalah "jalur komunikasi". Endpoint adalah alamat yang kita hubungi, sedangkan response adalah jawaban dari server.</div></section>''')

replace_by_badge("API FLOW", '''<section class="slide"><div class="badge">API FLOW</div><h2>Bayangkan API seperti <span class="blue">percakapan.</span></h2>
<div class="step-grid"><div class="step"><strong>01 · Request</strong><p>Browser meminta data tertentu.</p></div><div class="step"><strong>02 · Server</strong><p>Server menerima dan memproses request.</p></div><div class="step"><strong>03 · Response</strong><p>Server mengembalikan status + data.</p></div><div class="step"><strong>04 · Render</strong><p>JavaScript mengubah data menjadi UI.</p></div></div>
<div class="visual-api"><div class="node client"><b>GET /users</b><small>Request</small></div><div class="flow-arrow">→</div><div class="node server"><b>API Server</b><small>Process</small></div><div class="flow-arrow">→</div><div class="node data"><b>200 + JSON</b><small>Response</small></div></div>
<pre class="code">GET https://jsonplaceholder.typicode.com/users

Response:
[
  { "id": 1, "name": "Leanne Graham" },
  { "id": 2, "name": "Ervin Howell" }
]</pre></section>''')

replace_by_badge("FETCH", '''<section class="slide"><div class="badge">FETCH</div><h2>Fetch API: membuat <span class="blue">HTTP request.</span></h2>
<p class="lead">Mulai dari bentuk paling sederhana. Jangan langsung menghafal full application.</p>
<pre class="code">fetch("https://jsonplaceholder.typicode.com/users");</pre>
<div class="step-grid"><div class="step"><strong>1</strong><p>URL menentukan endpoint.</p></div><div class="step"><strong>2</strong><p>fetch() memulai request.</p></div><div class="step"><strong>3</strong><p>Hasilnya adalah Promise.</p></div><div class="step"><strong>4</strong><p>Promise akan menghasilkan Response.</p></div></div>
<div class="callout">Coba jalankan baris tersebut di Console DevTools. Belum perlu DOM. Kita sedang mempelajari satu konsep pada satu waktu.</div></section>''')

replace_by_badge("PROMISE", '''<section class="slide"><div class="badge">PROMISE</div><h2>Promise = "hasilnya <span class="blue">nanti.</span>"</h2>
<p class="lead">Network request tidak selesai seketika. Promise memberi kita cara untuk menangani hasil yang datang kemudian.</p>
<div class="visual-api"><div class="node"><b>Pending</b><small>Masih menunggu</small></div><div class="flow-arrow">→</div><div class="node server"><b>Fulfilled</b><small>Berhasil</small></div></div>
<div class="visual-api"><div class="node"><b>Pending</b><small>Masih menunggu</small></div><div class="flow-arrow">→</div><div class="node data"><b>Rejected</b><small>Gagal</small></div></div>
<pre class="code">fetch(url)
  .then(response =&gt; response.json())
  .then(data =&gt; console.log(data))
  .catch(error =&gt; console.error(error));</pre>
<div class="callout"><b>Jangan takut dengan istilah Promise.</b> Untuk sekarang, pahami bahwa fetch memberikan hasil asynchronous yang perlu kita tunggu dan tangani.</div></section>''')

replace_by_badge("ASYNC AWAIT", '''<section class="slide"><div class="badge">ASYNC / AWAIT</div><h2>Promise menjadi lebih nyaman dengan <span class="blue">async/await.</span></h2>
<div class="grid2"><div class="card"><h3>Promise chaining</h3><pre class="code">fetch(url)
  .then(r =&gt; r.json())
  .then(data =&gt; {
    console.log(data);
  });</pre></div><div class="card"><h3>Async / Await</h3><pre class="code">async function getData() {
  const response = await fetch(url);
  const data = await response.json();

  console.log(data);
}</pre></div></div>
<div class="visual-api"><div class="node client"><b>async function</b><small>Function asynchronous</small></div><div class="flow-arrow">→</div><div class="node api"><b>await fetch()</b><small>Tunggu Promise</small></div><div class="flow-arrow">→</div><div class="node data"><b>data</b><small>Hasil siap dipakai</small></div></div>
<div class="callout"><span class="inline">await</span> tidak membuat network menjadi synchronous. Ia membuat cara menulis dan membaca alur asynchronous menjadi lebih mudah.</div></section>''')

replace_by_badge("RESPONSE", '''<section class="slide"><div class="badge">RESPONSE</div><h2>Response bukan langsung <span class="blue">data.</span></h2>
<pre class="code">const response = await fetch(url);

console.log(response.status);
console.log(response.ok);

const data = await response.json();

console.log(data);</pre>
<div class="step-grid"><div class="step"><strong>Response</strong><p>Object hasil fetch.</p></div><div class="step"><strong>status</strong><p>Contoh: 200, 404, 500.</p></div><div class="step"><strong>ok</strong><p>Menunjukkan response HTTP berhasil.</p></div><div class="step"><strong>json()</strong><p>Membaca body JSON menjadi data JavaScript.</p></div></div>
<div class="callout">Urutan penting: <b>Response → cek status → parse body → gunakan data.</b></div></section>''')

replace_by_badge("ERROR", '''<section class="slide"><div class="badge">ERROR</div><h2>Request bisa gagal. Gunakan <span class="blue">try/catch.</span></h2>
<pre class="code">async function getUsers() {
  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error("HTTP request failed");
    }

    const data = await response.json();
    console.log(data);

  } catch (error) {
    console.error(error);
  }
}</pre>
<div class="grid2"><div class="card"><h3>try</h3><p>Jalankan kode yang berpotensi gagal.</p></div><div class="card"><h3>catch</h3><p>Tangani error dan berikan feedback kepada pengguna.</p></div></div>
<div class="callout"><b>Catatan penting:</b> status HTTP 404/500 perlu diperiksa dengan <span class="inline">response.ok</span>; jangan hanya mengandalkan <span class="inline">catch</span>.</div></section>''')

replace_by_badge("UI STATES", '''<section class="slide"><div class="badge">UI STATES</div><h2>Jangan biarkan user melihat <span class="blue">layar kosong.</span></h2>
<div class="grid3"><div class="card"><h3>⏳ Loading</h3><p>Request sedang berjalan.</p><pre class="code">status.textContent = "Loading...";</pre></div><div class="card"><h3>✓ Success</h3><p>Data berhasil diterima.</p><pre class="code">status.textContent = "Success";</pre></div><div class="card"><h3>⚠ Error</h3><p>Request gagal.</p><pre class="code">status.textContent = "Failed";</pre></div></div>
<div class="callout">Ini adalah pola dasar aplikasi yang berkomunikasi dengan server: <b>Loading → Success / Error.</b></div></section>''')

# Insert a dedicated live full example before DEVTOOLS.
needle = '<section class="slide"><div class="badge">DEVTOOLS</div>'
live = '''<section class="slide"><div class="badge">LIVE FULL APP</div><h2>Full example: <span class="blue">API → JSON → DOM</span></h2>
<div class="playground"><div class="editor"><div class="tag">HTML</div><textarea class="html"><h2>User Directory</h2>
<p id="status">Klik tombol untuk mengambil data.</p>
<button id="load">Load Users</button>
<ul id="users"></ul></textarea><div class="tag">CSS</div><textarea class="css">body{font-family:Arial;padding:24px}
button{padding:10px 14px;border:0;border-radius:8px;background:#2563eb;color:white}
li{margin:9px 0;padding:9px;border:1px solid #ddd;border-radius:8px}</textarea><div class="tag">JavaScript</div><textarea class="js">const load = document.querySelector("#load");
const status = document.querySelector("#status");
const users = document.querySelector("#users");

load.addEventListener("click", async () => {
  status.textContent = "Loading...";

  try {
    const response = await fetch(
      "https://jsonplaceholder.typicode.com/users"
    );

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }

    const data = await response.json();

    users.innerHTML = "";

    data.forEach(user => {
      const li = document.createElement("li");
      li.textContent = `${user.name} — ${user.email}`;
      users.appendChild(li);
    });

    status.textContent = "Data berhasil dimuat.";

  } catch (error) {
    status.textContent = "Gagal mengambil data.";
    console.error(error);
  }
});</textarea><button class="run">▶ Jalankan</button></div><div class="output"><div class="outhead">LIVE OUTPUT · CLICK LOAD USERS</div><iframe></iframe></div></div>
<div class="callout"><b>Mentor flow:</b> jalankan → lihat hasil → buka Network → klik request → lihat status → lihat Response → kembali ke kode → ubah satu bagian → jalankan lagi.</div></section>'''
s = s.replace(needle, live + needle, 1)

# Add a visual debugging slide after DEVTOOLS.
needle2 = '<section class="slide"><div class="badge">CHALLENGE 01</div>'
debug = '''<section class="slide"><div class="badge">DEBUG PLAYBOOK</div><h2>Kalau Fetch error, <span class="blue">jangan menebak.</span></h2>
<div class="step-grid"><div class="step"><strong>01 · URL</strong><p>Endpoint benar? Ada typo?</p></div><div class="step"><strong>02 · Network</strong><p>Request benar-benar terkirim?</p></div><div class="step"><strong>03 · Status</strong><p>200, 404, 500, atau lainnya?</p></div><div class="step"><strong>04 · Response</strong><p>Apakah body sesuai harapan?</p></div></div>
<div class="visual-api"><div class="node client"><b>Request</b><small>URL + method</small></div><div class="flow-arrow">→</div><div class="node api"><b>Status</b><small>200 / 404 / 500</small></div><div class="flow-arrow">→</div><div class="node server"><b>Response</b><small>JSON?</small></div><div class="flow-arrow">→</div><div class="node data"><b>DOM</b><small>Render?</small></div></div>
<div class="callout">Biasakan debugging berdasarkan bukti dari <b>Console dan Network</b>, bukan hanya mencoba-coba baris kode.</div></section>'''
s = s.replace(needle2, debug + needle2, 1)

# Add reference/playbook slide before NEXT.
needle3 = '<section class="slide"><div class="badge">NEXT</div>'
refs = '''<section class="slide"><div class="badge">PLAYBOOK</div><h2>API & Async <span class="blue">Playbook.</span></h2>
<p class="lead">Gunakan ini setelah sesi. Jangan menghafal semuanya; kembali ke bagian yang sedang kamu butuhkan.</p>
<div class="refgrid">
<a class="ref" href="https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch" target="_blank"><b>MDN · Using Fetch</b><small>Fetch, response, status, JSON, error handling</small></a>
<a class="ref" href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function" target="_blank"><b>MDN · async function</b><small>Konsep async function dan Promise</small></a>
<a class="ref" href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS/Promises" target="_blank"><b>MDN · Promises</b><small>Dasar asynchronous JavaScript</small></a>
<a class="ref" href="https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/JSON" target="_blank"><b>MDN · JSON</b><small>Object, array, dan pertukaran data JSON</small></a>
<a class="ref" href="https://jsonplaceholder.typicode.com/" target="_blank"><b>JSONPlaceholder</b><small>Fake REST API untuk latihan GET</small></a>
<a class="ref" href="https://developer.chrome.com/docs/devtools/network/" target="_blank"><b>Chrome DevTools · Network</b><small>Melihat request, response, status, dan timing</small></a>
</div>
<div class="callout"><b>Playbook inti:</b> API → HTTP → JSON → fetch → Promise → async/await → response.ok → response.json() → try/catch → DOM → DevTools.</div></section>'''
s = s.replace(needle3, refs + needle3, 1)

# Add interactive quick-check slide before PLAYBOOK.
quiz = '''<section class="slide"><div class="badge">QUICK CHECK</div><h2>Sudah paham? <span class="blue">Uji diri.</span></h2>
<div class="quiz">
<div class="q"><b>1. fetch() mengembalikan apa?</b><button onclick="this.nextElementSibling.style.display='block'">Lihat jawaban</button><div class="answer">Promise yang akan menghasilkan Response.</div></div>
<div class="q"><b>2. Kenapa response.json() diperlukan?</b><button onclick="this.nextElementSibling.style.display='block'">Lihat jawaban</button><div class="answer">Untuk membaca body JSON dan mengubahnya menjadi data JavaScript.</div></div>
<div class="q"><b>3. Apakah 404 otomatis masuk catch?</b><button onclick="this.nextElementSibling.style.display='block'">Lihat jawaban</button><div class="answer">Tidak. Periksa response.ok/status dan lempar error jika diperlukan.</div></div>
<div class="q"><b>4. Setelah data didapat, lalu apa?</b><button onclick="this.nextElementSibling.style.display='block'">Lihat jawaban</button><div class="answer">Proses data lalu render ke DOM sesuai kebutuhan UI.</div></div>
</div></section>'''
s = s.replace(needle3, quiz + refs + needle3, 1)

# Update total counter dynamically; existing JS does it based on slides.
s = re.sub(r'<div class="counter" id="counter">01 / 24</div>', '<div class="counter" id="counter">01 / 30</div>', s)

out = Path("itsenja_modern_javascript_async_fetch_api_interactive.html")
out.write_text(s, encoding="utf-8")
print(out)
