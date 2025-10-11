#!/usr/bin/env python3
"""
Termômetro de Produtividade (Gamificação simples)
- Registra minutos produtivos e de procrastinação por dia
- Calcula score diário = productive / (productive + procrastination)
- Calcula score semanal = sum(productive) / sum(productive + procrastination)
- Armazena em data.json
"""

import json
from pathlib import Path
from datetime import date, datetime, timedelta

DATA_FILE = Path("data.json")
LINE_WIDTH = 35  # largura do termômetro entre as bordas

def load_data():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    return {}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def calc_score(productive_min, procrast_min):
    p = float(productive_min)
    r = float(procrast_min)
    denom = p + r
    if denom == 0:
        return 0.5  # neutro quando não há registro; altere se preferir 0.0
    return max(0.0, min(1.0, p / denom))

def thermometer_line(score, width=LINE_WIDTH):
    # score in [0,1], map to position in [0, width]
    pos = int(round(score * width))
    left = "-" * width
    # place a marker ● at pos (0..width). If pos==0 put at start; if pos==width put at end.
    if pos <= 0:
        visual = "●" + left[1:]
    elif pos >= width:
        visual = left[:-1] + "●"
    else:
        visual = left[:pos] + "●" + left[pos+1:]
    return f"|{visual}|"

def register_today(productive_min, procrast_min, the_date=None):
    data = load_data()
    d = (the_date or date.today()).isoformat()
    data.setdefault(d, {})
    data[d]["productive_min"] = int(productive_min)
    data[d]["procrast_min"] = int(procrast_min)
    data[d]["timestamp"] = datetime.now().isoformat()
    save_data(data)
    return d

def get_day_entry(d):
    data = load_data()
    return data.get(d)

def week_range_for(date_obj=None):
    # semana com 7 dias terminando hoje (inclusive). Você pode preferir semana Mon-Sun; aqui é rolling 7 dias.
    today = date_obj or date.today()
    start = today - timedelta(days=6)
    return start, today

def weekly_summary(end_date=None):
    start, end = week_range_for(end_date)
    data = load_data()
    total_p = 0
    total_r = 0
    days_with_data = []
    cur = start
    while cur <= end:
        d = cur.isoformat()
        entry = data.get(d)
        if entry:
            p = int(entry.get("productive_min", 0))
            r = int(entry.get("procrast_min", 0))
            total_p += p
            total_r += r
            days_with_data.append((d, p, r))
        cur += timedelta(days=1)
    score = calc_score(total_p, total_r) if (total_p + total_r) > 0 else 0.5
    return {
        "start": start.isoformat(),
        "end": end.isoformat(),
        "total_productive_min": total_p,
        "total_procrast_min": total_r,
        "score": score,
        "days": days_with_data
    }

def print_day_report(d=None):
    d = d or date.today().isoformat()
    entry = get_day_entry(d)
    if not entry:
        print(f"Sem registro para {d}.")
        return
    p = entry.get("productive_min", 0)
    r = entry.get("procrast_min", 0)
    score = calc_score(p, r)
    print(f"Data: {d}")
    print(f"Produtivo: {p} min | Procrastinação: {r} min")
    print(f"Score diário: {score:.3f}")
    print(thermometer_line(score))
    print("0" + " " * (LINE_WIDTH - 1) + "1")

def print_week_report(end_date=None):
    summary = weekly_summary(end_date)
    print(f"Semana: {summary['start']} → {summary['end']}")
    print(f"Total produtivo: {summary['total_productive_min']} min")
    print(f"Total procrastinação: {summary['total_procrast_min']} min")
    print(f"Score semanal: {summary['score']:.3f}")
    print(thermometer_line(summary['score']))
    print("0" + " " * (LINE_WIDTH - 1) + "1")
    if summary["days"]:
        print("\nDias com registro (data | produtivo min | procrast min):")
        for d,p,r in summary["days"]:
            print(f"- {d} | {p} | {r}")

def interactive_cli():
    print("Termômetro de Produtividade\nComandos: register / today / week / exit")
    while True:
        cmd = input("comando> ").strip().lower()
        if cmd in ("exit", "q"):
            break
        if cmd == "register":
            d_input = input("Data (YYYY-MM-DD) [enter para hoje]: ").strip()
            try:
                the_date = date.fromisoformat(d_input) if d_input else date.today()
            except Exception:
                print("Data inválida.")
                continue
            try:
                p = int(input("Minutos produtivos (estudo/leitura): ").strip())
                r = int(input("Minutos procrastinando (redes/stream/jogos): ").strip())
            except ValueError:
                print("Por favor informe números inteiros de minutos.")
                continue
            register_today(p, r, the_date)
            print(f"Registro salvo para {the_date.isoformat()}.")
        elif cmd == "today":
            print_day_report()
        elif cmd == "week":
            print_week_report()
        else:
            print("Comando desconhecido. Use register / today / week / exit")

if __name__ == "__main__":
    interactive_cli()