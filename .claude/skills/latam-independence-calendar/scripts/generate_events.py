"""
Generate Google Calendar event payloads for LATAM independence days.
Usage: python generate_events.py [--year 2026] [--country Mexico]
Output: events_YYYY.json ready to review before pushing to Google Calendar via MCP.
"""

import json
import argparse
from datetime import date, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "latam_countries.json"
OUTPUT_DIR = Path(__file__).parent.parent / "output"


def build_event(country: dict, target_year: int) -> dict:
    month, day = map(int, country["independence_date"].split("-"))
    independence_day = date(target_year, month, day)
    years = target_year - country["year"]

    summary = f"{country['flag']} Quốc khánh {country['country_vi']} ({years} năm)"
    description = (
        f"🌎 {country['country']} tuyên bố độc lập năm {country['year']} "
        f"khỏi {country['from_vi']}.\n\n"
        f"📝 Nhắc nhở: Chuẩn bị bài chúc mừng trên mạng xã hội!\n"
        f"Template có tại: latam-independence-calendar/templates/"
    )

    reminders = [
        {"method": "popup", "minutes": days_before * 24 * 60}
        for days_before in country["reminder_days_before"]
    ]

    return {
        "summary": summary,
        "description": description,
        "start": {"date": independence_day.isoformat()},
        "end": {"date": (independence_day + timedelta(days=1)).isoformat()},
        "reminders": {
            "useDefault": False,
            "overrides": reminders
        },
        "colorId": "11",
        "_meta": {
            "country": country["country"],
            "country_vi": country["country_vi"],
            "independence_date": country["independence_date"],
            "years": years
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Generate LATAM calendar events")
    parser.add_argument("--year", type=int, default=date.today().year)
    parser.add_argument("--country", type=str, default=None, help="Filter by country name")
    args = parser.parse_args()

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    countries = data["countries"]

    if args.country:
        countries = [c for c in countries if args.country.lower() in c["country"].lower()]

    events = [build_event(c, args.year) for c in countries]
    events.sort(key=lambda e: e["start"]["date"])

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_file = OUTPUT_DIR / f"events_{args.year}.json"
    out_file.write_text(json.dumps(events, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Generated {len(events)} events -> {out_file}")
    for e in events:
        print(f"  {e['start']['date']}  {e['_meta']['country']}")


if __name__ == "__main__":
    main()
