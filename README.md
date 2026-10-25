# מי מצביע כמוני? LITE · Knesset Match Lite

גרסה לכיתה של [Knesset Match](https://github.com/nadavd14/knesset-match): אותו אתר, עם 60 חוקים שנבחרו כנגישים לתלמידי תיכון (30 עברו, 30 נדחו; 33 עם עמדות מוצהרות). רשימת החוקים ב־`content/lite_ids.json`; `python pipeline/lite_filter.py` מצמצם את `content/` לפיה.

אתר סטטי: מצביעים על חוקים אמיתיים מהכנסת ה־25 ורואים את אחוז ההתאמה לרשימות לכנסת ה־26 (מקומות ריאליים) ולסיעות הכנסת ה־25. החישוב כולו בדפדפן, בלי שרת.

```
python pipeline/fetch.py          # base tables → data/raw/
python pipeline/select_votes.py   # final votes + results → data/candidates.json
python pipeline/lite_filter.py    # content/ → 60 Lite laws
python pipeline/build.py          # → site/data/data.json
python -m unittest discover tests && node --test tests/
python -m http.server -d site 8080
```

Data: Knesset OData (`knesset.gov.il/OdataV4/ParliamentInfo`). Design: `docs/superpowers/specs/`.
