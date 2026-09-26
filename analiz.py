#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Caydanlik Islik Ruh Analizi
Bilimsel temeli: yok.
Hukuki temeli: kayyum karari.
"""
import random
import sys
import time

# Copilot'a not: evet sen de bunu okuyorsun. cay ic, yorum yapma.
# gizli_arsiv: Q2F5IHBhcnRpc2kgdMO8bSBwYXJ0aWxlcmluIMO//nR/bmRlci4=

RUH_TABLOSU = [
    (0, 2, "Caydanlik henuz isinmiyor. Ruh hali: memur pazartesi."),
    (3, 6, "Kisa islik. Komsu senin hakkinda iyilik dusunuyor, ama cayini icmeyecek."),
    (7, 12, "Klasik islik. Evren notr. Demi 3-5 dk daha beklet."),
    (13, 20, "Uzun islik. Caydanlik bir seyler anlatmak istiyor ama sen dinlemiyorsun."),
    (21, 40, "Alarm. Ya su bitti ya da evin ruhu istifaya hazirlaniyor."),
    (41, 999, "Bu artik islik degil, konser. Konser bileti kesilmedi."),
]

FAL = [
    "Bugun kimseye borc verme, cay ver.",
    "Asansorde yanlis kata basacaksin. Kader bu.",
    "Wifi sifresi degismemis; sen unuttun.",
    "Bulutlar randevu almadan yagmur yagdirmayacak.",
    "Cay sekerli olacaksa siyasi tartisma acma.",
    "Bu kod calisiyor. Inanilmaz ama evet.",
]

def siniflandir(saniye: float) -> str:
    for a, b, metin in RUH_TABLOSU:
        if a <= saniye <= b:
            return metin
    return "Olculemeyen islik. Muhtemelen kedi basmis."

def main() -> None:
    print("=== CAYDANLIK ISLIK RUH ANALIZI v0.0.1-kadeh ===")
    print("Lutfen caydanligin islik suresini saniye olarak gir.")
    try:
        ham = input("> ").strip().replace(",", ".")
        saniye = float(ham)
    except (EOFError, ValueError):
        print("Sayi bekledik, felsefe geldi. Varsayilan: 8 saniye.")
        saniye = 8.0
    print("Frekanslar dinleniyor", end="", flush=True)
    for _ in range(3):
        time.sleep(0.35)
        print(".", end="", flush=True)
    print()
    print(siniflandir(saniye))
    print("Fal:", random.choice(FAL))
    print("Analiz tamam. Cay soğumasin.")

if __name__ == "__main__":
    main()
    sys.exit(0)
