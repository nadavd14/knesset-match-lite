"""Knesset Match Lite: cut content/ down to the curated school law set in content/lite_ids.json."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content")


def load(name):
    with open(os.path.join(CONTENT, name), encoding="utf-8") as f:
        return json.load(f)


def save(name, obj, indent=1):
    with open(os.path.join(CONTENT, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def main():
    keep = set(load("lite_ids.json")["ids"])
    laws = [l for l in load("laws.json") if l["billId"] in keep]
    assert len(laws) == len(keep), "unknown bill id in lite_ids.json"
    # plain-language pro/con lines for students (content/lite_args.json) replace the full site's
    args = load("lite_args.json")
    for l in laws:
        a = args[str(l["billId"])]
        l["argFor"], l["argAgainst"], l["argSources"] = a["for"], a["against"], a["sources"]
        l["details"] = re.sub(r"\s*התומכים טענו.*?המתנגדים טענו[^.]*\.", "", l["details"], flags=re.S).strip()
    save("laws.json", laws)
    declared = load("declared.json")
    declared["laws"] = [i for i in declared["laws"] if i in keep]
    for lst in declared["lists"].values():
        lst["positions"] = {k: v for k, v in lst.get("positions", {}).items() if int(k) in keep}
    save("declared.json", declared, indent=2)
    dl = load("declared_laws.json")
    dl["ids"] = [i for i in dl["ids"] if i in keep]
    save("declared_laws.json", dl, indent=None)
    print("laws:", len(laws), "passed:", sum(l["passed"] for l in laws), "declared:", len(declared["laws"]))


if __name__ == "__main__":
    main()
