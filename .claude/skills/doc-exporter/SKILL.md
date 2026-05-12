# SKILL: doc-exporter

Tổ chức và lưu nội dung đã tạo thành các file Markdown có cấu trúc, bao gồm file riêng từng quốc gia, file tổng hợp, và index README.

## Khi nào dùng skill này

- Cần lưu captions/nội dung ra file markdown có cấu trúc
- Cần tạo index/table of contents tự động
- Cần tổ chức output theo thứ tự thời gian hoặc alphabetical

---

## Cách thực thi

### Bước 1 — Tạo thư mục output

Đảm bảo thư mục `docs/captions/` tồn tại. Dùng PowerShell nếu cần:
```powershell
New-Item -ItemType Directory -Force -Path "docs\captions"
```

### Bước 2 — Lưu file từng quốc gia

Với mỗi quốc gia, tạo file `docs/captions/[CODE]-[country-name].md`:

```markdown
# {FLAG} {COUNTRY} Independence Day — {MONTH} {DAY}, {YEAR_CELEBRATION}

## English Caption
{caption_en}

{hashtags_en}

## Vietnamese Caption
{caption_vi}

{hashtags_vi}

## Event Details
- **Date**: {MONTH} {DAY}, 2026
- **Years of independence**: {YEARS}
- **Independence from**: {FROM}
- **Year of independence**: {YEAR}
```

**Quy tắc đặt tên file**: `[ISO_CODE]-[country-name-lowercase-hyphenated].md`
Ví dụ: `MX-mexico.md`, `BR-brazil.md`, `CR-costa-rica.md`

### Bước 3 — Lưu file tổng hợp

Tạo `docs/captions/ALL-CAPTIONS-2026.md` theo thứ tự thời gian:

```markdown
# 🌎 Latin America Independence Days 2026 — All Captions

> Generated: {DATE} | Total countries: 20

---

## January
### 🇭🇹 Haiti — January 1
...

## February
...
```

### Bước 4 — Tạo README index

Tạo `docs/captions/README.md` với bảng tóm tắt:

```markdown
# Captions Index — Latin America Independence Days 2026

| # | Country | Date | Years | File |
|---|---------|------|-------|------|
| 1 | 🇭🇹 Haiti | Jan 1 | 222 | [HT-haiti.md](HT-haiti.md) |
...

## Stats
- Total countries: 20
- Languages: English, Vietnamese
- Generated: {DATE}
```

---

## Quy tắc đặt tên file

| Country | Code | Filename |
|---------|------|----------|
| Costa Rica | CR | `CR-costa-rica.md` |
| El Salvador | SV | `SV-el-salvador.md` |
| Dominican Republic | DO | `DO-dominican-republic.md` |

---

## Files output

```
docs/captions/
├── README.md                    ← index + table of contents
├── ALL-CAPTIONS-2026.md         ← tất cả 20 nước, thứ tự thời gian
├── HT-haiti.md
├── DO-dominican-republic.md
├── PY-paraguay.md
├── CU-cuba.md
├── VE-venezuela.md
├── AR-argentina.md
├── CO-colombia.md
├── PE-peru.md
├── BO-bolivia.md
├── EC-ecuador.md
├── UY-uruguay.md
├── BR-brazil.md
├── GT-guatemala.md
├── HN-honduras.md
├── SV-el-salvador.md
├── NI-nicaragua.md
├── CR-costa-rica.md
├── MX-mexico.md
├── CL-chile.md
└── PA-panama.md
```
