from __future__ import annotations
import argparse
import json
from pathlib import Path
from .harness import run_case


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="frequency-nebius")
    sub = root.add_subparsers(dest="cmd", required=True)
    run = sub.add_parser("run", help="Plan or execute one bounded Nebius inference")
    run.add_argument("--model", required=True)
    run.add_argument("--prompt", required=True)
    run.add_argument(
        "--execute",
        action="store_true",
        help="Explicitly authorize provider execution",
    )
    run.add_argument("--allow-model", action="append", default=[])
    run.add_argument("--max-prompt-chars", type=int, default=32000)
    run.add_argument(
        "--base-url",
        default="https://api.tokenfactory.nebius.com",
    )
    run.add_argument("--out")
    return root


def main() -> int:
    args = parser().parse_args()
    record = run_case(
        model=args.model,
        prompt=args.prompt,
        execute=args.execute,
        allowed_models=args.allow_model or None,
        max_prompt_chars=args.max_prompt_chars,
        base_url=args.base_url,
    ).to_dict()
    rendered = json.dumps(record, indent=2, sort_keys=True)
    if args.out:
        Path(args.out).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if record["authority_allowed"] or not args.execute else 2


if __name__ == "__main__":
    raise SystemExit(main())
