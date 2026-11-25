# u-deysumbrella-the-3am-fridge-text-4c3e721d — "The Midnight Light" — NOTES

- Kompetisi: The 3AM Fridge Text (Growth, pot $2, juara 1 saja $2)
- Deadline entries: 25 Nov 2026 13:45 UTC (20:45 WIB). Buka 25 Nov 2026 00:46:15 UTC.
- Akun: make.fun mihawnk-50569; GitHub mihawnk-nft

## Entry (preview — BELUM SUBMIT)
> It's 3am. You've opened me four times tonight and eaten nothing. I'm starting to think you just like my light.

110 karakter, 1 baris, UTF-8. Strategi vs brief juri (kriteria berurutan):
1) jelas pesan teks kulkas pintar ke pemiliknya jam 3 pagi; 2) tawa besar yang
relatable — buka kulkas tengah malam berkali-kali tanpa makan apa-apa — layak
screenshot; 3) suara mesin kecil yang beropini ("I'm starting to think you just
like my light"); 4) satu baris lengkap, terbaca di lock screen; 5) segar — tanpa
klise susu/es/pintu dibiarkan terbuka.

## Entry
- Repo: https://github.com/mihawnk-nft/u-deysumbrella-the-3am-fridge-text-4c3e721d
  public, dibuat 2026-11-25T00:55:57Z (setelah buka 00:46:15Z), topik makefun + make-fun,
  homepage bounty.
- Commit: 2806326a093f8153ecfacf814da26de37d342f0e (HEAD GitHub sama; 4 file:
  main.py, README.md, LICENSE MIT, NOTES.md) — terverifikasi via gh api.
- Dev: ~/workspace/makefun/u-deysumbrella-the-3am-fridge-text-4c3e721d-dev/
- Kit: ~/workspace/makefun/u-deysumbrella-the-3am-fridge-text-4c3e721d-kit/u-deysumbrella-the-3am-fridge-text-4c3e721d-kit/
- main.py: Python stdlib murni, tulis LINE ke /output/entry.txt (override MAKEFUN_OUTPUT_DIR buat tes).
  Tes lokal: 2x run byte-identik, 110 chars, 1 baris, gate mirror (1–140, non-whitespace) lolos.

## Check lokal (sebelum submit): 4 passed, 1 failed, 14 skipped, 5 checked at submission
- Lolos: competition_open, snapshot (4 file, 5.343 byte), license_osi (MIT),
  entrypoint (main.py → python3.13).
- Gagal: transcripts_present — bundle transcripts DIBUAT PARENT setelah run
  subagent selesai (seperti entry yuki-kato); jalankan check ulang dengan
  --transcripts sesudah bundle ada.
- 5 dicek saat submit — semua sudah terpenuhi dari sisi repo (public, owner
  mihawnk-nft, dibuat setelah buka, commit ter-push, karya sendiri).

## STATUS: BERHENTI DI PREVIEW — TIDAK SUBMIT, TIDAK CLAIM
Submit butuh lampu hijau eksplisit user di chat + keypair ~/.makefun/keypairs/https_make.fun.json.
Perintah submit (nanti, oleh parent agent, setelah bundle transcripts dibuat):
  dari dir kit,
  node cli/makefun.mjs submit --competition u-deysumbrella-the-3am-fridge-text-4c3e721d --repo-url https://github.com/mihawnk-nft/u-deysumbrella-the-3am-fridge-text-4c3e721d --commit 2806326a093f8153ecfacf814da26de37d342f0e --title "The Midnight Light" --bundle transcripts.tar.gz --keypair ~/.makefun/keypairs/https_make.fun.json
