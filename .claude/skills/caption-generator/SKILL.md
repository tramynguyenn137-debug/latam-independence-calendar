# SKILL: caption-generator

Sinh caption mạng xã hội song ngữ (English + Tiếng Việt) cho từng ngày quốc khánh Mỹ Latinh, dựa trên dữ liệu lịch sử của từng quốc gia.

## Khi nào dùng skill này

- Cần tạo nội dung bài đăng cho sự kiện quốc khánh LATAM
- Cần sinh caption theo format Twitter/Instagram/Facebook
- Cần tùy chỉnh giọng văn (celebratory, educational, formal)

---

## Cách thực thi

### Bước 1 — Đọc dữ liệu nguồn

Đọc từ một trong hai nguồn:
- `outputs/events_2026.json` — để lấy summary, description, _meta
- `.claude/skills/latam-independence-calendar/data/latam_countries.json` — để lấy thông tin gốc

Với mỗi quốc gia, trích xuất:
- `flag`, `country`, `country_vi`, `independence_date`, `year`, `from`, `from_vi`, `years` (tính theo 2026)

### Bước 2 — Sinh English caption

Format chuẩn (dưới 280 ký tự + hashtags):

```
{FLAG} Happy Independence Day, {COUNTRY}! 🎉
On {MONTH} {DAY}, {COUNTRY} celebrates {YEARS} years of independence
from {FROM} ({YEAR}). {UNIQUE_FACT}
#{COUNTRY_EN} #IndependenceDay #LatinAmerica #LATAM
```

**Quy tắc unique_fact**: mỗi quốc gia phải có 1 sự kiện/chi tiết lịch sử riêng biệt, không lặp lại giữa các nước.

### Bước 3 — Sinh Vietnamese caption

Format chuẩn:

```
{FLAG} Chúc mừng Quốc khánh {COUNTRY_VI}! 🎊
Ngày {DAY}/{MONTH}, {COUNTRY_VI} kỷ niệm {YEARS} năm độc lập khỏi {FROM_VI} ({YEAR}).
{UNIQUE_FACT_VI}
#{COUNTRY_HASHTAG} #QuocKhanh #MyLatinhh #LATAM
```

### Bước 4 — Kiểm tra chất lượng

Trước khi lưu, kiểm tra:
- Không có lỗi dấu tiếng Việt
- Main caption ≤ 280 ký tự (không tính hashtags)
- Mỗi caption có ít nhất 1 fact lịch sử cụ thể
- Hashtags ở dòng riêng

---

## Style guide

| Ngôn ngữ | Giọng văn | Đặc điểm |
|----------|-----------|----------|
| English | Enthusiastic, educational | Dùng dấu chấm than, facts cụ thể |
| Tiếng Việt | Ấm áp, trang trọng | Dùng dấu tiếng Việt đầy đủ, kính trọng |

---

## Templates tham chiếu

Xem thêm tại:
- `.claude/skills/latam-independence-calendar/templates/social_post_vi.md`
- `.claude/skills/latam-independence-calendar/templates/social_post_es.md`

---

## Output format

Mỗi quốc gia trả về object:
```json
{
  "country_code": "MX",
  "country": "Mexico",
  "date": "2026-09-16",
  "caption_en": "...",
  "caption_vi": "...",
  "hashtags_en": "#Mexico #IndependenceDay #LatinAmerica #LATAM",
  "hashtags_vi": "#Mexico #QuocKhanh #MyLatinhh #LATAM"
}
```
