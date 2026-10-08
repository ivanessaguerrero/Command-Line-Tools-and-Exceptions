#!/usr/bin/env python3
import argparse
import textwrap


def cowsay(text, width=40):
    wrapped = textwrap.wrap(text, width) if len(text) > width else [text]
    max_len = max(len(line) for line in wrapped)
    
    # Build speech bubble
    lines = []
    lines.append(" " +"_" * (max_len + 2))
    
    if len(wrapped) == 1:
        lines.append(f"| {wrapped[0].ljust(max_len)} |")
    else:
        for i, line in enumerate(wrapped):
            if i == 0:
                lines.append(f"/ {line.ljust(max_len)} \\")
            elif i == len(wrapped) - 1:
                lines.append(f"\\ {line.ljust(max_len)} /")
            else:
                lines.append(f"| {line.ljust(max_len)} |")
    
    lines.append(" " +"-" * (max_len + 2))
    
    # Add cow
    cow = r"""        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||"""
    
    lines.append(cow)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("text", help="The text for the cow to say")
    args = parser.parse_args()
    
    print(cowsay(args.text))


if __name__ == "__main__":
    main()
