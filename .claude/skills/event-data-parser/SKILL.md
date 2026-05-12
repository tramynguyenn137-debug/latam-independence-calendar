# SKILL: event-data-parser

Đọc, validate, và chuẩn hóa dữ liệu sự kiện từ file JSON ngày quốc khánh LATAM trước khi chuyển sang bước xử lý tiếp theo.

## Khi nào dùng skill này

- Cần load dữ liệu sự kiện từ `outputs/events_2026.json` hoặc `data/latam_countries.json`
- Cần lọc sự kiện theo tháng, quốc gia, hoặc khoảng thời gian
- Cần validate cấu trúc JSON trước khi gọi API

---

## Cách thực thi

### Bước 1 — Đọc file JSON

Đọc file nguồn bằng Read tool:
- **events_2026.json**: danh sách sự kiện đã format sẵn cho Google Calendar
- **latam_countries.json**: dữ liệu gốc 20 nước LATAM

### Bước 2 — Validate cấu trúc

Với mỗi event trong mảng JSON, kiểm tra các trường bắt buộc:
```
required fields: summary, start.date, end.date, reminders.overrides
optional fields: description, colorId, _meta
```

Log ra bất kỳ record nào thiếu trường bắt buộc.

### Bước 3 — Chuẩn hóa dữ liệu

- Đảm bảo định dạng ngày là `YYYY-MM-DD`
- Chuyển `reminder_days_before` sang phút nếu cần: `days × 1440`
- Trích xuất `_meta` fields: `country`, `country_vi`, `years`

### Bước 4 — Trả về dữ liệu đã parse

Trả về mảng events hợp lệ để agent sử dụng ở bước tiếp theo.

---

## Schema tham chiếu

```json
{
  "summary": "🇲🇽 Quốc khánh Mexico (216 năm)",
  "description": "...",
  "start": { "date": "2026-09-16" },
  "end":   { "date": "2026-09-17" },
  "reminders": {
    "useDefault": false,
    "overrides": [
      { "method": "popup", "minutes": 10080 },
      { "method": "popup", "minutes": 4320  },
      { "method": "popup", "minutes": 1440  }
    ]
  },
  "colorId": "11",
  "_meta": {
    "country": "Mexico",
    "country_vi": "Mexico",
    "independence_date": "09-16",
    "years": 216
  }
}
```

---

## Files liên quan

```
outputs/events_2026.json          ← input chính
.claude/skills/latam-independence-calendar/data/latam_countries.json  ← input gốc
```
