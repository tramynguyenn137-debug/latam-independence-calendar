# SKILL: latam-independence-calendar

Tạo sự kiện nhắc nhở trên Google Calendar cho ngày quốc khánh các nước Mỹ Latinh, kèm gợi ý nội dung bài đăng mạng xã hội.

## Khi nào dùng skill này

- Người dùng muốn tạo reminder quốc khánh LATAM trên Google Calendar
- Người dùng hỏi "quốc khánh nước X là ngày mấy"
- Người dùng muốn chuẩn bị nội dung social media cho dịp quốc khánh LATAM

---

## Cách thực thi

### Bước 1 — Xác định yêu cầu

Hỏi người dùng (nếu chưa rõ):
- Muốn tạo cho **tất cả** 20 nước hay **một nước cụ thể**?
- Năm nào? (mặc định: năm hiện tại)
- Ngôn ngữ bài đăng: Tiếng Việt hay Tiếng Tây Ban Nha?

### Bước 2 — Đọc dữ liệu

Đọc file `data/latam_countries.json` để lấy danh sách quốc gia, ngày độc lập, và cấu hình reminder.

### Bước 3 — Tạo preview sự kiện

Hiển thị danh sách các sự kiện sẽ tạo (tên nước, ngày, số năm kỷ niệm) để người dùng xác nhận trước khi push lên Google Calendar.

Format preview:
```
🗓️ SỰ KIỆN SẼ TẠO (năm YYYY)
──────────────────────────────
🇲🇽 09-16 | Quốc khánh Mexico (215 năm) | Nhắc: 7, 3, 1 ngày trước
🇧🇷 09-07 | Quốc khánh Brazil (204 năm)  | Nhắc: 7, 3, 1 ngày trước
...
Tổng: X sự kiện. Xác nhận tạo? (y/n)
```

### Bước 4 — Xác thực Google Calendar

Gọi MCP tool `mcp__claude_ai_Google_Calendar__authenticate` nếu chưa đăng nhập.

### Bước 5 — Tạo sự kiện trên Google Calendar

Với mỗi quốc gia, tạo 1 sự kiện all-day với:
- **Summary**: `{FLAG} Quốc khánh {TÊN NƯỚC} ({SỐ NĂM} năm)`
- **Description**: Tên nước, năm độc lập, tên nước thực dân, link template bài đăng
- **Date**: ngày quốc khánh của năm được chọn
- **Reminders**: popup 7 ngày trước, 3 ngày trước, 1 ngày trước
- **Color**: Xanh lá (colorId: "11" — Sage)

### Bước 6 — Gợi ý bài đăng

Sau khi tạo xong, hỏi người dùng có muốn xem template bài đăng không.
Nếu có, đọc file template phù hợp và điền thông tin nước được chọn.

---

## Dữ liệu & Files liên quan

```
latam-independence-calendar/
├── SKILL.md                          ← file này
├── data/
│   └── latam_countries.json          ← 20 nước LATAM + ngày quốc khánh
├── templates/
│   ├── social_post_vi.md             ← template bài đăng tiếng Việt
│   └── social_post_es.md             ← template bài đăng tiếng Tây Ban Nha
├── scripts/
│   └── generate_events.py            ← script tạo file JSON events offline
└── output/
    └── events_YYYY.json              ← events đã generate (tạo khi chạy script)
```

---

## Danh sách 20 nước LATAM (tóm tắt)

| Nước | Ngày | Năm |
|------|------|-----|
| Haiti | 01-01 | 1804 |
| Cộng hoà Dominica | 02-27 | 1844 |
| Paraguay | 05-14 | 1811 |
| Venezuela | 07-05 | 1811 |
| Argentina | 07-09 | 1816 |
| Colombia | 07-20 | 1810 |
| Peru | 07-28 | 1821 |
| Bolivia | 08-06 | 1825 |
| Ecuador | 08-10 | 1809 |
| Uruguay | 08-25 | 1825 |
| Brazil | 09-07 | 1822 |
| Guatemala / Honduras / El Salvador / Nicaragua / Costa Rica | 09-15 | 1821 |
| Mexico | 09-16 | 1810 |
| Chile | 09-18 | 1810 |
| Cuba | 05-20 | 1902 |
| Panama | 11-03 | 1903 |

---

## Lưu ý

- Luôn **preview** danh sách sự kiện trước khi gọi API tạo sự kiện
- Nếu sự kiện đã tồn tại trong tháng đó (trùng summary), hỏi người dùng có muốn ghi đè không
- Reminder tính bằng phút: 7 ngày = 10080 phút, 3 ngày = 4320 phút, 1 ngày = 1440 phút
