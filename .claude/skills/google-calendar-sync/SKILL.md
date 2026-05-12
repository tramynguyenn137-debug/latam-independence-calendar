# SKILL: google-calendar-sync

Tạo sự kiện Google Calendar từ danh sách events đã parse, xử lý lỗi, và tạo báo cáo kết quả.

## Khi nào dùng skill này

- Cần push một loạt sự kiện lên Google Calendar
- Cần kiểm tra sự kiện đã tồn tại trước khi tạo
- Cần ghi log kết quả tạo sự kiện (thành công / thất bại)

---

## Cách thực thi

### Bước 1 — Xác thực Google Calendar

Gọi `mcp__claude_ai_Google_Calendar__list_calendars` để kiểm tra kết nối.
Nếu chưa xác thực, tiến hành authentication flow trước.

### Bước 2 — Tạo từng sự kiện

Với mỗi event trong danh sách, gọi `mcp__claude_ai_Google_Calendar__create_event` với payload:

```json
{
  "summary": "<event.summary>",
  "description": "<event.description>",
  "start": { "date": "<YYYY-MM-DD>" },
  "end":   { "date": "<YYYY-MM-DD>" },
  "reminders": { "useDefault": false, "overrides": [...] },
  "colorId": "11"
}
```

**Lưu ý**: Google Calendar API yêu cầu định dạng ISO 8601 (`YYYY-MM-DDTHH:MM:SS`) cho một số trường hợp — dùng `T00:00:00` nếu date-only bị từ chối.

### Bước 3 — Xử lý lỗi

- Nếu sự kiện đã tồn tại (trùng summary + tháng): log cảnh báo, bỏ qua
- Nếu API trả lỗi: log lỗi, tiếp tục xử lý event tiếp theo
- Không dừng toàn bộ vì 1 event thất bại

### Bước 4 — Tạo báo cáo

Lưu báo cáo ra `outputs/calendar_creation_report.md`:

```markdown
# Calendar Creation Report — YYYY-MM-DD

## Tổng kết
- Tổng sự kiện xử lý: X
- Thành công: X
- Thất bại: X

## Sự kiện đã tạo
| # | Quốc gia | Ngày | Trạng thái |
|---|----------|------|------------|
| 1 | 🇲🇽 Mexico | 2026-09-16 | ✅ |
...

## Lỗi (nếu có)
...
```

---

## MCP Tools dùng

| Tool | Mục đích |
|------|---------|
| `mcp__claude_ai_Google_Calendar__list_calendars` | Xác thực kết nối |
| `mcp__claude_ai_Google_Calendar__create_event` | Tạo sự kiện |
| `mcp__claude_ai_Google_Calendar__list_events` | Kiểm tra trùng lặp |

---

## Files liên quan

```
outputs/events_2026.json              ← input (từ event-data-parser)
outputs/calendar_creation_report.md  ← output báo cáo
```
