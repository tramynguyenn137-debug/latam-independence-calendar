# Personal Workspace — Claude Code Skills & Agents

Không gian làm việc cá nhân với các Claude Code skills và multi-agent workflows tùy chỉnh.

---

## Multi-Agent System: Latin America Independence Days 2026

Hệ thống tự động gồm 2 sub-agents chạy song song để:
1. Tạo sự kiện nhắc nhở trên **Google Calendar** cho 20 ngày quốc khánh LATAM
2. Sinh **captions mạng xã hội** song ngữ (EN + VI) và lưu ra docs

### Sơ đồ kiến trúc

```
Claude Code (Orchestrator)
│
├── Sub-Agent 1: calendar-creator
│   ├── Skill: event-data-parser      → Đọc & validate JSON events
│   ├── Skill: google-calendar-sync   → Tạo events trên Google Calendar
│   └── Output: outputs/calendar_creation_report.md
│
└── Sub-Agent 2: content-writer
    ├── Skill: caption-generator      → Sinh captions EN + VI
    ├── Skill: doc-exporter           → Lưu ra Markdown docs
    └── Output: docs/captions/ (23 files)
```

### Luồng dữ liệu

```
latam_countries.json
        │
        ▼
generate_events.py
        │
        ▼
outputs/events_2026.json ──────────────────────┐
        │                                       │
        ▼                                       ▼
[calendar-creator]                    [content-writer]
  → 20 Google Calendar events           → docs/captions/
  → Reminders: 7, 3, 1 ngày trước         ├── ALL-CAPTIONS-2026.md
                                           ├── README.md
                                           └── [CODE]-[country].md ×20
```

---

## Agents

| Agent | File | Mô tả |
|-------|------|-------|
| `calendar-creator` | [`.claude/agents/calendar-creator.md`](.claude/agents/calendar-creator.md) | Tạo Google Calendar events với reminders |
| `content-writer` | [`.claude/agents/content-writer.md`](.claude/agents/content-writer.md) | Sinh captions & lưu docs |

---

## Skills

| Skill | File | Dùng bởi |
|-------|------|---------|
| `latam-independence-calendar` | [`.claude/skills/latam-independence-calendar/SKILL.md`](.claude/skills/latam-independence-calendar/SKILL.md) | Orchestrator (skill gốc) |
| `event-data-parser` | [`.claude/skills/event-data-parser/SKILL.md`](.claude/skills/event-data-parser/SKILL.md) | `calendar-creator` |
| `google-calendar-sync` | [`.claude/skills/google-calendar-sync/SKILL.md`](.claude/skills/google-calendar-sync/SKILL.md) | `calendar-creator` |
| `caption-generator` | [`.claude/skills/caption-generator/SKILL.md`](.claude/skills/caption-generator/SKILL.md) | `content-writer` |
| `doc-exporter` | [`.claude/skills/doc-exporter/SKILL.md`](.claude/skills/doc-exporter/SKILL.md) | `content-writer` |

---

## Cách dùng

Trong Claude Code, gọi hệ thống bằng chat tự nhiên:

> "Tạo reminder quốc khánh các nước Mỹ Latinh năm 2026 trên Google Calendar và viết captions cho từng nước"

Claude sẽ tự phân bổ công việc cho 2 sub-agents chạy song song.

Hoặc chạy từng agent riêng:
> "Dùng calendar-creator để tạo events cho tháng 9"
> "Dùng content-writer để viết caption cho Mexico"

---

## Cấu trúc thư mục

```
C:\Users\Admin\CLAUDE-CODE\
├── .claude/
│   ├── agents/
│   │   ├── calendar-creator.md
│   │   └── content-writer.md
│   └── skills/
│       ├── latam-independence-calendar/   ← skill gốc
│       ├── event-data-parser/
│       ├── google-calendar-sync/
│       ├── caption-generator/
│       └── doc-exporter/
├── docs/
│   └── captions/                          ← output của content-writer
│       ├── README.md
│       ├── ALL-CAPTIONS-2026.md
│       └── [CODE]-[country].md ×20
├── outputs/
│   ├── events_2026.json                   ← dữ liệu sự kiện
│   └── calendar_creation_report.md        ← báo cáo của calendar-creator
└── portuguese-flashcard/                  ← project khác
```

---

## Projects

### latam-independence-calendar
20 ngày quốc khánh Mỹ Latinh → Google Calendar + Social Media captions

### portuguese-flashcard
Ứng dụng flashcard học tiếng Bồ Đào Nha (React + FastAPI)
→ [`portuguese-flashcard/CLAUDE.md`](portuguese-flashcard/CLAUDE.md)
